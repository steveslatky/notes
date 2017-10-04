---
title: book -cs303
author: Stephen Slatky
geometry: margin=1in
numbersections: true
---
# Chapter 5.1 Elliptic Curves and Cryptography

## What is it

An elliptic curve is the set of solutions to an equation of the form
                    Y 2 = X3 + AX + B.

There is a natural way to take two points on an elliptic curve and 
“add” them to produce a third point.

## Addition Law

We start by drawing the line L through P and Q. This line L intersects
E at three points, namely P, Q, and one other point R. We take
that point R and reflect it across the x-axis (i.e., we multiply its Y-coordinate
by −1) to get a new point R
. The point R is called the “sum of P and Q,”


P (+) Q = R

* (+) should look like the XOR sign but is not.

### Example 

Take the equation 

Y 2 = X3 − 15X + 18.

The points P = (7, 16) and Q = (1, 2) are on the curve E. The line L connecting
them is given by the equation4

L : Y = 7/3X - 1/3

Recall that the equation of the line through two points (x1, y1) and (x2, y2) is given by
the point–slope formula Y − y1 = λ · (X − x1), where the slope λ is equal to y2−y1
x2−x1 .

Subsitute to find where they intersect.


0 = X^3 − 49/9X^2 - 121/9X + 161/9

We need to find the roots of this cubic polynomial

we already know two of the
roots, namely X = 7 and X = 1, since we know that P and Q are in the
intersection E ∩ L. It is then easy to find the other factor,

X^3 − 49/9x^2 + 121/9x + 161/9 = (x-7) * (x-1) * (X + 23/9) 




