How to Run the Code

Run the scripts by putting the file to standard input:
   - For Problem 1: `python P1.py < merge_input1.txt`
   - For Problem 2: `python P2.py < heap_input1.txt`
   - For Problem 3: `python P3.py < median_input1.txt`


Problem 1: Solution and Algorithm
I implement a custom ArrayMinHeap that stores tuples in the format of `(time, register_id, index_in_log)`. I initialize the priority queue by pushing the very first sale from each register's log, ensuring the heap never holds more than `k` entries at any time. 
In a loop, I extract the minimum tuple from the heap. Because Python compares tuples element by element, this inherently sorts by time first, and then by register_id for tie-breaking. I append the extracted `(time, register_id)` to my result list. If the log from which this sale originated has more subsequent sales, I push its next sale into the heap. This k-way merge process continues until the heap is empty. The overall time complexity is O(N log k),N is the total number of sales across all registers.

Problem 2: Heap Implementation Approach
To comply with the rule of using a binary tree of linked nodes without arrays or lists, I implement nodes with `value`, `left`, `right`, and `parent` references. To find the correct insertion or extraction spot in O(log n) time, I use a binary path traversal method: I convert the logical position `n` (1-indexed) to binary and drop the leading '1'. The remaining binary digits dictate the path from the root. After insertion, the node sifts up,after extraction, the root sifts down to maintain the heap order and complete shape invariants.

Problem 3: Running Median & Invariants
To simulate a Max-Heap for the smaller half of the numbers, I negate the values before inserting them into `left_heap`. The `right_heap` operates as a standard Min-Heap to store the larger half of the numbers.

To guarantee that the median is always available in O(1) time, the following conditions must stay true after each sale is processed:
1. Size Invariant: `0 <= len(left_heap) - len(right_heap) <= 1`. The `left_heap` can have at most one more element than the `right_heap`. If they become unbalanced, I extract the root from the larger heap and insert it into the smaller heap.
2. Order Invariant: The maximum value in `left_heap` must be less than or equal to the minimum value in `right_heap`.

With these invariants maintained, the median can be retrieved in exactly O(1) time by simply looking at the roots of the heaps:
- If the total number of elements is odd (len(left_heap) > len(right_heap)), the median is the peek of `left_heap`.
- If the total number of elements is even, the median is the average of the peek of `left_heap` and the peek of `right_heap`.