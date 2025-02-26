from DistanceConverter import DistanceConverter
from MassConverter import MassConverter
from TimeConverter import TimeConverter

def convert(c):
    number = float(input("Enter number: "))
    unit1 = input("Enter unit 1: ")
    unit2 = input("Enter unit 2: ")
    number *= c.convert(unit1, unit2)
    print(f"Your result is {number} {unit2}")

while True:
    print("What converter do you need?")
    print("1 - Distance")
    print("2 - Mass")
    print("3 - Time")
    print("0 - Exit")
    i = input("Your choice: ")
    if i == "1":
        dc = DistanceConverter()
        convert(dc)
    elif i == "2":
        mc = MassConverter()
        convert(mc)
    elif i == "3":
        tc = TimeConverter()
        convert(tc)
    elif i == "0":
        print("Goodbye")
        break
    else:
        print("Wrong input")