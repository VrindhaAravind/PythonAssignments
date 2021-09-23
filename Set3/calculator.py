class Calculator:
        def __init__(self,num1,num2):
                self.num1=num1
                self.num2=num2

        def add(self):
                return self.num1+self.num2

        def sub(self):
                return self.num1-self.num2

        def mul(self):
                return self.num1*self.num2

        def div(self):
                if self.num2==0:
                        raise ValueError("Number cannot be 0")
                return self.num1/self.num2


#
#
#
# while True:
#     choice=int(input("Enter your choice :1.add, 2.subtract,3.multiply,4.divide :"))
#     if choice==1:
#         print("Result :",a.add(num1,num2))
#     elif choice == 2:
#         print("Result :", a.sub(num1,num2))
#     elif choice == 3:
#         print("Result :", a.mul(num1,num2))
#     elif choice == 4:
#         print("Result :", a.div(num1,num2))
#     else:
#         print("Enter valid input")
#         break;