n=int(input('Enter number of students'))
total_percent=0
for i in range(n):
    total=0
    print('Student,i+1')


    for j in range(5):
        marks= int(input('Enter marks'))
        total+=marks
        percent=total/5
        print('Percentage:',percent)
        total_percent+=percent
avg=total_percent/n
print('Average percent=', avg)        

