"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""
#!/bin/python

import sys
def gcd(a,b):
    return gcd(b,a%b) if b else a

def lcm(a,b):
    return a/gcd(a,b)*b

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print reduce(lcm, range(1, n + 1))