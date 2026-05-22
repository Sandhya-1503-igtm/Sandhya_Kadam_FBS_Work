set={2,5,7,9,3,8}
li=list(set)
max_product=li[0]*li[1]
a=li[0]
b=li[1]
for i in range(len(li)):
    for j in range(i+1,len(li)):
        product=li[i]*li[j]
        if product > max_product:
            max_product=product
            a=li[i]
            b=li[j]
print('Numbers are:',a,'and',b)
print('Maximum product is:',max_product)            