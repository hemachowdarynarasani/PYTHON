is_logged_in = True
print(not is_logged_in)
#atm eligibility checker 
balance = 10000
withdraw = 5000
print(withdraw > 0 and withdraw <= balance)
#stuedent scholarship eligibility checker
marks = float(input("Enter marks:"))
attendence = float(input("Enter attendence:"))
eligible = marks >= 85 and attendence >=75
print("Scholarship eligible:", eligible)
# identity operators
a = None
print(a is None)
print(a is not None)
#bitwise operators
a = 5 
b = 3
print(a & b)
print(a | b )
print(a ^ b)
print(a << b)
print(a >> b)
a = 8
b=2
print(a<<b)
print(a>>b)
a = 13
b = 5
print(a >> b)
a = 12
b = 6
print(a << b)
a = 9
b = 3
print(a >> b)
a = 7
b = 4
print(a << b)
# electricity bill calculator
units=int(input("Enter electricity units:"))
rate=6
bill=units*rate
print("Electricity bill:", bill)
# travel expence clculator
travel = float(input("Travel expense: "))
food = float(input("Food expense:"))
hotel = float(input("Hotel expense:"))
total = travel+food+hotel
print("Total  expense:", total)
#list in python
#list is an ordered and changeable collection that can store
marks = [80,90,75,85]
print(marks)
#accessing elements in a list
marks = [80,90,75,85]
print(marks[0])
print(marks[1])
print(marks[3])
# change elements in a list
marks = [80,90,75]
marks[1] = 95
print(marks)
#add elements to a list
marks = [80,90,75]
marks.append(85)
print(marks)
# remove elements from a list
marks = [80,90,75]
marks.remove(90)
print(marks)
numbers = [10,20,30]
numbers.insert(1,15)
print(numbers)























































































































































































































































































