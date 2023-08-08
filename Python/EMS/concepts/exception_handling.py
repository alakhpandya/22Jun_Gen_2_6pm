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

# Next class: Exception handling remaining points, resource management