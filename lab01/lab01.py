"""Lab 1: Expressions and Control Structures"""

# Question 1 WWPD Control:
"""
xk:
    xk(10, 10) will display 23
    xk(10, 6) will display 23 
    xk(4, 6) will display 6    
    xk(0, 0) will display 25

how_big:
    how_big(7) will display 'big'
    how_big(12) will display huge (w/o the single quotation marks)
    how_big(1) will display small
    how_big(-1) will display nothin'

1st while loop:
    line 1: 2
    line 2: 1
    line 3: 0
    line 4: -1 (-1 will be displayed as the 4th line b/c it happens when n = 0 and the decrement makes n equal to -1)

2nd while loop:
    Infinite Loop (the loop will always evaluate to while True so it never ends)

3rd while loop:
    line 1: -12 (both while -12 and if -9 evaluate to True)
    line 2: -9
    line 3: -6 (negative = 0, the loop breaks)
"""


# Question 2 WWPD Veritasiness
"""
True and 13:
    13
False or 0:
    0
not 10:
    False
not None:
    True
True and 1 / 0 and False:
    Error
True or 1 / 0 or False:
    True
True and 0:
    0
False or 1:
    1
1 and 3 and 6 and 10 and 15:
    15
0 or False or 2 or 1 / 0:
    2 (2 is one True that is enough to determine the result)
not 0:
    True
(1 + 1) and 1:
    1
1/0 or True:
    Error
(True or False) and False:
    False (True or False is not false, therefore it returns False)
"""


# Question 3: Fix the Bug
def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return x > 0 and y > 0 # You can replace this line!


# Question 4: Sum Digits
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
    result = 0
    while n != 0:
        mod = n % 10
        result += mod
        n = n // 10
    return result


# Question 5 WWPD: What If?
"""
ab(10, 20):
    line 1: 10
    line 2: foo

bake(0, 29):
    line 1: 1
    line 2: 29
    line 3: 29 (this is the 29 that is returned)

bake(1, "mashed potatoes"):
    line 1: mashed potatoes
    line 2: 'mashed potatoes' (this is the 'make' that is returned)
"""