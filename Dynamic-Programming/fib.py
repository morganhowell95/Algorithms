#1, 1, 2, 3, 5, 8, 13, 21, 34, ...


#Naive implementation of Fibonacci O(2n) space and time
def naive_fib(n):
    if n<2: f=1
    else: f = naive_fib(n-1) + naive_fib(n-2)
    return f

#print naive_fib(10)

#Fibonacci with memoization O(n) space O(n) time
memo = {}
def memo_fib(n):
    if n in memo: return memo[n]
    elif n<2: f=1
    else: f = memo_fib(n-1) + memo_fib(n-2)
    memo[n]=f
    return f

#print memo_fib(100)

#Fibonacci with bottom-up approach O(n) space O(n) time
cmap = {}
def bottom_fib(n):
    for i in range(1,n+1):
        if i in cmap: return cmap[i]
        elif i<2: f = 1
        else: f = cmap[i-1] + cmap[i-2]
        cmap[i]=f
    return cmap[n]

#print memo_fib(100)


