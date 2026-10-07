import sys
import math

def check_ghostbusters():
    # 1. 从标准输入读取所有行
    input_lines = sys.stdin.read().splitlines()
    if not input_lines:
        return

    # 过滤空行
    lines = [line.strip() for line in input_lines if line.strip()]
    if not lines:
        return

    # 读取组数 n
    n = int(lines[0])

    directions = []
    c_constants = []

    for i in range(1, n + 1):
        parts = lines[i].split()
        # 格式为: B <x1> <y1> G <x2> <y2>
        x1, y1 = int(parts[1]), int(parts[2])
        x2, y2 = int(parts[4]), int(parts[5])

        # 计算方向向量
        dx = x2 - x1
        dy = y2 - y1

        # 使用最大公约数 (GCD) 将方向向量化简为最简整数比
        g = math.gcd(abs(dx), abs(dy))
        dx //= g
        dy //= g

        # 规范化方向向量的方向（确保唯一性，便于直接比较相等）
        # 约定 dx > 0，若 dx == 0 则 dy > 0
        if dx < 0 or (dx == 0 and dy < 0):
            dx = -dx
            dy = -dy

        dir_vec = (dx, dy)

        # 直线方程为 -dy * x + dx * y = C
        # 对应标准形式 Ax + By = C，其中 A = -dy, B = dx
        c = -dy * x1 + dx * y1

        directions.append(dir_vec)
        c_constants.append(c)

    # 2. 判断条件:
    # 条件 A: 所有直线的方向向量完全相同 (彼此平行)
    all_same_direction = all(d == directions[0] for d in directions)

    # 条件 B: 所有直线的常数项 C 互不相同 (没有重合)
    all_unique_lines = (len(set(c_constants)) == n)

    # 3. 输出结果
    if all_same_direction and all_unique_lines:
        print("All Ghosts: were eliminated")
    else:
        print("All Ghosts: were not eliminated")


if __name__ == '__main__':
    check_ghostbusters()