# fibonacci
#.
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
