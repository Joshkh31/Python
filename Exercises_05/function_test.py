def name_of_function():
 """
 Simple test function
 """
 print("Yoo hoo!")
name_of_function()
""""""

def name_of_function(first_name):
 """
 Simple test function
 """
 print(f"Yoo hoo, hello {first_name}!")
name_of_function("JOR")
""""""

def calculate_circumference(radius):
 """
 Calculate the circumference of a circle based on its radius
 """
 return 2 * 3.142 * radius
a = calculate_circumference(5)
print(a)
""""""

def calculate_circumference(radius = 1):
 """
 Calculate the circumference of a circle based on its radius
 """
 return 2 * 3.142 * radius
a = calculate_circumference()
print(a)
""""""

def calculate_circumference(radius):
 """
 Calculate the circumference of a circle based on its radius
 """
 return 2 * 3.142 * radius
# Get a radius value as a string
r = input("Provide a radius value: ")
# Convert it to a float
r_float = float(r)
# Call the function and create the variable for the return value
a = calculate_circumference(r_float)
print(a)
