# Repository Guidelines

## Project Structure & Module Organization

This workspace contains `moleculeview/`, a Korean, three-hour biomolecular structure lesson. Read `moleculeview/AGENTS.md` for additional project-specific guidance.

- `moleculeview/content/`: slide text, timing, speaker notes, and references in JSON. Edit `foundations.json` and `structure_reading.json`; `teacher_notes.md` is generated.
- `moleculeview/assets/structures/`: original PDB coordinates; `assets/figures/`: teaching images.
- `moleculeview/build/`: Python builders, export scripts, intermediate artifacts, and preview images. This directory contains source code, so do not treat it as disposable.
- `moleculeview/output/`: reviewed lecture PPTX/PDF and student worksheet PDF.

## Build, Test, and Development Commands

Run these commands from `moleculeview/` (`cd moleculeview` from the workspace root). Dependencies are `python-pptx`, Pillow, and PyMuPDF; builders require `/Library/Fonts/Arial Unicode.ttf`.

```sh
python3 build/build_deck.py
python3 build/build_worksheet.py
osascript build/export_pdf.applescript "$PWD/build/biomolecule_view_3h_ko.pptx" "$PWD/build/biomolecule_view_3h_ko.pdf"
```

These build the editable deck, generated notes/check report, worksheet, and lecture PDF, respectively. PDF export requires macOS and Microsoft PowerPoint.

For molecular-image changes, run `python3 build/render_structures.py` with PyMOL installed, then `python3 build/fix_assessment_labels.py`. Rebuild affected documents afterward. Review artifacts before copying them into `output/`.

## Coding Style & Naming Conventions

Use four-space Python indentation, `snake_case` functions, and uppercase constants. Follow nearby formatting; no formatter or linter is configured. Preserve UTF-8 Korean text and use two-space indentation in slide JSON. Retain descriptive PDB-prefixed image names, such as `2ITY_hbond.png`. Keep teaching content in Korean with relevant English terminology.

## Testing Guidelines

There is no dedicated test framework or coverage threshold. Running the builders executes assertions for sequential slide IDs, 52 slides, 180 minutes including 20 minutes of breaks, text fit, and slide bounds.

After rebuilding, inspect rendered pages for overlap, clipping, Korean glyphs, and residue labels. Confirm lecture and worksheet PDFs contain 52 and 2 pages. Keep assessment answers in instructor materials.

## Commit & Pull Request Guidelines

No Git metadata is available to establish historical conventions. Recommended commit subjects are concise and imperative, e.g., `Fix residue labels in assessment figures`. PRs should describe changed content, validation performed, and affected outputs; include screenshots for visual changes and link relevant issues when available.

## Scientific Integrity & File Safety

Preserve coordinate provenance, residue numbering, citations, and image licenses. Ground scientific claims in source data and figures. Archive superseded artifacts instead of deleting them; gitignore large raw datasets rather than committing them.
