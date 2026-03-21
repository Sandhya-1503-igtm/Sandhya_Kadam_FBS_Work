gender = input("Enter gender (M/F): ").upper()
age = int(input("Enter age: "))

if (gender == "M" and age >= 21) or (gender == "F" and age >= 18):
    print("Eligible to marry")
else:
    print("Not eligible to marry")