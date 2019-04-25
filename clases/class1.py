class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Example:
	def add(self, n1, n2):
		return n1 + n2

	def result(self):
		return self.add(1, 2)


e1 = Example
x = e1.result()
print(x)
