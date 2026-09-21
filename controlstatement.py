age = 18
if age>=20:
    print("eligible")
else:
    print("not eligible")

marks = 60
if marks <= 100:
    print("pass")
else:
    print("fail")
marks = int(input("Enter marks:"))

if marks>=90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")

# divisible by 5
number = int(input("Enter a number:"))
if number % 5 == 0:
    print("Divisible by 5")

# temperatiure check
temperature = float(input("Enter temperature:"))

if temperature > 40:
    print("High temperature")


# odd or even check
number = int(input("Enter a number :"))
if number % 2 == 0:
    print("even")
else :
    print("odd")

marks = int(input("Enter marks :"))
if marks >= 40:
    print("pass")
else:
    print("fail")


number = int(input("Enter a number :"))
if number >= 0:
    print("positive")
else:
    print("negative")


number = int(input("Enter a number :"))
if number > 100:
    print("Number is greater than 100")
else:
    print("Number is not greater than 100")


a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
if a > b:
    print("Largest:", a)
elif b > a:
    print("Largest:", b)
else:
    print("Both are equal")

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >=c:
    print("Largest:", b)
else:
    print("Largest:", c)

number = int(input("enter a number:"))
if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("Zero")
    

#print numbers from 1 to 10
for i in range(1,11):
    print(i)

for i in range(1,11):
    print(i)
    i = i-1

# print numbers from 10 to 1
for i in range(10,0,-1):
    print(i)

for i in range(1,20):
    print(i)
    i = +1
    





