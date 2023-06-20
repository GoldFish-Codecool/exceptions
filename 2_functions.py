def get_number(prompt):
    number = None
    while number is None:
        try:
            number = int(input(f"{prompt}: "))
        except ValueError:
            print(f"{prompt} is not an integer")
    return number


try:
    print(get_number("Numerator") / get_number("Denominator"))
except ZeroDivisionError:
    print("Divison by zero!")
finally:
    print("Goodbye!")
