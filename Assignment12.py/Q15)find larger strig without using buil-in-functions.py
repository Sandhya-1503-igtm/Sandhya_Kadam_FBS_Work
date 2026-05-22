str1=input('Enter a string:')
str2=input('Enter a string:')
len1=0
len2=0
for ch in str1:
    len1=len1+1
for ch in str2:
    len2=len2+1 
if len1>len2:
    print('Larger string is:',str1) 
else:
    print('Larger string is:',str2)
