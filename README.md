# Cell-lct GPT Scientific Figure Pipeline

An editable scientific-figure reconstruction workflow for Adobe Illustrator:

`reference image -> text manifest -> GPT Image text removal -> semantic SVG reconstruction -> SVG validation -> immutable geometry cache -> batched Illustrator playback`

The pipeline avoids pixel tracing. Text remains live SVG text, connectors remain meaningful lines, and repeated shapes remain separate editable objects.

## Workflow

1. Preserve the untouched reference image.
2. Record every visible text run and its position/style in a text manifest.
3. Use GPT Image editing to remove text only. Compare multiple versions and reject any version that deletes non-text structure.
4. Reconstruct the cleaned reference as semantic SVG geometry. Do not embed a raster image and do not produce a pixel mosaic.
5. Merge the recorded text back as live `<text>` elements.
6. Validate the Master SVG.
7. Parse it once into an immutable geometry cache.
8. Draw consecutive batches into the currently open Illustrator document while preserving existing artwork.

## Requirements

- Windows
- Adobe Illustrator 2026 (30.x)
- PowerShell 5.1+
- Python 3.11+
- GPT Image access for the text-removal stage

The text-removal call is intentionally not hard-coded into this repository. Use your authorized image-editing client and keep credentials outside the repository.

## Validation

```powershell
python scripts/validate_vector_svg.py --svg path/to/master.svg --strict-ids
python scripts/validate_manifest.py --manifest path/to/text-manifest.json
```

The SVG must contain real vector primitives, no raster `<image>` nodes, stable IDs, and live text.

## Cache and Illustrator playback

```powershell
python scripts/prepare_geometry_cache.py `
  --input path/to/master.svg `
  --output-dir path/to/work `
  --job-id example `
  --min-batch-size 20 `
  --max-batch-size 40

powershell -ExecutionPolicy Bypass -File scripts/run_cell_lct.ps1 `
  -InputSvg path/to/master.svg `
  -WorkDir path/to/work `
  -OutputAi path/to/result.ai `
  -OutputPng path/to/result.png
```

Open Illustrator and the target document yourself before playback. The runner appends new editable objects and does not delete existing artwork.

## Repository layout

- `scripts/`: validation, text merge, cache preparation, and playback orchestration
- `runtime/`: Illustrator JSX playback runtime
- `examples/euktaxa/`: semantic SVG builder and generated editable SVG example
- `docs/`: workflow and quality gates

## Security

- Never commit API keys, access tokens, cookies, generated credential files, or `.env` files.
- Do not place secrets in command-line arguments or logs.
- Keep source images private unless you have permission to publish them.

## License

MIT
