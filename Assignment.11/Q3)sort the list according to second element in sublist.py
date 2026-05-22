li=[[1,3],[4,1],[2,2],[5,0]]
n=len(li)
for i in range(n):
    #print(i)
    for j in range(0,n-i -1):  #(0,4-1 -1)(0,2)
        #print(j)
        if li[j][1] > li[j+1][1]: #li[0][1]=li[1]>li[0+1][3] 1>3
            temp=li[j]
            li[j]=li[j+1]
            li[j+1]=temp
print('sorted list:',li)            