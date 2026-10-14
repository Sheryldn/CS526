import sys
import math

def count_right_triangles(input_file):
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
        
    n = int(lines[0])
    points = []
    for line in lines[1:n + 1]:
        parts = line.split()
        if len(parts) >= 2:
            points.append((int(parts[0]), int(parts[1])))
            
    total_right_triangles = 0
    
    
    for i in range(n):
        px, py = points[i]
        dir_count = {}
        
        for j in range(n):
            if i == j:
                continue
            qx, qy = points[j]
            dx = qx - px
            dy = qy - py
            
            
            g = math.gcd(abs(dx), abs(dy))
            dx_red = dx // g
            dy_red = dy // g
            
            d_tuple = (dx_red, dy_red)
            dir_count[d_tuple] = dir_count.get(d_tuple, 0) + 1
            
        
        p_triangles = 0
        for (dx_r, dy_r), count in dir_count.items():
            perp1 = (-dy_r, dx_r)
            perp2 = (dy_r, -dx_r)
            
            p_triangles += count * dir_count.get(perp1, 0)
            p_triangles += count * dir_count.get(perp2, 0)
            
        
        total_right_triangles += p_triangles // 2

    print(f"The number of right triangles is: {total_right_triangles}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        count_right_triangles(sys.argv[1])