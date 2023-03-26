def summ(a, b) -> int:
    if a == 1 and b == 0:
        return 1
    elif a == 0: return b
    elif b == 0:
        return 1 + summ(a - 1, b)
    return 1 + summ(a, b - 1)
