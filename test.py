class Profile():
	def __init__(self, name, age):
		self.name = name
		self.age = age		
	def greetings(self):
		return "Welcome Mr. " + str(self.name) + ". Your Age is " + str(self.age) 


	
p1 = Profile("Mehmood Ghaffar", 30)

print(p1.name)
print(p1.greetings())