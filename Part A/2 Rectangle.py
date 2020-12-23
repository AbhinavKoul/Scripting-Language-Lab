class Rectangle:
	def __init__(self):
		self.l = int(input("Enter length"))
		self.b = int(input("Enter breadth"))
	def area(self):
		print("The area of the given rectangle is",self.l*self.b)
	
	def permimerter(self,a:int)->bool:
		if(self.l + self.b > a):
			return True
		else:
			return False


R=Rectangle()
R.area()