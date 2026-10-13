import sys

def find_substrings_recursive(s, start=0, end=1, unique_set=None):
    
    if unique_set is None:
        unique_set = set()

    
    if start >= len(s):
        return unique_set

     
    if end > len(s):
        return find_substrings_recursive(s, start + 1, start + 2, unique_set)

    
    unique_set.add(s[start:end])
    return find_substrings_recursive(s, start, end + 1, unique_set)


def process_string(s):
    
    s = s.strip()
    if not s:
        return

    
    substrings = find_substrings_recursive(s)

    
    sorted_substrings = sorted(substrings)

    for sub in sorted_substrings:
        print(sub)
    print(len(sorted_substrings))


def main():
    for line in sys.stdin:
        process_string(line)


if __name__ == '__main__':
    main()