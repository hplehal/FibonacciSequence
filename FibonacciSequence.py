from math import sqrt
#fibonacci sequence using the recursion O(2^n) thats alot let try something else

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
#fibonaci sequence using the sqrt formula
#def fibSec():
def fibSqrt(n):
    return ((1+sqrt(5))**n - (1-sqrt(5))**n )/ (2**n*sqrt(5))

#using generator and goes in sequence
def fibGen(n):
    a,b = 0, 1
    for _ in range(n+1):
        yield a
        a , b = b , a+b
for i in fibGen(2):
    print(i)


#using a specific starting point and end point

def fibPoints(start, end):
    for num in fibGen(end):
        if num > end : return
        if num >= start:
            yield num

for i in fibPoints(0, 150):
    print(i)
            


