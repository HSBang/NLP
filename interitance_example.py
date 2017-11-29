class SchoolMember:
	'''Represents any school member'''
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print('(Initializing SchoolMemebr: {})'.format(self.name))

	def tell(self):
		'''Tell my details'''
		print('Name:"{}" Age:"{}"'.format(self.name, self.age))

class Teacher(SchoolMember):
	'''Represents a teacher'''
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age) # Inherit __init__ method of SchoolMember
		self.salary = salary
		print('(Initializing Teacher: {})'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
	'''Represent a studnet'''
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print('(Initializing Student: {})'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Marks: "{}"'.format(self.marks))


t = Teacher('Mrs. Kim', 40, 50000)
s = Student('Hyoseok', 20, 4.0)
print()
members = [t, s]
for member in members:
	member.tell()

