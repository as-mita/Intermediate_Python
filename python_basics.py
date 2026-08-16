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

# ============================================================
# 2. TYPE CONVERSION
# ============================================================

number_as_string = "100"

number = int(number_as_string)
decimal_number = float(number)

print("\nType Conversion:")
print(number)
print(decimal_number)
print(str(number))


# ============================================================
# 3. STRINGS
# ============================================================

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
