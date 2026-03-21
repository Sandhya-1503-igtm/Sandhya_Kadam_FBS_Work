import random

correct_userid = "admin"
correct_password = "1234"

userid = input("Enter userid: ")
password = input("Enter password: ")

if userid == correct_userid and password == correct_password:
    captcha = random.randint(1000, 9999)
    print("Captcha:", captcha)
    user_captcha = int(input("Enter captcha: "))
    if user_captcha == captcha:
        print("Success")
    else:
        print("Failed")
else:
    print("Incorrect userid or password")