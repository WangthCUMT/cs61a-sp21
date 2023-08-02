def multiply(m, n):
    """ Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return m
    else:
        return m + multiply(m,n-1)

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return n * skip_mul(n - 2)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(i):
        if i > (n ** 0.5):
            return True
        elif n % i == 0:
            return False
        return helper(i+1)
    return helper(2)  # make a inital call of helper()

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
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
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(n*3 + 1)

def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    "*** YOUR CODE HERE ***"
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 < n2 % 10:
        return merge(n1 // 10, n2)*10 + n1 % 10
    else:
        return merge(n1, n2 // 10)*10+ n2 % 10

def num_digits(n):
    '''
    >>> num_digits(0)
    1
    >>> num_digits(123)
    3
    '''
    if n < 10:
        return 1
    else:
        return num_digits(n // 10) + 1

def interleave(a,b):
    """
    >>> interleave(1,0)
    10
    >>> interleave(0,1)
    1
    >>> interleave(123,456)
    142536
    >>> interleave(1234,5678)
    15263748
    """
    assert num_digits(a) == num_digits(b)
    if a < 10:
        return a*10 + b
    else:
        return interleave(a // 10, b // 10) * 100 + a%10*10 + b%10

