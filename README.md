# Python Algorithm Lab

Extensive Python and data structures/algorithms learning repository.

This repo has two jobs:

- preserve the original course/practice archive under `ITP/`, `DSA/`, and `revision/`
- provide a clean, tested reference layer under `src/dsa/` for optimized implementations

## Structure

```text
DSA/                 original DSA practice files
ITP/                 introduction-to-python practice files
revision/            merged revision material
src/dsa/             clean reference implementations
tests/               tests for reference implementations
docs/
  learning-roadmap.md
  problem-index.md
```

## Clean Reference Implementations

```bash
pytest
```

Current reference modules:

- `src/dsa/searching.py`
- `src/dsa/sorting.py`
- `src/dsa/stack.py`
- `src/dsa/queue.py`

## Learning Philosophy

For every topic:

1. Understand the brute-force approach.
2. Write the simple implementation.
3. Optimize time and space complexity.
4. Add tests for edge cases.
5. Document the pattern in `docs/problem-index.md`.

## Status

This is the primary home for Python algorithm, DSA, and revision work.

Next upgrade: expand edge-case tests and add time/space complexity notes for each clean implementation in `src/dsa/`.
