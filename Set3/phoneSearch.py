import re
numbers=[]

inp=input("Enter a sentance :")
num=re.compile('\+91\d{10}')

nums=num.findall(inp)
# numbers.append(nums.group())
print('Mobile number(s)-',nums)