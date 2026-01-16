"""
datatypes_demo.py
This script demonstrates Python data types, type conversion,
error handling, arithmetic operations, and dynamic typing.
"""

# ----------------------------------------------------
# 1. Declare variables of different data types
# ----------------------------------------------------

integer_var = 10              # int type
float_var = 3.5               # float type
string_var = "Python"         # string type
boolean_var = True            # boolean type

# ----------------------------------------------------
# 2. Print the type of each variable
# ----------------------------------------------------

print("Data Types:")
print("integer_var:", type(integer_var))
print("float_var:", type(float_var))
print("string_var:", type(string_var))
print("boolean_var:", type(boolean_var))

print("\n----------------------------------")

# ----------------------------------------------------
# 3. Perform arithmetic operations
# ----------------------------------------------------

addition = integer_var + float_var
subtraction = integer_var - float_var
multiplication = integer_var * float_var
division = integer_var / float_var

print("Arithmetic Operations:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

print("\n----------------------------------")

# ----------------------------------------------------
# 4. Convert string input to integer and float
#    with error handling
# ----------------------------------------------------

user_input = input("Enter a number: ")

try:
    # Converting string input to integer
    int_value = int(user_input)
    print("Converted to Integer:", int_value)

    # Converting string input to float
    float_value = float(user_input)
    print("Converted to Float:", float_value)

except ValueError:
    # This block runs if conversion fails
    print("Error: Invalid input! Please enter a numeric value.")

print("\n----------------------------------")

# ----------------------------------------------------
# 5. Concatenate strings and numbers properly
# ----------------------------------------------------

age = 21

# Convert number to string before concatenation
message = "My age is " + str(age)

print("String Concatenation:")
print(message)

print("\n----------------------------------")

# ----------------------------------------------------
# 6. Demonstrate dynamic typing
# ----------------------------------------------------

data = 100
print("data =", data, "| Type:", type(data))

# Reassigning the same variable to a string
data = "Now I am a string"
print("data =", data, "| Type:", type(data))

# Reassigning the same variable to a float
data = 45.67
print("data =", data, "| Type:", type(data))

print("\n----------------------------------")

print("Demo completed successfully!")
