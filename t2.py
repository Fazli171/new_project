import math

'''FIBONACHI'''
# Recursive method
das_fib = 10

def MyFib(son: int) -> int:
    if son <= 1 :
        return son
    else:
        return MyFib(son-1) + MyFib(son - 2)
    
print(MyFib(das_fib))

def myFib(son: int) -> int:
    F0 , F1 = 0, 1
    n = 1
    while n < son:
        F0 , F1 =F1, F0 + F1
        n += 1
    return F1
print(myFib(10))


n = 10
fib = lambda n : 0 if n == 0 else 1 if n == 1 else (fib(n -1 ) + fib(n-2))

print(fib(n))

def myFIB(son: int) -> int:
    f0 , f1 = 0 , 1
    for _ in range(n):
        f0, f1 = f1, f1 + f0
    return f0
print(myFIB(10))

def fib_memon(n, memo={0: 0, 1: 1}):
    if n not in memo:
        memo[n] = fib_memon(n - 1, memo) + fib_memon(n - 2, memo)
    return memo[n]

print(fib_memon(10))

def fibonacci_binet(n):
    phi = (1 + math.sqrt(5)) / 2
    return round((phi**n - (-phi)**(-n)) / math.sqrt(5))

print(fibonacci_binet(10))

def fibonacci_generator(n):
    F0, F1 = 0, 1
    for _ in range(n):
        yield F0
        F0, F1 = F1, F0 + F1

fib_gen = fibonacci_generator(10)
for fib in fib_gen:
    print(fib, end=" ")


def fibonacci_up_to_n(n):
    F0, F1 = 0, 1
    fib_sequence = [F0]
    for _ in range(1, n):
        F0, F1 = F1, F0 + F1
        fib_sequence.append(F0)
    return fib_sequence


print(fibonacci_up_to_n(10)) 



