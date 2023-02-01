# Exploration of Lambda Expressions

print()
print('Lamba Expressions')
print()
print("Lambda : Some expression")
print("Lamba x: 3x+1")
print("Lambda x, y: (x*y)**0.5")
print("Lamba x, y, z: 3x + 2y * 55z")
print("Lambda X1, X2, ... , XN: <expression>")
print()
print("Lambda functions are short throwaway functions, good for sorting and quick uses.")
print()

# This is a 'normal' function to compute 3x+1

def f(x):
    return 3*x + 1
print('This is a normal function')
x = int(input('Enter a Number: '))
print(f(x))

# This is a lambda expression/anaonymous function example

g = lambda x: 3*x+1
print()
print("This is a lambda expression")
x = int(input('Enter Another Number: '))
print(g(x))

# This example uses a lambda expression to take two imputs and combines them into one.
# In this case, it is a user's first name and last name.

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print()
fn = input("Enter the first name: ")
ln = input("Enter the last name: ")
print(full_name (fn, ln))

# Another Example
print()
scifi_auth = ["Issac Asimov", "Ray Bradbury", "Robert Heinlein", "Author S. Clarke", "Frank Herbert", "Orson Scott Card", "Douglass Adams", "H. G. Wells", "Leigh Brackett"]

scifi_auth.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifi_auth)

# This is a quadratic function
def build_quadratic_function(a, b, c):
    # This will return the function F(x)=ax^2 =bx =c
    return lambda x: a*x**2 + b*x+c
h = build_quadratic_function(2, 3, -5)
print()
user_in_h = int(input("Enter Another Number: "))
print(h(user_in_h))
