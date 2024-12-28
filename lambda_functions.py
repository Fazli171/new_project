from functools import reduce
'''1  Factorial (Faktorial)'''                              
# def myfoc(son: int) -> int :
#     if son == 0 :
#         return 1
#     else:
#         return son * myfoc(son - 1)
# print(myfoc(5))

'''2  Power (Daraja)
Bir sonni berilgan darajaga ko‘tarish.'''

# def myPower(a: int, b : int) -> int:
#     if b == 0:
#         return 1
#     else:
#         return a * myPower(a, b - 1)
# print(myPower(2,3))

'''3  Listning elementlarining yig‘indisini hisoblash
Calculating the sum of the elements of a list'''

lis = [2, 3, 6, 8, 9, 5, 3]

# def mysum(lis: list) -> int:
#     if len(lis) == 0 :
#         return 0
#     else:
#         return lis[0] + mysum(lis[1:])
# print(mysum(lis))

'''4  Reversing a String (Matnni teskari qilish)'''

# text = "Fazliddin"

# def myReversing(text: str) -> str:

#     if len(text) == 0:
#         return ''
#     else :
#         return text[-1] + myReversing(text[:-1])
    
# print(myReversing(text))

'''5 Max Elementni Topish
Finding the Max Element'''

# lis1 = [2, 3, 6, 8, 9, 5, 3]

# def myMax(lis: list) -> int:

#     if len(lis) == 1:
#         return lis[0]
#     else:
#         max_v = myMax(lis[1:])
#         return  lis[0] if lis[0] > max_v else max_v
# print(myMax(lis1))



# cry = int(input('count your number'))
numbers = [-1, -2, -5, -6, 1, 3, 5, 7, 4, 9, 6]
numbers1 = [2, 3, 5, 7, 8]
number = 10
x = 'fazli'
x1 = 'Fazliddin'

n1 = 10
n2 = 20
# text = input("type text")
words = ["apple", "banana", "cherry", "orange", "grape", "lemon", "peach", "melon", "pear", "plum"]


'''6 Lambda funksiyasidan foydalanib, berilgan sonni 10 ga ko‘paytiring.
1 Multiply a given number by 10 using a lambda function'''
# for i in range(10):
#     funk = lambda i: i * 10
#     print(funk(i))
# print(list(map(lambda i : i * 10 , numbers)))
# result =( lambda i : i * 10 )( number)
# print(result)

'''7 Lambda funksiyasi yordamida sonning kubini hisoblang.
2 Calculate the cube of a number using the lambda function'''

# result = list(map(lambda i : i ** 3 , numbers))
# print(result)

# result1 = list(map(lambda i : i ** 3 , [i for i in range(cry)]))
# print(result1)

# result2 = (lambda i : i ** 3)(number) 
# print(result2)

'''8 Lambda funksiyasi bilan sonning manfiy yoki musbatligini aniqlang.
 3 Determine whether a number is negative or positive with the lambda function.'''

# result = list(map(lambda i : f"{i} negative number " if i < 0 else f"{i} positive number ", numbers))
# print(result)

# result1 = list(map(lambda i: f"{i} > negative number" if i < 0 else f"{i} > positive number",[i for i in range(cry)]))
# print(result1)

# result2 = (lambda i : f"pasitive number" if i > 0 else "negative number")(number)
# print(result2)

'''9 Berilgan so‘zning oxirgi harfini qaytaruvchi lambda funksiyasini yozing
4 Write a lambda function that returns the last letter of a given word.'''

# result = (lambda i : i[-1] )(text)
# print(result)

# result1 = list(map(lambda i: i[-1], words))
# print(result1)

# result2 = list(map(lambda i: i[-1], [i for i in words]))
# print(result2)

'''10 Lambda yordamida ikkita so‘zning uzunligini taqqoslang
 5 Compare the length of two words using lambda'''

# result = (lambda x , x1 : f"{x} is longer" if len(x) > len(x1) else f"{x1} is longer "  f"{x1} is longer" if len(x) < len(x1) else "both are equal in length")(x1, x)
# print(result)

'''11 Lambda funksiyasi yordamida sonning faktorialini hisoblang (rekursiyasiz)
   6 Calculate the factorial of a number using a lambda function (without recursion)'''

# factorial = (lambda n: (lambda x: reduce(lambda x, y: x * y, x))(list(range(1, n + 1))))(number)
# print(factorial)

'''12 Lambda funksiyasi bilan ikkita sonni bo‘ling
   7 Divide two numbers with the lambda function'''
