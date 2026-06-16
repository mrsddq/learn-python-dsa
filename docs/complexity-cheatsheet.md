# Complexity Cheatsheet

This repo is a learning archive plus a small tested reference module under `src/dsa`.

| Operation | Implementation | Time | Space | Edge cases covered |
| --- | --- | --- | --- | --- |
| Linear search | `src.dsa.searching.linear_search` | O(n) | O(1) | Empty list, missing value, duplicates |
| Binary search | `src.dsa.searching.binary_search` | O(log n) | O(1) | Empty sorted list, negative values, missing value |
| Merge sort | `src.dsa.sorting.merge_sort` | O(n log n) | O(n) | Empty list, duplicates, does not mutate input |
| Stack push/pop/peek | `src.dsa.stack.Stack` | O(1) | O(n) | Empty pop/peek raises `IndexError` |
| Queue enqueue/dequeue | `src.dsa.queue.Queue` | O(1) | O(n) | Empty dequeue raises `IndexError` |

Interview practice note: explain the invariant before coding. For binary search, the invariant is that the target, if present, remains inside `[left, right]` after each comparison.
