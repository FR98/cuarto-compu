def prob_14(n):
    if n < 1:
        return False
    if n == 1:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True