from operator import add, sub

def both_positive(x, y):
   
    """Returns True if both x and y are positive.
    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    
    return x > 0 and y > 0 # You can replace this line!



def a_plus_abs_b(a, b):
  
    """Return a+abs(b), but without calling abs.
    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """

    if b < 0:
        f = sub
    else:
        f = add

    return f(a, b)



def two_of_three(a, b, c):
  
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.
    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    
    return a*a + b*b + c*c - min(a,b,c)**2





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



def sum_digits(n):
   
    """Sum all the digits of n.
    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> x = sum_digits(123) # make sure that you are using return rather than print
    >>> x
    6
    """

    
    if n < 10:
        return n
    return (n % 10) + sum_digits(n // 10)




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
