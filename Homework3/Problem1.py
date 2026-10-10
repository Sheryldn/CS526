def process_palindromes(filename):
    total_palindromes = 0
    
    with open(filename, 'r') as f:
        for line in f:
            
            cleaned_str = line.strip().replace(" ", "")
            
            
            is_palindrome = cleaned_str == cleaned_str[::-1]
            
            
            print(is_palindrome)
            
            if is_palindrome:
                total_palindromes += 1
                
    
    print(total_palindromes)



# Driver

import sys
import os


if __name__ == '__main__':
    # Use the filename from command-line arguments if provided; default to 'input.txt'
    if len(sys.argv) > 1:
        test_file = sys.argv[1]
    else:
        test_file = 'input.txt'

    if os.path.exists(test_file):
        process_palindromes(test_file)
    else:
        print(f"Error: Test file not found: {test_file}")