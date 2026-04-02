n=int(input('Enter number of passengers'))
cost=int(input('Enter ticket cost'))
total=0
for i in range(1,n):
    age=int(input('Enter age'))
    if (age<12):
        total+=cost*0.7
    elif (age>59):
        total+=cost*0.5
    else:
        total+=cost
    print('Total Amount')    
