---
name: skill-creator
description: Create new skills, modify and improve existing skills, and measure skill performance. Invoke when user wants to create a skill from scratch, edit, optimize an existing skill, or run evals to test a skill.
---

# Skill Creator

A skill for creating new skills and iteratively improving them.

## Creating a Skill: Overview

1. Decide what the skill should do
2. Write a draft of the skill
3. Create test prompts and run them
4. Evaluate results (qualitatively and quantitatively)
5. Rewrite based on feedback
6. Repeat until satisfied

## Creating a Skill

### Step 1: Capture Intent

Understand from conversation or ask:
1. What should this skill enable Claude to do?
2. When should this skill trigger?
3. What's the expected output format?
4. Should we set up test cases?

### Step 2: Interview and Research

Ask about edge cases, input/output formats, example files, success criteria, and dependencies.

### Step 3: Write the SKILL.md

```markdown
---
name: "skill-name"
description: "What it does AND when to trigger. Be specific about contexts."
---

# Skill Title

[Detailed instructions, examples, workflows]
```

## Skill Structure

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description required)
│   └── Markdown instructions
└── Bundled Resources (optional)
    ├── scripts/    - Executable code
    ├── references/ - Documentation
    └── assets/     - Templates, icons, fonts
```

## Progressive Disclosure

Skills use a three-level loading system:
1. **Metadata** (name + description) - Always in context (~100 words)
2. **SKILL.md body** - In context when skill triggers (<500 lines ideal)
3. **Bundled resources** - As needed (unlimited)

## Writing Guidelines

- Keep SKILL.md under 500 lines
- Use imperative form in instructions
- Include clear examples
- Explain WHY things are important
- Avoid heavy-handed MUSTs; use reasoning instead

## Test Cases

After writing the skill draft, create 2-3 realistic test prompts:

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "User's task prompt",
      "expected_output": "Description of expected result"
    }
  ]
}
```

## Improving the Skill

1. **Generalize from feedback** — Don't overfit to specific examples
2. **Keep the prompt lean** — Remove things that aren't pulling their weight
3. **Explain the why** — Help the model understand reasoning
4. **Look for repeated work** — If test cases all write similar scripts, bundle them

## Principle of Lack of Surprise

Skills must not contain malware, exploit code, or content that could compromise system security. A skill's contents should not surprise the user in their intent if described.
