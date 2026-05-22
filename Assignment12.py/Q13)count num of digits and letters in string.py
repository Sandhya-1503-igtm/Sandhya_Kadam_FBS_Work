str=input('Enter a string:')
digit=0
letter=0
for ch in str:
    if(ch.isdigit()):
        digit=digit+1
    elif ch.isalpha():
        letter=letter+1 
print('Numbrs of digits:',digit)
print('Numbrs of letters:',letter)

