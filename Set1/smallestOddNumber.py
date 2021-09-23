user=input("Enter a list of numbers :")
nums=sorted(user.split(','))

for num in nums:
    if (int(num)%2!=0):
        break;
print(num)
