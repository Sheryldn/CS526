import sys

def solve_snowfall():

    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            data = f.read().split()
    else:
        data = sys.stdin.read().split()
        
    if not data:
        return


    n = int(data[0])
    A = [int(x) for x in data[1:n+1]]
    
    input_str = " ".join(map(str, A))
    
    if n < 3:
        print(f"{input_str} solution: NO")
        return
        
    total_snowfall = A[-1]
    
    
    for i in range(n - 2):
        
        if i == 0:
            window_sum = A[2]
        else:
            window_sum = A[i + 2] - A[i - 1]
            
        
        if window_sum * 2 > total_snowfall:
            print(f"{input_str} solution: YES")
            return
            
    print(f"{input_str} solution: NO")

if __name__ == "__main__":
    solve_snowfall()