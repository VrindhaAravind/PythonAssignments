import re
print("enter email id to validate :")
mail=input()

x='([a-zA-Z0-9+_.]+@[a-z]+[.]+[a-z]{2,3}$)'
match=re.fullmatch(x,mail)
if match is not None:
    print("Valid")
else:
    print("Invalid")