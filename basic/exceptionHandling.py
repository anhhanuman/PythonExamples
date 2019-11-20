def spam(inputNumber):
    try:
        print(42 / inputNumber)
        return 42 / inputNumber
    except ZeroDivisionError:
        print("Invalid input number, the input number is 0, it\t's cannot be divided")


theInputNumber = int(input('now enter the input: '))
spam(theInputNumber)
