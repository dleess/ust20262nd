#!/usr/bin/env python3
"""Validate one protein FASTA and its A3M; prepare inputs without inference."""

import argparse
import hashlib
import json
from pathlib import Path
import tempfile


AMINO_ACIDS = "ACDEFGHIKLMNPQRSTVWYX"


def sequences(text, allowed, single_line=False):
    """Read multiline FASTA/A3M; do not change residue case or gaps."""
    rows = []
    for number, line in enumerate(text.splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            if not line[1:].strip():
                raise ValueError(f"{number}행: 빈 header")
            rows.append("")
        else:
            if not rows or set(line) - allowed:
                raise ValueError(f"{number}행: header 없는 서열 또는 지원하지 않는 문자")
            if single_line and rows[-1]:
                raise ValueError("Boltz 입력 호환을 위해 A3M의 각 sequence는 한 줄이어야 함")
            rows[-1] += line
    if not rows or any(not row for row in rows):
        raise ValueError("빈 FASTA/A3M 또는 빈 sequence")
    return rows


def validate(fasta_bytes, msa_bytes):
    query_rows = sequences(fasta_bytes.decode("utf-8"), set(AMINO_ACIDS))
    if len(query_rows) != 1:
        raise ValueError("FASTA에는 대문자 단백질 서열 하나만 있어야 함")
    query = query_rows[0]
    msa_text = msa_bytes.decode("utf-8")
    lines = msa_text.splitlines()
    first = next((i for i, line in enumerate(lines) if line.strip()), None)
    if first is not None and lines[first].startswith("#"):
        if lines[first][1:].split() != [str(len(query)), "1"]:
            raise ValueError("ColabFold metadata는 #query길이<TAB>1 단량체만 지원함")
        # Only skip metadata for validation; the original bytes are copied.
        lines.pop(first)
    allowed = set(AMINO_ACIDS + AMINO_ACIDS.lower() + "-")
    rows = sequences("\n".join(lines), allowed, single_line=True)
    if rows[0] != query:
        raise ValueError("A3M 첫 query가 FASTA 서열과 정확히 일치하지 않음")
    if any(sum(not char.islower() for char in row) != len(query) for row in rows):
        raise ValueError("A3M의 소문자 삽입 제외 정렬 길이가 query와 다름")
    return query, len(rows)


def prepare(fasta_path, msa_path, output):
    fasta_bytes = fasta_path.read_bytes()
    msa_bytes = msa_path.read_bytes()
    query, depth = validate(fasta_bytes, msa_bytes)
    output = output.resolve()
    af3 = {
        "name": "calmodulin",
        "modelSeeds": [0, 1, 2],
        "sequences": [{"protein": {
            "id": "A", "sequence": query,
            "unpairedMsaPath": "target.a3m", "pairedMsa": "", "templates": [],
        }}],
        "dialect": "alphafold3",
        "version": 2,
    }
    boltz = (
        "version: 1\nsequences:\n  - protein:\n      id: A\n"
        f"      sequence: {json.dumps(query)}\n"
        f"      msa: {json.dumps(str(output / 'target.a3m'))}\n"
    )
    files = {
        "target.a3m": msa_bytes,
        "alphafold3.json": (json.dumps(af3, indent=2) + "\n").encode("utf-8"),
        "boltz.yaml": boltz.encode("utf-8"),
        "chai.fasta": f">protein|calmodulin\n{query}\n".encode("utf-8"),
        "esm.fasta": f">calmodulin\n{query}\n".encode("utf-8"),
    }
    output.mkdir(parents=True, exist_ok=False)
    for name, data in files.items():
        with (output / name).open("xb") as handle:
            handle.write(data)
    if any((output / name).read_bytes() != data for name, data in files.items()):
        raise ValueError("저장 파일 재검증 실패")
    if fasta_path.read_bytes() != fasta_bytes or msa_path.read_bytes() != msa_bytes:
        raise ValueError("실행 중 원본 입력 파일이 변경됨")
    return len(query), depth, hashlib.sha256(msa_bytes).hexdigest()


def self_test():
    # A tiny synthetic fixture exercises file preparation, not biology/inference.
    with tempfile.TemporaryDirectory(prefix="prepare-inputs-test-") as temporary:
        folder = Path(temporary)
        fasta, msa = folder / "query.fasta", folder / "input.a3m"
        fasta.write_text(">fictional_test_only\nACD\nEFG\n", encoding="utf-8")
        original = b"#6\t1\n>query\nACDEFG\n>homolog\nACDttEFG\n>gap\nA-DEFG\n"
        msa.write_bytes(original)
        output = folder / "space and ' quote"
        length, depth, digest = prepare(fasta, msa, output)
        assert (length, depth) == (6, 3)
        assert digest == hashlib.sha256(original).hexdigest()
        assert (output / "target.a3m").read_bytes() == original == msa.read_bytes()
        af3 = json.loads((output / "alphafold3.json").read_text())
        assert af3["version"] == 2 and af3["dialect"] == "alphafold3"
        assert af3["modelSeeds"] == [0, 1, 2]
        protein = af3["sequences"][0]["protein"]
        assert protein == {"id": "A", "sequence": "ACDEFG", "unpairedMsaPath": "target.a3m", "pairedMsa": "", "templates": []}
        assert (output / protein["unpairedMsaPath"]).read_bytes() == original
        msa_line = (output / "boltz.yaml").read_text().splitlines()[-1]
        assert Path(json.loads(msa_line.split("msa: ", 1)[1])).read_bytes() == original
        assert (output / "chai.fasta").read_text() == ">protein|calmodulin\nACDEFG\n"
        assert (output / "esm.fasta").read_text() == ">calmodulin\nACDEFG\n"
        try:
            prepare(fasta, msa, output)
        except FileExistsError:
            pass
        else:
            raise AssertionError("existing output directory was accepted")
        invalid = [
            (b">q\nACDEFG\n>q2\nACDEFG\n", original),
            (fasta.read_bytes(), original.replace(b"#6\t1", b"#6\t2")),
            (fasta.read_bytes(), b">q\nACDEFA\n"),
            (fasta.read_bytes(), b">q\nACDEFG\n>h\nACDEF\n"),
            (fasta.read_bytes(), b">q\nACDEFG\n>h\nAC.EFG\n"),
            (fasta.read_bytes(), b">q\nACD\nEFG\n>h\nACDEFG\n"),
            (b">q\nAcDEFG\n", original),
            (b"", original),
            (fasta.read_bytes(), b""),
        ]
        for bad_fasta, bad_msa in invalid:
            try:
                validate(bad_fasta, bad_msa)
            except ValueError:
                pass
            else:
                raise AssertionError("invalid input was accepted")
        plain = original.split(b"\n", 1)[1]
        assert validate(fasta.read_bytes(), plain) == ("ACDEFG", 3)
    print("SELF-TEST PASS: query, widths, insertions, metadata, paths, files, no overwrite")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fasta", type=Path, nargs="?")
    parser.add_argument("a3m", type=Path, nargs="?")
    parser.add_argument("--out", type=Path, default=Path("prepared"))
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    if args.fasta is None or args.a3m is None:
        parser.error("FASTA와 실제 query A3M 경로를 지정하세요")
    try:
        length, depth, digest = prepare(args.fasta, args.a3m, args.out)
    except (OSError, UnicodeError, ValueError) as error:
        parser.exit(2, f"오류: {error}\n")
    print(f"준비/저장 검증 완료: {args.out.resolve()} ({length} 잔기, query 포함 {depth}행)")
    print(f"원본/복사본 A3M SHA-256: {digest}")
    print("MSA 검색·구조 예측을 실행하지 않았습니다. 입력 생물학적 출처는 별도로 확인하세요.")


if __name__ == "__main__":
    main()
