# multiplication table
number = int(input("Enter number:"))
for i in range(1,11):
    print(number,"x",i,"=",number * i)

n = int(input("Enter n:"))
total = 0
for i in range(1,n +1):
    total = total + i
    print("sum:",total)

# factorial of a number
n = int(input("Enter number:"))
factorial = 1
for i in range(1,n+1):
    factorial = factorial*i
    print("factorial:", factorial)

# sum of even numbers from 2 to n
n = int(input("Enter n:"))
total = 0
for i in range(2,n+1,2):
    total = total+i
print("sum:", total)

# count of multiples of 3
n = int(input("Enter n:"))
count = 0
for i in range(1,n+1):
    if i % 3 == 0:
        count=count+1
print("count:", count)

#sum of multiples of 5
n = int(input("Enter n:"))
total = 0
for i in range(1,n+1):
    if i % 5 == 0:
        total = total+i
print("sum:", total)

# print all even numbers from 2 to 50
i = 2
while i <= 50:
    print(i)
    i = i+2

# print total of numbers entered by user until 0 is entered
total = 0
number = int(input("ENTER NUMBER:")) 
while number != 0:
    total = total+number
    number = int(input("Enter number:"))
print("total:", total)

# password check
password = ""
while password != "python123":
    password = input("Enter password:")
    print("logical successful")
