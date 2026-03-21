# Convert feet and inches to meters and centimeters

feet = float(input("Enter distance in feet: "))
inches = float(input("Enter distance in inches: "))

meters = feet * 0.3048
centimeters = inches * 2.54

print("Distance in meters:", meters)
print("Distance in centimeters:", centimeters)