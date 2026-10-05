## Introduction
### This repository contains the solution for CS526 Homework 2, covering singly linked lists with tail pointers, pure recursive algorithms, and sorted doubly linked lists.

## Algorithm

### Problem 1: Tail Pointer Advantage
- Using a tail pointer reduces the time complexity of append operations from $O(n)$ to $O(1)$, because we can directly link the new node without traversing the entire list.

### Problem 2: Singly Linked List (`SinglyLinkedList`)
- Maintained both `head` and `tail` references along with a `count` integer.
- Boundary checks handle head/tail updates carefully during `append`, `prepend`, and `delete`.

### Problem 3: Climbing Stairs (`ways(n)`)
- State transition equation: `ways(n) = ways(n-1) + ways(n-2) + ways(n-3)`.
- Base cases: `ways(0) = 1` (valid path reached) and `ways(n < 0) = 0` (invalid path).

### Problem 4: Sorted Doubly Linked List (`SortedDoublyLinkedList`)
- **Insertion (`add`):** Always maintains ascending order by comparing incoming values sequentially.
- **Recursive Methods:** Used recursion for `total`, `exists`, `count`, and `print_list`. Early termination is applied when current node value exceeds target.


## Interesting Aspects
- **Design Trade-offs:** Renamed the count attribute in Problem 4 to `self.size` to prevent conflict with the required `count(value)` method.
- **Early Termination:** Leveraging list order to halt recursive search early in `exists` and `count` significantly improves performance for non-existent or out-of-range queries.

## How to run
-## How to Run

Run the following commands in your terminal:

-problem 2:
  python3 problem2_driver.py < test.txt
-problem 3:
  python3 problem3.py
-problem 4:
  python3 problem4_driver.py
