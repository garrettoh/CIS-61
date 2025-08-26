def largest_factor(n):
    """Return the largest factor of n that is smaller than n.
    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1,2,4,5,8,10,16,20,40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    if n % 2 == 0:
        return n // 2
    elif n % 3 == 0:
        return n // 3
    elif n % 5 == 0:
        return n // 5
    elif n % 7 == 0:
        return n // 7
    else:
        return 1
