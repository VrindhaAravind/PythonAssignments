inp=input("Enter some words separated by commas :")

words=[word.lower() for word in inp.split(',')]
# print(words)

for i in range(0,len(words)):
    for j in range(0,len(words)):
        if words[j]>words[i]:
            temp=words[i]
            words[i]=words[j]
            words[j]=temp

print(words)
