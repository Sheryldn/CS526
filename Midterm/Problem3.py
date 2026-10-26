import sys
import math

def solve_puzzle():
    
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            lines = f.read().splitlines()
    else:
        lines = sys.stdin.read().splitlines()
        
    if not lines:
        return

    
    n = int(lines[0].strip())
    valid_symbols = set(lines[1].strip().split(','))
    
    
    board = []
    for i in range(2, 2 + n):
        row = lines[i].strip().split(',')
        board.append(row)
        
    sub_size = math.isqrt(n)
    
    
    for i in range(n):
        row_seen = set()
        col_seen = set()
        for j in range(n):
            
            cell_row = board[i][j]
            if cell_row != '.':
                if cell_row not in valid_symbols or cell_row in row_seen:
                    print("The board is invalid")
                    return
                row_seen.add(cell_row)
                
            
            cell_col = board[j][i]
            if cell_col != '.':
                if cell_col not in valid_symbols or cell_col in col_seen:
                    print("The board is invalid")
                    return
                col_seen.add(cell_col)

    
    for box_row in range(0, n, sub_size):
        for box_col in range(0, n, sub_size):
            box_seen = set()
            for r in range(sub_size):
                for c in range(sub_size):
                    cell = board[box_row + r][box_col + c]
                    if cell != '.':
                        if cell in box_seen:
                            print("The board is invalid")
                            return
                        box_seen.add(cell)

    print("The board is valid")

if __name__ == "__main__":
    solve_puzzle()