"""
a = int(input("Enter two integers:\n"))
b = int(input())

while True:
    # try:
    #     c = a/b
    #     print("Division =", c)

    # except ZeroDivisionError:
    #     print("b cannot be zero, try again...")

    op = input("Enter operation (+, -, *, / or x to exit): ").lower()

    if op == "+":
        print(f"{a} + {b} = {a+b}")
    elif op == "-":
        print(f"{a} - {b} = {a-b}")
    elif op == "*":
        print(f"{a} * {b} = {a*b}")
    elif op == "/":
        try:
            print(f"{a} / {b} = {a/b}")
        except ZeroDivisionError:
            print("b cannot be zero, try some other operation...")
    elif op == "x":
        break
"""

"""
try:
    a = int(input("Enter two integers:\n"))
    b = int(input())
    c = a/b
except ZeroDivisionError:
    print("b cannot be zero, try some other operation...")
except ValueError:
    print("Please enter integers only...")
"""
"""
while True:
    try:
        a = int(input("a: "))
        b = int(input("b: "))
        op = input("Enter operation(+, -, *, / or x to quit): ")
        if op == "+":
            print(f"{a} + {b} = {a+b}")
        elif op == "-":
            print(f"{a} - {b} = {a-b}")
        elif op == "*":
            print(f"{a} * {b} = {a*b}")
        elif op == "/":
            print(f"{a} / {b} = {a/b}")
        elif op.lower() == "x":
            break
        else:
            print("Invalid input, please try again...")
    
    # except:
    #     print("Something went wrong, please try again...")
    # except Exception:
        # print("Something went wrong, please try again...")
    except Exception as e:
        print(e)
    

print("Thanks!")
"""

"""
fruits = ["Apple", "Mango", "Banana", "Kiwi", "Guava", "Peach"]
x = 0
while x < len(fruits):
    print(fruits[x])

print("End of the program.")
"""
try:
    a = int(input("a: "))
    b = int(input("b: "))

except Exception as e:
    # This code will be executed only when exception is raised
    print(e)

else:
    # This code will be executed only when no exception is raised
    print("Sum =", a+b)

finally:
    # This code will be executed always, no matter what
    # So we put very imp tasks those have to be performed before the program shuts down eg, closing a file that was opened, closing a database connection which was connected
    print("Good bye!")
# print("Good bye!")
