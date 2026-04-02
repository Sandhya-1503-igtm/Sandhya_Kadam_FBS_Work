correct_id= 'admin'
correct_pass='1234'
for i in range(3):
    userid=input('Enter userid')
    password=input('Ener password')
    if(userid==correct_id and password==correct_pass):
        print('login successful')
        break
    else:
            print('Program Termiated after 3 attempts')


