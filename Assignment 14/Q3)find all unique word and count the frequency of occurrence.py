words=['apple','mango','apple','banana','mango']
unique_words=set(words)
print('unique words:',unique_words)
for i in unique_words:
    print(i,'=',words.count(i))