
def even_or_odd(n):
    """
        returns true if the number is even and returns false if the number is odd
    >>> even_or_odd(4)
    True
    >>> even_or_odd(1337)
    False
    >>> even_or_odd(0)
    True
    >>> even_or_odd(11)
    False
    """
    return n % 2 == 0
