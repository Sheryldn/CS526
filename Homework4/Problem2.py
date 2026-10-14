import sys

def smallest_number_of_elements(input_file):
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    n = int(lines[0])
    target = int(lines[1])
    arr = list(map(int, lines[2].split()))
    
    
    sorted_arr = sorted(arr, reverse=True)
    
    current_sum = 0
    count = 0
    
    for num in sorted_arr:
        current_sum += num
        count += 1
        if current_sum > target:
            break
            
    
    arr_str = ",".join(map(str, arr))
    print(f"Input: {arr_str} Target: {target} Answer: {count}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        smallest_number_of_elements(sys.argv[1])