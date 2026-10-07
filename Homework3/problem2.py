import sys

def find_substrings_recursive(s, start=0, end=1, unique_set=None):
    """
    使用递归提取字符串 s 的所有连续子串并存入 unique_set。
    """
    if unique_set is None:
        unique_set = set()

    # 1. 递归终止条件：起始索引越界
    if start >= len(s):
        return unique_set

    # 2. 当前起点的所有长度已遍历完，推进到下一个起点
    if end > len(s):
        return find_substrings_recursive(s, start + 1, start + 2, unique_set)

    # 3. 收集当前子串 (s[start:end]) 并递归推进 end
    unique_set.add(s[start:end])
    return find_substrings_recursive(s, start, end + 1, unique_set)


def process_string(s):
    """
    处理单个字符串并按格式输出
    """
    s = s.strip()
    if not s:
        return

    # 1. 递归获取所有不重复子串
    substrings = find_substrings_recursive(s)

    # 2. 按字典序排序
    sorted_substrings = sorted(substrings)

    # 3. 按要求格式输出结果
    for sub in sorted_substrings:
        print(sub)
    print(len(sorted_substrings))


def main():
    # 从标准输入逐行读取数据（兼容重定向管道输入）
    for line in sys.stdin:
        process_string(line)


if __name__ == '__main__':
    main()