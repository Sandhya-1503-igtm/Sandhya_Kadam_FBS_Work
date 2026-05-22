str='Ali Pune Ali Mumbai Pune'
words=str.split()
di={}
for i in words:
    if i in di:
        di[i]=di[i]+1
    else:
        di[i]=1
print(di)            