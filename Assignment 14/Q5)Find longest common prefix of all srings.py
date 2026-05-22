str=['flower','flow','flight']
prefix=str[0]
for i in str[1:]:
    while i.find(prefix)!=0:
        prefix=prefix[:-1]
print('Longest common prefix:',prefix)        
