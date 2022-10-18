# fibonacci
"""
We define the Fibonacci numbers as follows:
F0 = 0
F1 = 1
∀n > 1, Fn = Fn−1 + Fn−2
For this problem, you will code four versions of fib(n), all of which should return the
same answers.
(a) Write fib_recursive(n). It should implement the recursion directly and take
time exponential in n.
(b) Write fib_memoize(n). It should be recursive like fib_recursive(n), but it
should memoize its answers, so that it runs in time O(n).
(c) Write fib_bottom_up(n). Instead of working top-down like in the previous two
examples, start from the bottom, recording your results in a list. This code should
also take O(n) time.
(d) Write fib_in_place(n). It should work bottom-up like the previous example,
but use only O(1) space instead of accumulating answers into a list.
"""

#!/usr/bin/python

def fib_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_recursive(n-1) + fib_recursive(n-2)

dfn = {0:0,1:1}
def fib_memoize(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if not n-1 in dfn:
        dfn[n-1] = fib_memoize(n-2) + fib_memoize(n-3)

    dfn[n] = dfn[n-1] + dfn[n-2]
    return dfn[n]

def fib_bottom_up(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(2,n+1):
        dfn[i] = dfn[i-1] + dfn[i-2]

    return dfn[n]

def fib_in_place(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    no1 = 0
    no2 = 1
    curr = 1
    for i in range(2,n+1):
        curr = no1 + no2
        no1 = no2
        no2 = curr

    return curr
