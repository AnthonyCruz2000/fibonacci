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

