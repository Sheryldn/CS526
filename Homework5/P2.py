import os

# Morse code dictionary mapping for Vowels
VOWEL_MAP = {
    'A': '.-',
    'E': '.',
    'I': '..',
    'O': '---',
    'U': '..-'
}

def count_vowel_combinations(sequence: str) -> int:
    """Computes the total number of valid vowel sequences using Dynamic Programming."""
    n = len(sequence)
    dp = [0] * (n + 1)
    dp[n] = 1  # Base case: empty sequence

    for i in range(n - 1, -1, -1):
        ways = 0
        for code in VOWEL_MAP.values():
            code_len = len(code)
            if i + code_len <= n and sequence[i:i + code_len] == code:
                ways += dp[i + code_len]
        dp[i] = ways

    return dp[0]

def main():
    # Process files 1 through 4 automatically
    for file_num in range(1, 5):
        file_name = f"vowel_input{file_num}.txt"
        
        if os.path.exists(file_name):
            with open(file_name, "r") as f:
                sequence = f.read().strip()
                total_ways = count_vowel_combinations(sequence)
                
                # Output formatted strictly as required by the specification
                print(f"File Input: {file_name}")
                print("The Number of Vowel combinations is:")
                print(total_ways)
                print()  # Empty line for separation
        else:
            print(f"File Input: {file_name} (File not found)")
            print()

if __name__ == "__main__":
    main()