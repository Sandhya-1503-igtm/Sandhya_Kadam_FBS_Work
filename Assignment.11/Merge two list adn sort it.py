li1=[1,2,3]
li2=[4,5,6]
merged=li1 + li2
n=len(merged)
print(n)
for i in range(1,n):
    for j in range(n - 1 - 1):
        if(merged[j]>merged[j+1]):
            temp=merged[j]
            merged
            li1[j], li2[j+1] = li2[j+1], li1[j]
print(merged)       


