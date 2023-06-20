def get_number(prompt):
    number = None
    while number is None:
        try:
            number = int(input(f"{prompt}: "))
        except ValueError:
            print(f"{prompt} is not an integer")
    return number


try:
    numerator = get_number("Numerator")
    denominator = get_number("Denominator")
    if numerator < 0:
        raise ValueError("Negative numerator!")
    if denominator < 0:
        raise ValueError("Negative denominator")
    print(numerator / denominator)
except Exception as ex:
    print(f"{type(ex)}: {ex}")
finally:
    print("Goodbye!")
