class Circle:
    def area(self,radius):
        self.radius=radius
        area=float(3.14*radius*radius)
        print("The area of circle is :")
        print(area)


inp=float(input("Enter the radius of circle :"))
rad=Circle()
rad.area(inp)