---
name: "obsidian-bases"
description: "Create and edit Obsidian Bases (.base files) with views, filters, formulas. Invoke when working with .base files or creating database-like views of notes."
---

# Obsidian Bases Skill

## Schema

Base files use `.base` extension with YAML:

```yaml
filters:
  and: []
  or: []
  not: []

formulas:
  formula_name: 'expression'

properties:
  property_name:
    displayName: "Display Name"

views:
  - type: table | cards | list | map
    name: "View Name"
    order:
      - file.name
      - property_name
```

## Filter Syntax

```yaml
# Single filter
filters: 'status == "done"'

# AND - all conditions must be true
filters:
  and:
    - 'status == "done"'
    - 'priority > 3'

# OR - any condition can be true
filters:
  or:
    - 'file.hasTag("book")'
    - 'file.hasTag("article")'

# NOT - exclude matching items
filters:
  not:
    - 'file.hasTag("archived")'
```

## Key Functions

| Function | Description |
|----------|-------------|
| `date()` | Parse string to date |
| `now()` | Current date and time |
| `today()` | Current date |
| `if()` | Conditional |
| `duration()` | Parse duration string |

## Duration Arithmetic

```yaml
# Calculate days between dates
"(date(due_date) - today()).days"

# Days since created
"(now() - file.ctime).days"
```

## View Types

- `table` - Table view with columns
- `cards` - Card gallery view
- `list` - Simple list view
- `map` - Map view (requires lat/lng properties)

## Default Summaries

`Average`, `Min`, `Max`, `Sum`, `Count`, `Earliest`, `Latest`, `Unique`

## Example: Task Tracker

```yaml
filters:
  and:
    - file.hasTag("task")

formulas:
  days_until_due: 'if(due, (date(due) - today()).days, "")'
  is_overdue: 'if(due, date(due) < today() && status != "done", false)'

views:
  - type: table
    name: "Active Tasks"
    filters:
      and:
        - 'status != "done"'
    order:
      - file.name
      - status
      - due
      - formula.days_until_due
```
