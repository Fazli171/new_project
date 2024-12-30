import math

# Determine whether the sum of the squares of two numbers is greater than the square of their sum
a = float(input('Enter a: '))
b = float(input('Enter b: '))
if (a**2 + b**2) > (a + b)**2:
    print('The sum of squares of a and b is greater.')
else:
    print('The square of the sum of a and b is greater.')

# Calculate bonus based on work experience
salary = int(input('Enter your salary: '))
experience = int(input('Enter your work experience (in years): '))
if 2 < experience <= 5:
    print(f'Your experience is {experience} years. You will receive a bonus of {salary * 0.02}.')
elif 5 < experience <= 10:
    print(f'Your experience is {experience} years. You will receive a bonus of {salary * 0.05}.')
else:
    print('Your salary remains unchanged.')

# Check if a triangle is a right triangle
a = float(input('Enter side a: '))
b = float(input('Enter side b: '))
c = float(input('Enter side c: '))
if c**2 == a**2 + b**2:
    print('The triangle is a right triangle.')
else:
    print('The triangle is not a right triangle.')

# Square positive numbers, leave negatives unchanged
num1 = float(input('Enter number 1: '))
num2 = float(input('Enter number 2: '))
num3 = float(input('Enter number 3: '))

if num1 > 0:
    print(f'The square of {num1} is {num1**2}.')
else:
    print(f'{num1} is a negative number.')

if num2 > 0:
    print(f'The square of {num2} is {num2**2}.')
else:
    print(f'{num2} is a negative number.')

if num3 > 0:
    print(f'The square of {num3} is {num3**2}.')
else:
    print(f'{num3} is a negative number.')

# Cube positive numbers, replace negatives with 0
num1 = float(input('Enter number 1: '))
num2 = float(input('Enter number 2: '))
num3 = float(input('Enter number 3: '))

if num1 > 0:
    print(f'The cube of {num1} is {num1**3}.')
else:
    print(f'{num1} is negative and replaced with 0.')

if num2 > 0:
    print(f'The cube of {num2} is {num2**3}.')
else:
    print(f'{num2} is negative and replaced with 0.')

if num3 > 0:
    print(f'The cube of {num3} is {num3**3}.')
else:
    print(f'{num3} is negative and replaced with 0.')

# Check if a natural number is even and divisible by 5
n = int(input('Enter a natural number: '))
if n % 2 == 0 and n % 5 == 0:
    print('The number is even and divisible by 5.')
elif n % 2 != 0 and n % 5 == 0:
    print('The number is odd but divisible by 5.')
elif n % 2 == 0 and n % 5 != 0:
    print('The number is even but not divisible by 5.')
else:
    print('The number is odd and not divisible by 5.')

# Check if a point lies in the first quadrant
x = float(input('Enter x-coordinate of point A: '))
y = float(input('Enter y-coordinate of point A: '))
if x > 0 and y > 0:
    print('The point lies in the first quadrant.')
else:
    print('The point does not lie in the first quadrant.')

# Compare the difference of squares and the square of the difference
a = float(input('Enter a: '))
b = float(input('Enter b: '))
if a**2 - b**2 > abs(a - b)**2:
    print('The difference of squares is greater.')
else:
    print('The square of the difference is greater.')

# Check if a triangle is equilateral
a = float(input('Enter side a: '))
b = float(input('Enter side b: '))
c = float(input('Enter side c: '))
if a == b == c:
    print('The triangle is equilateral.')
else:
    print('The triangle is not equilateral.')

# Check if three numbers form a Pythagorean triplet
a = float(input('Enter side a: '))
b = float(input('Enter side b: '))
c = float(input('Enter side c: '))
if c**2 == a**2 + b**2 or a**2 == b**2 + c**2 or b**2 == a**2 + c**2:
    print('The numbers form a Pythagorean triplet.')
else:
    print('The numbers do not form a Pythagorean triplet.')

# Determine if a circle can be inscribed in or circumscribed around a square
circle_area = float(input("Enter the area of the circle: "))
square_area = float(input("Enter the area of the square: "))

radius = math.sqrt(circle_area / math.pi)
side = math.sqrt(square_area)

if radius <= side / 2:
    print("The circle can be inscribed in the square.")
else:
    print("The circle cannot be inscribed in the square.")

if side <= radius * math.sqrt(2):
    print("The square can be inscribed in the circle.")
else:
    print("The square cannot be inscribed in the circle.")
# Determine if a circle can fit into a rectangle
circle_area = float(input("Enter the area of the circle: "))
rectangle_width = float(input("Enter the width of the rectangle: "))
rectangle_height = float(input("Enter the height of the rectangle: "))

radius = math.sqrt(circle_area / math.pi)
if radius * 2 <= rectangle_width and radius * 2 <= rectangle_height:
    print("The circle can fit inside the rectangle.")
else:
    print("The circle cannot fit inside the rectangle.")

# Determine if a triangle can be formed with given sides
a = float(input('Enter side a: '))
b = float(input('Enter side b: '))
c = float(input('Enter side c: '))
if a + b > c and b + c > a and c + a > b:
    print('The triangle can be formed.')
else:
    print('The triangle cannot be formed.')

# Calculate ticket price based on age
age = int(input('Enter your age: '))
if age <= 5:
    print('The ticket is free for children under 5 years.')
elif 5 < age <= 18:
    print('The ticket price is $5 for ages 6 to 18.')
elif 18 < age <= 60:
    print('The ticket price is $10 for adults.')
else:
    print('The ticket price is $7 for seniors.')

# Determine the largest number among three inputs
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))
num3 = float(input('Enter the third number: '))

if num1 > num2 and num1 > num3:
    print(f'The largest number is {num1}.')
elif num2 > num1 and num2 > num3:
    print(f'The largest number is {num2}.')
else:
    print(f'The largest number is {num3}.')

# Calculate discount based on purchase amount
purchase_amount = float(input('Enter the purchase amount: '))
if purchase_amount < 50:
    print(f'No discount applied. Total amount: ${purchase_amount:.2f}')
elif 50 <= purchase_amount < 100:
    discount = purchase_amount * 0.1
    print(f'A 10% discount of ${discount:.2f} is applied. Total amount: ${(purchase_amount - discount):.2f}')
elif 100 <= purchase_amount < 200:
    discount = purchase_amount * 0.2
    print(f'A 20% discount of ${discount:.2f} is applied. Total amount: ${(purchase_amount - discount):.2f}')
else:
    discount = purchase_amount * 0.3
    print(f'A 30% discount of ${discount:.2f} is applied. Total amount: ${(purchase_amount - discount):.2f}')

# Determine grade based on score
score = float(input('Enter your score: '))
if 90 <= score <= 100:
    print('Grade: A')
elif 80 <= score < 90:
    print('Grade: B')
elif 70 <= score < 80:
    print('Grade: C')
elif 60 <= score < 70:
    print('Grade: D')
else:
    print('Grade: F')

# Determine the type of triangle based on angles
angle1 = float(input('Enter angle 1: '))
angle2 = float(input('Enter angle 2: '))
angle3 = float(input('Enter angle 3: '))

if angle1 + angle2 + angle3 == 180:
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        print('The triangle is a right triangle.')
    elif angle1 < 90 and angle2 < 90 and angle3 < 90:
        print('The triangle is an acute triangle.')
    else:
        print('The triangle is an obtuse triangle.')
else:
    print('The angles do not form a triangle.')

# Determine the smallest number among three inputs
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))
num3 = float(input('Enter the third number: '))

if num1 < num2 and num1 < num3:
    print(f'The smallest number is {num1}.')
elif num2 < num1 and num2 < num3:
    print(f'The smallest number is {num2}.')
else:
    print(f'The smallest number is {num3}.')
# Determine the category of a given number
number = float(input('Enter a number: '))
if number > 0:
    print('The number is positive.')
elif number < 0:
    print('The number is negative.')
else:
    print('The number is zero.')

# Calculate electricity bill based on usage
units = float(input('Enter the number of electricity units consumed: '))
if units <= 100:
    bill = units * 0.5
elif units <= 200:
    bill = 100 * 0.5 + (units - 100) * 0.75
elif units <= 300:
    bill = 100 * 0.5 + 100 * 0.75 + (units - 200) * 1.2
else:
    bill = 100 * 0.5 + 100 * 0.75 + 100 * 1.2 + (units - 300) * 1.5
print(f'The electricity bill is: ${bill:.2f}')

# Determine the type of day based on temperature
temperature = float(input('Enter the temperature in degrees Celsius: '))
if temperature > 30:
    print('It’s a hot day.')
elif 20 <= temperature <= 30:
    print('It’s a warm day.')
elif 10 <= temperature < 20:
    print('It’s a cool day.')
else:
    print('It’s a cold day.')

# Check if a number is divisible by 3 and 5
number = int(input('Enter a number: '))
if number % 3 == 0 and number % 5 == 0:
    print('The number is divisible by both 3 and 5.')
elif number % 3 == 0:
    print('The number is divisible by 3.')
elif number % 5 == 0:
    print('The number is divisible by 5.')
else:
    print('The number is not divisible by 3 or 5.')

# Calculate the final grade based on marks
marks = []
for i in range(5):
    mark = float(input(f'Enter marks for subject {i+1}: '))
    marks.append(mark)

average = sum(marks) / len(marks)
if average >= 90:
    print('Final Grade: A')
elif average >= 80:
    print('Final Grade: B')
elif average >= 70:
    print('Final Grade: C')
elif average >= 60:
    print('Final Grade: D')
else:
    print('Final Grade: F')

# Determine the largest even number among three inputs
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
num3 = int(input('Enter the third number: '))

even_numbers = [n for n in [num1, num2, num3] if n % 2 == 0]
if even_numbers:
    print(f'The largest even number is {max(even_numbers)}.')
else:
    print('No even numbers were entered.')

# Check if a number is prime
number = int(input('Enter a number: '))
if number > 1:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(f'{number} is not a prime number.')
            break
    else:
        print(f'{number} is a prime number.')
else:
    print(f'{number} is not a prime number.')

# Determine the quadrant of a point in a Cartesian plane
x = float(input('Enter the x-coordinate: '))
y = float(input('Enter the y-coordinate: '))
if x > 0 and y > 0:
    print('The point is in the first quadrant.')
elif x < 0 and y > 0:
    print('The point is in the second quadrant.')
elif x < 0 and y < 0:
    print('The point is in the third quadrant.')
elif x > 0 and y < 0:
    print('The point is in the fourth quadrant.')
elif x == 0 and y != 0:
    print('The point lies on the y-axis.')
elif y == 0 and x != 0:
    print('The point lies on the x-axis.')
else:
    print('The point is at the origin.')
