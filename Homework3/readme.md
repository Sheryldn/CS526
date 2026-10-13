# CS526 Homework 3

## output screenshots are in the individual file.

## Introduction
This homework consists of four programming problems: Palindrome, Unique Substrings, Stack Reversing, and Ghostbusters. 

## Algorithm

*   **Problem 1 (Palindrome)**: The program reads all input lines. It strips leading/trailing whitespaces and ignores empty lines, then checks each string against its reversed version to determine if it is a palindrome.
*   **Problem 2 (Unique Substrings)**: The core of this solution relies on recursive functions to traverse and slice the input strings. By passing the state down recursively and utilizing appropriate data structures, the program deduplicates and counts all unique substrings.
*   **Problem 3 (Stack Reversing)**: The program initializes a stack by sequentially pushing the numbers 1 through 10. It utilizes recursion to reverse the order of the elements without the need to allocate a separate stack.
*   **Problem 4 (Ghostbusters)**: This problem utilizes the standard line equation $Ax + By = C$ for geometric collision detection. First, direction vectors $(dx, dy)$ are normalized using the Greatest Common Divisor (GCD) and standardized signs. Next, the constant $C$ is calculated using the starting coordinates ($C = dy \times x - dx \times y$). By comparing these standardized mathematical signatures, the program detects collinearity and overlapping paths.

## Interesting aspects
    *   **Input Sanitization**: When reading files via `<` redirection, trailing empty lines can cause unexpected crashes. I added conditional checks (`if line.strip():`) to safely filter out empty lines.
    *   **Geometric Normalization**: In Problem 4, I handled the standardization of negative direction vectors to prevent the same line from generating different mathematical signatures. I also resolved a critical variable scope issue regarding the calculation of the constant `c` before appending it to our tracking lists.

## How to run

**Problem 1 (Palindrome)**
```bash
python Problem1.py < "Palindrome Resources\palindrome_4.txt"
python Problem1.py < "Palindrome Resources\palindrome_4S.txt"
python Problem1.py < "Palindrome Resources\palindrome_4L.txt"
```

**Problem 2 (Unique Substrings)**
```bash
python problem2.py < unique_substrings_input_0.txt
python problem2.py < unique_substrings_input_1.txt
```

**Problem 3 (Stack Reversing)**
*Run it directly*
```bash
python Problem3.py
```

**Problem 4 (Ghostbusters)**
```bash
python problem4.py < "Ghostbusters Resources\ghostbusters_input_0.txt"
python problem4.py < "Ghostbusters Resources\ghostbusters_input_1.txt"
```
