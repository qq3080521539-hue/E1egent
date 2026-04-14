---
name: ai-image-generation
description: "Generate AI images with FLUX, Gemini, Grok, Seedream, Reve and 50+ models via inference.sh CLI. Invoke when user asks to generate images, create AI art, product mockups, or visual content."
allowed-tools: Bash(infsh *)
---

# AI Image Generation

Generate images with 50+ AI models via [inference.sh](https://inference.sh) CLI.

## Quick Start

> Requires inference.sh CLI (`infsh`). [Install instructions](https://raw.githubusercontent.com/inference-sh/skills/refs/heads/main/cli-install.md)

```bash
infsh login

# Generate an image with FLUX
infsh app run falai/flux-dev-lora --input '{"prompt": "a cat astronaut in space"}'
```

## Available Models

| Model | App ID | Best For |
|-------|--------|----------|
| FLUX Dev LoRA | `falai/flux-dev-lora` | High quality with custom styles |
| FLUX.2 Klein LoRA | `falai/flux-2-klein-lora` | Fast with LoRA support |
| P-Image | `pruna/p-image` | Fast, economical |
| Gemini 3 Pro | `google/gemini-3-pro-image-preview` | Google's latest |
| Grok Imagine | `xai/grok-imagine-image` | xAI's model |
| Seedream 4.5 | `bytedance/seedream-4-5` | 2K-4K cinematic quality |
| Reve | `falai/reve` | Natural language editing |
| ImagineArt 1.5 Pro | `falai/imagine-art-1-5-pro-preview` | Ultra-high-fidelity 4K |
| Topaz Upscaler | `falai/topaz-image-upscaler` | Professional upscaling |

## Examples

### Text-to-Image with FLUX

```bash
infsh app run falai/flux-dev-lora --input '{
  "prompt": "professional product photo of a coffee mug, studio lighting"
}'
```

### Grok Imagine

```bash
infsh app run xai/grok-imagine-image --input '{
  "prompt": "cyberpunk city at night",
  "aspect_ratio": "16:9"
}'
```

### Seedream 4.5 (4K Quality)

```bash
infsh app run bytedance/seedream-4-5 --input '{
  "prompt": "cinematic portrait of a woman, golden hour lighting"
}'
```

### Image Upscaling

```bash
infsh app run falai/topaz-image-upscaler --input '{"image_url": "https://..."}'
```

## Browse All Image Apps

```bash
infsh app list --category image
```
