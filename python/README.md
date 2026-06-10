# Gilded Rose — Python solution

Refactoring kata solution. Original requirements: [GildedRoseRequirements.md](../GildedRoseRequirements.md).

## Getting started

Requires Python 3.10+ and [Poetry](https://python-poetry.org/).

```
make install     # install dependencies
make test        # run the test suite
make lint        # ruff check + format check
make typecheck   # mypy
make check       # lint + typecheck + test
```

## Approach

1. **Safety net first.** Approved the 30-day golden master (ApprovalTests) and wrote
   characterization tests for every business rule and boundary value, before touching
   any code.
2. **Incremental refactoring.** Replaced the nested conditionals with one updater per
   item category, selected by name; quality bounds (0–50) centralized in two helpers.
   The golden master guarantees behavior is preserved.
3. **Conjured items (TDD).** Failing tests first, then a four-line updater: a normal
   item with a doubled degradation rate. The golden master was re-approved — only the
   `Conjured Mana Cake` lines changed, as intended.

## Design notes

- `Item` is untouched, as required by the specification.
- Conjured items are matched by name prefix, other special items by exact name.
- Poetry replaces `requirements.txt` for locked, reproducible installs; ruff and mypy
  keep the code consistent.
- Single module on purpose: one responsibility, ~80 lines. The first natural split,
  if more item types appeared, would be a dedicated updaters module.

## Time spent

Approximately 2 hours, including test design, refactoring and tooling setup.
