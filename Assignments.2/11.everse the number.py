# Program to reverse a three-digit number

num = int(input("Enter a three-digit number: "))

# Extract digits
hundreds = num // 100          # First digit
tens = (num // 10) % 10        # Second digit
units = num % 10               # Third digit

# Reverse number
reversed_num = (units * 100) + (tens * 10) + hundreds

print("Reversed Number:", reversed_num)