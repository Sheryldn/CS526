import sys
import math

def check_ghostbusters():
    
    input_lines = sys.stdin.read().splitlines()
    if not input_lines:
        return

    
    lines = [line.strip() for line in input_lines if line.strip()]
    if not lines:
        return

    n = int(lines[0])

    directions = []
    c_constants = []

    for i in range(1, n + 1):
        parts = lines[i].split()
        
        x1, y1 = int(parts[1]), int(parts[2])
        x2, y2 = int(parts[4]), int(parts[5])

        
        dx = x2 - x1
        dy = y2 - y1

        
        g = math.gcd(abs(dx), abs(dy))
        dx //= g
        dy //= g

        if dx < 0 or (dx == 0 and dy < 0):
            dx = -dx
            dy = -dy

        dir_vec = (dx, dy)

        

        directions.append(dir_vec)
        c_constants.append(c)

    all_same_direction = all(d == directions[0] for d in directions)

    all_unique_lines = (len(set(c_constants)) == n)

    if all_same_direction and all_unique_lines:
        print("All Ghosts: were eliminated")
    else:
        print("All Ghosts: were not eliminated")


if __name__ == '__main__':
    check_ghostbusters()