#!/usr/bin/env python3
"""Offline A3M teaching exercise; no sequence search or structure prediction."""

import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
import random


HERE = Path(__file__).resolve().parent
AMINO_ACIDS = "ACDEFGHIKLMNPQRSTVWYX"
ALLOWED = set(AMINO_ACIDS + AMINO_ACIDS.lower() + "-")
NOTICE = "학습용 문자열 조작만 수행함. 구조 예측 또는 실험 결과가 아님."


def aligned(sequence):
    """Lowercase A3M insertions do not occupy query-aligned columns."""
    return "".join(char for char in sequence if not char.islower())


def parse_a3m(text):
    """Read our monomer teaching subset; reject unsupported syntax explicitly."""
    rows = []
    for line_number, line in enumerate(text.splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            header = line[1:].strip()
            if not header:
                raise ValueError(f"{line_number}행: 빈 FASTA header")
            rows.append((header, ""))
        else:
            if not rows:
                raise ValueError(f"{line_number}행: sequence 전에 >header가 필요함")
            invalid = set(line) - ALLOWED
            if invalid:
                raise ValueError(f"{line_number}행: 지원하지 않는 문자 {sorted(invalid)!r}")
            header, sequence = rows[-1]
            rows[-1] = (header, sequence + line)
    if not rows or any(not sequence for _, sequence in rows):
        raise ValueError("빈 MSA 또는 빈 sequence")
    ids = [header.split()[0] for header, _ in rows]
    if len(set(ids)) != len(ids):
        raise ValueError("sequence ID는 중복될 수 없음")
    query = rows[0][1]
    if any(char not in AMINO_ACIDS for char in query):
        raise ValueError("첫 행 query는 gap/소문자 없는 대문자 아미노산이어야 함")
    if any(len(aligned(sequence)) != len(query) for _, sequence in rows):
        raise ValueError("소문자 제거 후 모든 행의 정렬 길이가 query와 같아야 함")
    return rows


def encode_a3m(rows):
    return "".join(f">{header}\n{sequence}\n" for header, sequence in rows)


def insertion_counts(sequence):
    """Count insertions before each aligned column and after the last column."""
    counts, pending = [], 0
    for char in sequence:
        if char.islower():
            pending += 1
        else:
            counts.append(pending)
            pending = 0
    return counts, pending


def subsample(rows, depth, seed):
    if not 1 <= depth <= len(rows):
        raise ValueError(f"depth는 query 포함 1..{len(rows)} 범위여야 함")
    indices = sorted(random.Random(seed).sample(range(1, len(rows)), depth - 1))
    return [rows[0]] + [rows[index] for index in indices]


def prelabelled_groups(rows):
    """Split provided labels, not a clustering or AF-Cluster implementation."""
    groups = {"A": [rows[0]], "B": [rows[0]]}
    for row in rows[1:]:
        labels = [token for token in row[0].split() if token.startswith("group=")]
        if len(labels) != 1 or labels[0] not in ("group=A", "group=B"):
            raise ValueError("모든 homolog header에 group=A 또는 group=B 하나가 필요함")
        groups[labels[0][-1]].append(row)
    if any(len(group) == 1 for group in groups.values()):
        raise ValueError("실습에는 A/B 그룹에 각각 homolog가 하나 이상 필요함")
    return groups


def mask_homologs(rows, columns):
    """Replace homolog residues with X; preserve query, insertions and gaps."""
    if not columns or any(column < 1 or column > len(rows[0][1]) for column in columns):
        raise ValueError("mask 열은 query의 1-based 열 번호 범위여야 함")
    masked = [rows[0]]
    for header, sequence in rows[1:]:
        new_sequence, column = [], 0
        for char in sequence:
            if not char.islower():
                column += 1
                if column in columns and char != "-":
                    char = "X"
            new_sequence.append(char)
        masked.append((header, "".join(new_sequence)))
    return masked


def self_test():
    rows = parse_a3m((HERE / "fictional_learning.a3m").read_text(encoding="utf-8"))
    original = tuple(rows)
    assert len(rows) == 7 and len(rows[0][1]) == 12
    assert aligned(rows[2][1]) == rows[0][1]
    assert insertion_counts(rows[2][1]) == ([0, 0, 0, 2] + [0] * 8, 0)
    assert insertion_counts("aACtt") == ([1, 0], 2)
    assert parse_a3m(">q\nAC\nDE\n>h\nACaaDE\n")[1][1] == "ACaaDE"
    sample = subsample(rows, 4, 7)
    assert sample == subsample(rows, 4, 7) and len(sample) == 4
    assert sample[0] == rows[0] and subsample(rows, 1, 0) == rows[:1]
    assert subsample(rows, len(rows), 0) == rows
    groups = prelabelled_groups(rows)
    assert all(len(group) == 4 and group[0] == rows[0] for group in groups.values())
    assert groups["A"][1:] == rows[1:4] and groups["B"][1:] == rows[4:]
    masked = mask_homologs(rows, {5, 7, 10})
    assert masked[0] == rows[0]
    assert masked[2][1] == "ACDeeEXGXIKXMN"
    assert aligned(masked[3][1])[4] == "-"
    for before, after in zip(rows[1:], masked[1:]):
        assert before[0] == after[0]
        assert [c for c in before[1] if c.islower()] == [c for c in after[1] if c.islower()]
        assert [i for i, c in enumerate(before[1]) if c == "-"] == [i for i, c in enumerate(after[1]) if c == "-"]
        for column, (old, new) in enumerate(zip(aligned(before[1]), aligned(after[1])), 1):
            assert new == ("X" if column in {5, 7, 10} and old != "-" else old)
    assert tuple(rows) == original
    assert parse_a3m(encode_a3m(masked)) == masked
    invalid_actions = [
        lambda: parse_a3m(""),
        lambda: parse_a3m("ACD\n"),
        lambda: parse_a3m(">q\nACD\n>h\nAC\n"),
        lambda: parse_a3m(">q\nAcD\n"),
        lambda: parse_a3m(">q\nA-D\n"),
        lambda: parse_a3m(">q\nACD\n>q\nACD\n"),
        lambda: parse_a3m(">q\nACD\n>h\nAC.\n"),
        lambda: subsample(rows, 0, 7),
        lambda: subsample(rows, 8, 7),
        lambda: mask_homologs(rows, {13}),
        lambda: mask_homologs(rows, {0}),
        lambda: prelabelled_groups(rows[:2]),
        lambda: prelabelled_groups([rows[0], ("unlabelled", rows[1][1])]),
    ]
    for action in invalid_actions:
        try:
            action()
        except ValueError:
            pass
        else:
            raise AssertionError("invalid input was accepted")
    print("SELF-TEST PASS: parsing, query, insertions, gaps, depth, labels, mask, invalid inputs")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--input", type=Path, default=HERE / "fictional_learning.a3m")
    parser.add_argument("--out", type=Path, help="새 폴더만 허용; 기존 자료를 덮어쓰지 않음")
    parser.add_argument("--depth", type=int, default=4, help="query를 포함한 행 수")
    parser.add_argument("--seed", type=int, default=7, help="행 추출용 seed; 예측 seed가 아님")
    parser.add_argument("--mask-columns", default="5,7,10", help="query 정렬 열, 1-based")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    try:
        source = args.input.read_bytes()
        rows = parse_a3m(source.decode("utf-8"))
        try:
            columns = {int(value) for value in args.mask_columns.split(",")}
        except ValueError as error:
            raise ValueError("--mask-columns 예: 5,7,10") from error
        groups = prelabelled_groups(rows)
        variants = {
            "subsample.a3m": subsample(rows, args.depth, args.seed),
            "group_A.a3m": groups["A"],
            "group_B.a3m": groups["B"],
            "masked.a3m": mask_homologs(rows, columns),
        }
        for name, variant in variants.items():
            if variant[0] != rows[0] or parse_a3m(encode_a3m(variant)) != variant:
                raise ValueError(f"{name}: 출력 검증 실패")
        report = {
            "notice": NOTICE,
            "input_file": str(args.input.resolve()),
            "input_sha256": hashlib.sha256(source).hexdigest(),
            "depth_including_query": len(rows),
            "query_length": len(rows[0][1]),
            "subsample_depth_including_query": args.depth,
            "row_sampling_seed": args.seed,
            "mask_query_columns_1based": sorted(columns),
            "query_preserved": True,
            "grouping_method": "provided header labels only; NOT AF-Cluster",
            "masking_method": "homolog uppercase residue to X; NOT AFsample2 implementation",
            "rows": [],
            "outputs": {name: {"depth_including_query": len(variant), "ids": [row[0].split()[0] for row in variant]} for name, variant in variants.items()},
        }
        for header, sequence in rows:
            counts, trailing = insertion_counts(sequence)
            match = aligned(sequence)
            report["rows"].append({
                "id": header.split()[0], "raw_a3m": sequence,
                "aligned": match, "raw_length": len(sequence),
                "aligned_length": len(match), "gap_count": match.count("-"),
                "unknown_X_count": match.count("X"),
                "insertion_count_before_column": counts,
                "trailing_insertion_count": trailing,
            })
        out = args.out or HERE / "runs" / datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        out.mkdir(parents=True, exist_ok=False)
        for name, variant in variants.items():
            (out / name).write_text(encode_a3m(variant), encoding="utf-8")
        (out / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        for name, variant in variants.items():
            if parse_a3m((out / name).read_text(encoding="utf-8")) != variant:
                raise ValueError(f"{name}: 저장 후 재검증 실패")
        if args.input.read_bytes() != source:
            raise ValueError("입력 파일이 실행 중 변경됨")
        print(NOTICE)
        print(f"입력: {len(rows)}행(query 포함), {len(rows[0][1])} 정렬 열")
        for row in report["rows"]:
            print(f"  {row['id']:12} {row['aligned']}  gap={row['gap_count']} X={row['unknown_X_count']}")
        print(f"출력/저장 검증 완료: {out.resolve()}")
        print("group_A/B는 사전 라벨 분리이며 구조 상태를 뜻하지 않습니다.")
    except (OSError, UnicodeError, ValueError) as error:
        parser.exit(2, f"오류: {error}\n")


if __name__ == "__main__":
    main()
