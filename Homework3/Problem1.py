def process_palindromes(lines):
    total_palindromes = 0

    for line in lines:
        cleaned_str = line.strip().replace(" ", "")
        is_palindrome = cleaned_str == cleaned_str[::-1]

        if is_palindrome:
            total_palindromes += 1

    print(total_palindromes)


# Driver

import sys

if __name__ == '__main__':
    input_data = sys.stdin.read().splitlines()
    lines = [line.strip() for line in input_data if line.strip()]

    if lines:
        process_palindromes(lines)