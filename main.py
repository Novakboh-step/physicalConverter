from DistanceConverter import DistanceConverter

while True:
    print("What converter do you need?")
    print("1 - Distance")
    print("0 - Exit")
    i = input("Your choice: ")
    if i == "1":
        dm = DistanceConverter()
        number = float(input("Enter number: "))
        unit1 = input("Enter unit 1: ")
        unit2 = input("Enter unit 2: ")
        number *= dm.convert(unit1, unit2)
        print(f"Your result is {number} {unit2}")
    elif i == "0":
        print("Goodbye")
        break
    else:
        print("Wrong input")