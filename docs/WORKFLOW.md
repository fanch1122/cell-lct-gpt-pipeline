# Workflow and quality gates

## 1. Text manifest

Record content, line breaks, x/y coordinates, bounding box, font family, font size, weight, color, rotation, alignment, opacity, z-index, and paint order before editing the image.

## 2. Text-only cleanup

Remove only visible glyphs. Preserve frames, arrows, tails, connectors, charts, icons, colors, spacing, hierarchy, and canvas dimensions. Generate more than one candidate when needed, then select by structural fidelity rather than by cleanliness alone.

## 3. Semantic reconstruction

Build the figure from meaningful objects such as `rect`, `line`, `polyline`, `polygon`, `circle`, and `path`. Repeated visual units stay independent. Arrow shafts and arrowheads are explicit editable objects.

Reject:

- embedded raster images;
- thousands of tiny same-style paths;
- outlined text used in place of live text;
- malformed coordinates;
- unsupported gradients, masks, clipping groups, filters, or effects.

## 4. Master SVG

Restore text before caching and preserve SVG paint order. Assign a stable unique ID to every editable primitive.

## 5. Cache and playback

Parse the complete Master SVG once. Reuse the generated cache for all batches. Ordinary batches contain 20–50 consecutive atoms. Keep one Illustrator connection throughout the session.

## 6. Completion gate

- text removal preserves all non-text structures;
- SVG contains no unintended raster node;
- text is live and editable;
- strict ID validation passes;
- cache is generated once;
- all batches complete;
- existing Illustrator artwork remains unchanged;
- AI is saved and final PNG is visually inspected.
