class Parent:
    def getString(self):
        self.user=input("Enter a sring :")

    def printString(self):
        print(self.user.upper())

p=Parent()

p.getString()
p.printString()