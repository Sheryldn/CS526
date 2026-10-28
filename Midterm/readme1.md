# Heart of the algorithm:

## The algorithm uses the provided cumulative array to calculate the snowfall of any 3-day window in $O(1)$ time. For any starting day index i (0-indexed), the 3-day total is computed as A[i+2] if i == 0, or A[i+2] - A[i-1] for subsequent days. It iterates through all possible 3-day windows (from i = 0 to n - 3). If it finds a window where the sum multiplied by 2 is strictly greater than the final cumulative value A[n-1] (the total snowfall), it returns YES. If the loop completes without finding such a window, or if $n < 3$, it returns NO. The overall time complexity is $O(n)$.   


# To run using standard input redirect:
## python Problem1.py < snowfall_input1.txt

# To run using a file name passed via command line:
## python Problem1.py snowfall_input1.txt