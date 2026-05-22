str=input('Enter a string:')
words=str.split()
for word in words:
    count=0
    for w in words:
        if(word==w):
            count=count+1
    print(word, ":", count)

