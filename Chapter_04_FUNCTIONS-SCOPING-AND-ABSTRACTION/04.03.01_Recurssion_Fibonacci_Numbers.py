def fib(n):
    """Assumes n an int >= 0
    returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    else: 
        return fib(n-1) + fib(n-2)
    
def testFib(n):
    for i in range(n+1):
        print('Fibonacci of', i, '=', fib(i))

    
    
