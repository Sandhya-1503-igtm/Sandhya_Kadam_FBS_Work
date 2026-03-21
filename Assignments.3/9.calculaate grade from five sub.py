marks = []
for i in range(1,6):
    marks.append(float(input(f"Enter marks of subject {i}: ")))

total = sum(marks)
percentage = total / 5

if percentage >= 60:
    grade = "First Class"
elif percentage >= 50:
    grade = "Second Class"
elif percentage >= 40:
    grade = "Third Class"
else:
    grade = "Fail"

print("Percentage:", percentage)
print("Grade:", grade)