# Repository Guidelines

## Project Structure

This project produces a Korean, three-hour Biomolecule View lesson for biology-background master's students with no assumed chemistry knowledge. Activities use paper or oral responses.

- `content/foundations.json` and `content/structure_reading.json`: slide text, timing, speaker notes, and source keys.
- `content/sources.json`: scientific references and image attribution.
- `assets/structures/`: original PDB coordinates; `assets/figures/`: teaching images.
- `build/`: Python builders, PowerPoint export script, intermediate artifacts, and previews.
- `output/`: reviewed lecture PPTX/PDF and student worksheet PDF.

Edit source JSON rather than generated `content/teacher_notes.md` or `build/content_all.json`.

## Build and Development Commands

Run from the repository root. Python dependencies are `python-pptx`, Pillow, and PyMuPDF. Builders expect `/Library/Fonts/Arial Unicode.ttf`; the deck uses Arial Unicode MS.

```sh
python3 build/build_deck.py
python3 build/build_worksheet.py
osascript build/export_pdf.applescript "$PWD/build/biomolecule_view_3h_ko.pptx" "$PWD/build/biomolecule_view_3h_ko.pdf"
```

The first command builds the editable deck, notes, and check report. The second builds the worksheet. PDF export requires macOS and Microsoft PowerPoint.

When changing molecular views, run `python3 build/render_structures.py` with PyMOL installed, followed by `python3 build/fix_assessment_labels.py` to restore assessment labels. Review generated artifacts before copying them into `output/`.

## Coding Style and Naming

Use four-space Python indentation, `snake_case` functions, UTF-8 JSON, and descriptive filenames. Retain PDB prefixes such as `2ITY_hbond.png`. Keep instructional content in Korean with relevant English terminology. No formatter or linter configuration is present; follow nearby code.

## Validation

There is no dedicated test suite or coverage threshold. The deck builder asserts sequential slide IDs, 64 slides, 180 minutes including 20 minutes of breaks, estimated text fit, and shape bounds. The worksheet builder checks text fit.

After changes, rebuild affected artifacts and visually inspect rendered pages for clipping, overlap, Korean glyphs, and molecular labels. Confirm lecture and worksheet PDFs contain 64 and 2 pages respectively. Keep worksheet answers in instructor materials.

## Commits and Pull Requests

No Git metadata is available here to establish historical conventions. Use concise imperative subjects, such as `Fix residue labels in assessment figures`. Describe changed teaching content, validation performed, and affected outputs. Include slide screenshots for visual changes and link relevant issues when available.

## Scientific Integrity and File Safety

Preserve coordinate provenance, residue numbering, citations, and image licenses. Distinguish observed proximity from binding-strength claims. Archive superseded artifacts instead of destructively deleting them.
