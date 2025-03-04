# def mydeco(funk):
#     def wrapper(*args, **kwargs):
#         a = funk(*args, **kwargs)
#         return a *2
#     return wrapper
# @mydeco
# def two(a, b):
#     return a + b

# print(two(1, 3))


# def foktor(n):
#     if n == 1:
#         return 1
#     else:
#         return n * foktor(n-1)
    
# print(foktor(5))

# def raq(n):
#     if n == 1:
#         return 1
    
#     else:
#         return n + raq(n-1)
    
# print(raq(10))


# def revers(m):
#     if len(m) == 0:
#         return m
#     else:
#         return m[-1] + revers(m[:-1])
    
# print(revers('fazliddin'))

son = 123 
summa = 0
while son != 0:
    summa = summa + son % 10  # oxirgi raqamni olish
    son = son // 10  # sonni 10 ga bo'lib, oxirgi raqamni olib tashlash

print(summa)


    
        

    