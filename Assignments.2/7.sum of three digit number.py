# Program to calculate total salary of an employee

basic = float(input("Enter basic salary: "))

da = basic * 0.10
ta = basic * 0.12
hra = basic * 0.15

total_salary = basic + da + ta + hra

print("DA =", da)
print("TA =", ta)
print("HRA =", hra)
print("Total Salary =", total_salary)