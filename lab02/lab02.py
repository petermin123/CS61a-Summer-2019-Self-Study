"""Lab 2: Lambda Expressions and Higher Order Functions"""

# Lambda Functions

# Q1: WWPD: Lambda the Free
"""
>>> lambda x: x            Function

>>> a = lambda x: x        
>>> a(5)                   5

>>> (lambda: 3)()          3

>>> b = lambda x: lambda: x
>>> c = b(88)
>>> c                      Function
>>> c()                    88

>>> d = lambda f: f(4)
>>> def square(x)
        return x * x
>>> d(square)              16


>>> z = 3
>>> e = lambda x: lambda y: lambda: x + y + z
>>> e(0)(1)()              4

>>> f = lambda z: x + z
>>> f(3)                   Error (because x is not defined)


>>> higher_order_lambda = lambda f: lambda x: f(x)
>>> g = lambda x: x * x
>>> higher_order_lambda(2)(g)
                           Error (because you cannot call an integer object, this would be correct if it is '(g)(2)')
>>> higher_order_lambda(g)(2)
                           4

>>> call_thrice = lambda f: lambda x: f(f(f(x)))
>>> call_thrice(lambda y: y + 1)(0)
                           3 (0 + 1, 1 + 1, 2 + 1)

>>> print_lambda = lambda z: print(z)
>>> print_lambda           Function
>>> one_thousand = print_lambda(1000)
                           1000
>>> one_thousand           Nothing
"""

# Q2: WWPD: Higher Order Functions
"""
>>> def even(f):
...     def odd(x):
...         if x < 0:
...             return f(-x)
...         return f(x)
...     return odd
stewart                    Function
stewart(61)                61
stewart(-4)                4

>>> def cake():
...    print('beets')
...    def pie():
...        print('sweets')
...        return 'cake'
...    return pie
chocolate = cake()                                beets                               
chocolate                                         function
chocolate()                                       sweets, 'cake'
more_chocolate, more_cake = chocolate(), cake     sweets
more_chocolate                                    'cake'

>>> def snake(x,y):
...     if cake == more_cake:
...             return lambda: x + y
...     else:
...             return x + y
...
>>> snake(10, 20)          Function
>>> snake(10, 20)()        30 (lambda: x + y)
>>> cake = 'cake'
>>> snake(10, 20)          30 (x + y because cake != more_cake now)
"""

# Q3: Lambdas and Currying
def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    """
    "*** YOUR CODE HERE ***"
    return lambda x: lambda y: func(x, y)


# Q5: Lambda the Environment Diagram
"""
>>> a = lambda x: x * 2 + 1
>>> def b(b, x):
...     return b(x + a(x))
>>> x = 3
>>> b(a, x)

Will give 21 because the function can be simplified to 'a(3 + a(3))'
"""