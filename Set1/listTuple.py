tup1= (1,2,3,4,5,6,7,8,9,10,22,15,95,80,78)
lis1=[]
for i in tup1:
    if i%2==0:
        lis1.append(i)

print(tuple(lis1))