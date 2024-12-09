def fatorial(n, conta=False):
    msg = str(n)
    for c in range(n-1, 0, -1):
        n *= c
        msg += f" x {c}"
    msg += f" = {n}"
    if conta:
        return msg
    else:
        return n


print(fatorial(5, True))
