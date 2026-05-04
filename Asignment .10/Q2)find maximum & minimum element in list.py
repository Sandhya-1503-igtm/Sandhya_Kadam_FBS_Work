li=[10,25,60,30,45]

max_value=li[0]
min_value=li[0]
for i in li:
    if(i > max_value ):
        max_value=i
    if(i < min_value):
        min_value=i    
print("Max:", max_value)        
print("Min:", min_value)