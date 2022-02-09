"""Optional questions for Lab 1"""

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    result = 1
    while k > 0:
        result = n * result
        k -= 1
        n -= 1
    return result

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    marker = 0
    while n != 0:
        d = n % 10
        n = n // 10
        # This makes sure we are only comparing each round w/ previous round, aka two eights in a row
        if d == 8 and marker == 1:
            return True
        # Set marker to 1 if this round has a remainder of 8
        elif d == 8:
            marker = 1
        else:
            marker = 0
    return False