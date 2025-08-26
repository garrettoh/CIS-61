def hailstone(n):
    """Print the hailstone sequence starting at n and return its length.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    steps = 1
    while n != 1:
        print(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    print(1)
    return steps
