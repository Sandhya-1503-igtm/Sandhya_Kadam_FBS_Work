li=[10,20,30,40,50]
largest=li[0]
second=li[0]

for i in li:
    if(i>largest):
        second=largest
        largest=i
    elif(i > second):
        second=i
print("Second Largest:",second)            