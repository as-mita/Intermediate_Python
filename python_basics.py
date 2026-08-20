"""
Python Basic revision

"""
# 1. Variables and data Types

name = "Asmita"
age = 23
height = 5.2
is_learning = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("learning Python: ", is_learning)

print(type(name))
print(type(age))
print(type(height))
print(type(is_learning))

# 2. TYPE CONVERSION


number_as_string = "100"

number = int(number_as_string)
decimal_number = float(number)

print("\nType Conversion:")
print(number)
print(decimal_number)
print(str(number))



# 3. STRINGS


message = "Python is powerful"

print("\nStrings:")
print(message)
print(message.upper())
print(message.lower())
print(message.title())
print(message.replace("powerful", "useful"))
print(message[0])
print(message[-1])
print(message[0:6])

# f-string
language = "Python"
level = "beginner"

print(f"I am learning {language} at a {level} level.")

# Operator
a = 15
b = 4

print("\nArithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

print("\nComparison Operators:")
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# Conditional Statements

score = 78

print("\nConditional Statement:")

if score >= 80:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Needs improvement")


# Nested condition

age = 23
has_id = True

if age >= 18:
    if has_id:
        print("Access allowed.")
    else:
        print("ID required.")
else:
    print("Access denied.")

# LISTS

fruits = ["apple", "banana", "mango", "orange"]

print("\nLists:")
print(fruits)
print(fruits[0])
print(fruits[-1])

fruits.append("grape")
fruits.insert(1, "kiwi")
fruits.remove("banana")

print("Updated list:", fruits)

# List slicing
print("First two:", fruits[:2])
print("Last two:", fruits[-2:])


# Tuples
coordinates = (27.7, 85.3)

print("\nTuple:")
print(coordinates)
print("Latitude:", coordinates[0])
print("Longitude:", coordinates[1])


# Sets
numbers = {1, 2, 3, 3, 4, 5}

print("\nSet:")
print(numbers)

numbers.add(6)
numbers.remove(2)

print("Updated set:", numbers)

# Dictionaries
student = {
    "name": "Asmita",
    "age": 23,
    "course": "Data Science"
}

print("\nDictionary:")
print(student)

print("Name:", student["name"])
print("Course:", student["course"])

student["level"] = "Beginner"

print("Updated dictionary:", student)
 
# For loop
print("\nFor Loop:")

for fruit in fruits:
    print(fruit)
    