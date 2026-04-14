---
name: "json-canvas"
description: "Create and edit JSON Canvas files (.canvas) with nodes, edges, groups. Invoke when working with .canvas files, creating mind maps, flowcharts, or visual canvases."
---

# JSON Canvas Skill

## File Structure

A canvas file (`.canvas`) contains two top-level arrays:

```json
{
  "nodes": [],
  "edges": []
}
```

## Common Workflows

### 1. Create a New Canvas

1. Create a `.canvas` file with base structure `{"nodes": [], "edges": []}`
2. Generate unique 16-character hex IDs for each node
3. Add nodes with required fields: `id`, `type`, `x`, `y`, `width`, `height`
4. Add edges referencing valid node IDs via `fromNode` and `toNode`
5. Validate: Parse JSON to confirm validity

### 2. Node Types

| Type | Required Fields |
|------|-----------------|
| `text` | `text` (Markdown content) |
| `file` | `file` (path to file) |
| `link` | `url` (external URL) |
| `group` | `label` (optional) |

### 3. Text Node Example

```json
{
  "id": "6f0ad84f44ce9c17",
  "type": "text",
  "x": 0,
  "y": 0,
  "width": 400,
  "height": 200,
  "text": "# Hello World\n\nThis is **Markdown** content."
}
```

### 4. Edge Example

```json
{
  "id": "0123456789abcdef",
  "fromNode": "6f0ad84f44ce9c17",
  "fromSide": "right",
  "toNode": "a1b2c3d4e5f67890",
  "toSide": "left",
  "toEnd": "arrow",
  "label": "leads to"
}
```

## Colors

Preset colors: `"1"` (Red), `"2"` (Orange), `"3"` (Yellow), `"4"` (Green), `"5"` (Cyan), `"6"` (Purple)

Or use hex: `"#FF0000"`

## Layout Guidelines

- Coordinates can be negative (canvas extends infinitely)
- `x` increases right, `y` increases down
- Space nodes 50-100px apart
- Align to grid (multiples of 10 or 20)
