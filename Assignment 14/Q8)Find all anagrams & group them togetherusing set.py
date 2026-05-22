words={'eat','tea','bat','ate','tba'}
di={}
for word in words:
    key=''.join(sorted(word))
    if key in di:
        di[key].append(word)
    else:
        di[key]=[word]
print(di.values)          