li=[1,2,3,4,5,6]
target=7
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if(li[i]+li[j]==target):
            print(li[i],li[j])
            
