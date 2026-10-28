# Heart of the algorithm:

## The algorithm uses a Breadth-First Search-like simulation to model the simultaneous daily spread of the infection. It stores the coordinates of all currently infected counties in a HashSet for $O(1)$ lookup time. During each "day", it iterates through all grid cells. For every healthy county, it checks its 4 immediate neighbors. If at least 2 neighbors are present in the currently infected set, this county is added to a temporary new_infected set. This temporary set ensures the updates are simultaneous, so counties infected today cannot infect others until the next day. The loop breaks when new_infected is empty . Finally, it compares the total number of infected counties to $N \times N$ to determine if any healthy counties remain.  

# To run using standard input redirect:
## python pandemic.py < pandemic_input1.txt

# To run using a file name passed via command line:
## python pandemic.py pandemic_input1.txt