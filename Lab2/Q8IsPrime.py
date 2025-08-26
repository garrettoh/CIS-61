def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """

    
    if n < 2:
        return False
    div = 2
    while div * div <= n:
        if n % div == 0:
            return False
        div += 1
    return True
