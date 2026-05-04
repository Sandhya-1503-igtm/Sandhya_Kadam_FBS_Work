li=[1,2,3,4,5,6,7,8,9]
new_list=[]
for i in range(len(li)):
    if(li[i] % 2 != 0):
        new_list = new_list + [li[i]]

print("List after removing even numbers:",new_list)
