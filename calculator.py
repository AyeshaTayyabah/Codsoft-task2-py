while True:
    print("\n Enter operator to perform the operation:")
    print("\t+ (addition), - (subtraction), * (multiplication), / (division)")
    print("Enter '!' to end the program")
    user_input = input("\t ")
    if user_input == "!":
        break
    elif user_input in ("+", "-", "*", "/"):
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if user_input == "+":
            print("Addition of given numbers:", a + b)
        elif user_input == "-":
            print("Subtraction of given numbers:", a - b)
        elif user_input == "*":
            print("Multiplication of given numbers:", a * b)
        elif user_input == "/":
            result = a / b
            print("Division of given numbers:", a / b)
        else:
            print("Invalid input")
    else:
        print("Invalid input")
