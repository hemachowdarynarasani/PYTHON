a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)
numbers = [10,20,30]
numbers.clear()
print(numbers)

numbers = [10,20,30,40]
print(numbers.index(30))

numbers = [10,20,20,30,20]
print(numbers.count(20))
numbers = [40,10,30,20]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

# Reverse method
numbers = [10,20,30,40]
numbers.reverse()
print(numbers)

# Copy method
a = [1,2,3]
b = a.copy()
print(b)

numbers = [10,20,30,40,50]
print(numbers[1:4])
print(numbers[ :3])
print(numbers[2: ])
print(numbers[ ::-1])





