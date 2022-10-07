while True:
# allow user to choose calculator operation
    print("Enter '1' for Addition")
    print("Enter '2' for Subtraction")
    print("Enter '3' for Multiplication")
    print("Enter '4' for Division")

    # stopping the program loop
    print("Enter 'q' to Exit")


    # allow user to input calculator operation
    opt = input("Enter Calculation Option: ")

    # break loop if exit function q is entered
    if opt == 'q':
        break

    # allow user to input first value
    num1 = float(input('Enter first number: '))

    # allow user to input second value
    num2 = float(input('Enter second number: '))

    # computation
    if opt == "1":
        print(num1, '+', num2, "=", (num1 + num2))
    elif opt == "2":
        print(num1, '-', num2, "=", (num1 - num2))
    elif opt == "3":
        print(num1, '*', num2, "=", (num1 * num2))
    elif opt == "4":
        if num2 == 0:
            print("Cannot divide a number by zero")
        else:
            print(num1, '/', num2, "=", (num1 / num2))
    else:
        print("invalid option")