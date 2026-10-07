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

# Example usage:
# process_palindromes('input.txt')