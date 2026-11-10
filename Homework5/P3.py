import os

def compute_longest_alternating_seq(A, B):
    """Computes the maximum length of an alternating increasing sequence using DP."""
    len_A = len(A)
    len_B = len(B)
    dpA = [0] * len_A
    dpB = [0] * len_B

    max_length = 0
    max_idx = max(len_A, len_B)

    # Reverse DP loop to handle dependencies correctly
    for idx in range(max_idx - 1, -1, -1):
        # State transition for Array A
        if idx < len_A:
            max_next = 0
            for j in range(idx + 1, len_B):
                if B[j] > A[idx]:
                    max_next = max(max_next, dpB[j])
            dpA[idx] = 1 + max_next
            max_length = max(max_length, dpA[idx])

        # State transition for Array B
        if idx < len_B:
            max_next = 0
            for i in range(idx + 1, len_A):
                if A[i] > B[idx]:
                    max_next = max(max_next, dpA[i])
            dpB[idx] = 1 + max_next
            max_length = max(max_length, dpB[idx])

    return max_length

def main():
    # Process input files 1 through 6
    for file_num in range(1, 7):
        file_name = f"longest_seq{file_num}.txt"
        
        if os.path.exists(file_name):
            with open(file_name, "r") as f:
                lines = [line.strip() for line in f if line.strip()]
                if len(lines) >= 4:
                    size_A = int(lines[0])
                    size_B = int(lines[1])
                    A = list(map(int, lines[2].split()))
                    B = list(map(int, lines[3].split()))

                    result = compute_longest_alternating_seq(A, B)

                    # Output strict layout required by assignment spec
                    print(f"File Input: {file_name}")
                    print(f"Longest Sequence: {result}")
                    print()
        else:
            print(f"File Input: {file_name} (File not found)")
            print()

if __name__ == "__main__":
    main()