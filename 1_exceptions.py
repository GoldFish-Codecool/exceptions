numerator = None
denominator = None

while numerator is None:
    try:
        numerator = int(input("Numerator: "))
    except ValueError:
        print("Numerator is not an integer")

while denominator is None:
    try:
        denominator = int(input("Denominator: "))
    except ValueError:
        print("Denominator is not an integer")

try:
    print(numerator / denominator)
except ZeroDivisionError:
    print("Divison by zero!")
finally:
    print("Goodbye!")
