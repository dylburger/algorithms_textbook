#!/usr/bin/env python3

""" Calculate the Greatest Common Divisor of two numbers u and v
"""


def gcd(u, v):
    """ Input: Two integers u and v
        Output: Returns the greatest common divisor of u and v
    """
    # Define a temp variable for swapping, if necessary
    t = 0
    while u != 0:
        # Ensure u is greater than v, else swap
        if u < v:
            t = u
            u = v
            v = t
        u = u % v

    print("GCD: %d" % (v))
    return v

x, y = 267702, 178468
print("x: %d, y: %d" % (x, y))
gcd(x, y)

a, b = 461952, 116298
print("a: %d, b: %d" % (a, b))
gcd(a, b)
