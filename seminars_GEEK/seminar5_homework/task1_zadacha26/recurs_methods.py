def power(a, b) -> int:
    print(f"get{a} and{b}")
    if b == 0:
        return 1
    return a * power(a, b-1)  