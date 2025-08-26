def fibonacci(n):
  
    """Return the nth Fibonacci number.
    Fibonacci Numbers is a series of numbers in which each number is 
    the sum of the two preceding numbers
    >>> fibonacci(5) # 1, 1, 2, 3, 5
    5
    >>> fibonacci(7) 
    13
    """

    
    a, b = 0, 1
    count = 0
    while count < n:
        a, b = b, a + b
        count += 1
    return a

