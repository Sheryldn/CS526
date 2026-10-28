# Heart of the algorithm :

## The algorithm validates the puzzle board by iterating through the grid and using HashSets to track the occurrence of symbols. First, it stores the allowed symbols in a set to perform $O(1)$ constant-time checks for illegal characters. It uses separate HashSets to detect duplicates within each row and each column. Finally, it iterates through each $\sqrt{n} \times \sqrt{n}$ sub-board by incrementing the row and column indices by $\sqrt{n}$, using another HashSet to guarantee that no symbol appears more than once in any sub-board. If any check fails, it immediately terminates and prints "The board is invalid". If all checks pass, it prints "The board is valid".   


## To run using standard input redirect:
## python Problem3.py < puzzle_game_input1.txt

# To run using a file name passed via command line:
## python Problem3.py puzzle_game_input1.txt   