numerator = ""
denominator = ""

while not numerator.isnumeric():
    numerator = input("Numerator: ")

numerator = int(numerator)

while not denominator.isnumeric():
    denominator = input("Denominator: ")

denominator = int(denominator)

print(numerator / denominator)
