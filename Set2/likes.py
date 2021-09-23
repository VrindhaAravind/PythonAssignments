inp=input("Enter list of names :")
lis=inp.split(',')

if len(lis)==0:
    print("Nobody likes the post")
elif len(lis)==1:
    print(lis[0]," likes your post")
elif len(lis)==2:
    print(lis[0]," and ",lis[1], " likes your post")
elif len(lis)==3:
    print(lis[0],",",lis[1]," and ",lis[2]," likes your post")
else:
    print(lis[0],",",lis[1]," and ",(len(lis)-2)," others likes the post")