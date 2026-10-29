# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""


def classifyTriangle(a, b, c):
    # Check that all inputs are integers
    if not all(isinstance(side, int) and not isinstance(side, bool)
               for side in (a, b, c)):
        return 'InvalidInput'

    # Check valid side length range
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    # Check triangle inequality
    if a + b <= c or a + c <= b or b + c <= a:
        return 'NotATriangle'

    # Check equilateral
    if a == b == c:
        return 'Equilateral'

    # Check right triangle (Pythagorean theorem)
    sides = sorted([a, b, c])
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        return 'Right'

    # Check isosceles
    if a == b or b == c or a == c:
        return 'Isoceles'

    return 'Scalene'

