def ways(n):
    # Base Cases
    if n < 0:
        return 0
    if n == 0:
        return 1

    
    return ways(n - 1) + ways(n - 2) + ways(n - 3)


if __name__ == "__main__":
    print(f"ways(3) = {ways(3)}")
    print(f"ways(5) = {ways(5)}")
    print(f"ways(10) = {ways(10)}")