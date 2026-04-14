---
name: "obsidian-cli"
description: "Interact with Obsidian vaults via CLI to read, create, search notes. Invoke when user asks to interact with vault, manage notes, or perform vault operations from command line."
---

# Obsidian CLI

Use `obsidian` CLI to interact with a running Obsidian instance. Requires Obsidian to be open.

## Syntax

**Parameters** use `=`. Quote values with spaces:

```bash
obsidian create name="My Note" content="Hello world"
```

**Flags** are boolean switches with no value:

```bash
obsidian create name="My Note" silent overwrite
```

## File Targeting

- `file=<name>` — resolves like a wikilink
- `path=<path>` — exact path from vault root

## Vault Targeting

```bash
obsidian vault="My Vault" search query="test"
```

## Common Commands

```bash
# Read a note
obsidian read file="My Note"

# Create a note
obsidian create name="New Note" content="# Hello" template="Template" silent

# Append to a note
obsidian append file="My Note" content="New line"

# Search
obsidian search query="search term" limit=10

# Daily notes
obsidian daily:read
obsidian daily:append content="- [ ] New task"

# Properties
obsidian property:set name="status" value="done" file="My Note"

# Tasks
obsidian tasks daily todo

# Tags
obsidian tags sort=count counts

# Backlinks
obsidian backlinks file="My Note"
```

## Plugin Development

```bash
# Reload plugin after code changes
obsidian plugin:reload id=my-plugin

# Check for errors
obsidian dev:errors

# Take screenshot
obsidian dev:screenshot path=screenshot.png

# Inspect DOM
obsidian dev:dom selector=".workspace-leaf" text

# Run JavaScript
obsidian eval code="app.vault.getFiles().length"
```

## Useful Flags

- `--copy` — copy output to clipboard
- `silent` — prevent files from opening
- `total` — get count on list commands
