class Geek: 
	def __init__(self, age=0): 
		self.age = age
	
	# getter method 
	@property 
	def age(self): 
		return self._age
	
	# setter method
	@age.setter
	def age(self, x): 
		self._age = x

raj = Geek() 

# setting the age using setter 
raj.age = 21 

# retrieving age using getter 
print(raj.age) 
print(raj._age)