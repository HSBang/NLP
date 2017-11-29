class robot:
	"""Represents a robot, with a name"""

	# A class variable, counting the number of robots
	population = 0

	def __init__(self, name):
		"""Initialize the data"""
		self.name = name
		print("(Initializing {})".format(self.name))

		# When this person is create, the robot adds to the population
		robot.population += 1

	def die(self):
		"""I am dying"""
		print("{} is being destroyed".format(self.name))

		robot.population -= 1

		if robot.population == 0:
			print("{} was the last one".format(self.name))
		else:
			print("There are still {:d} robots working".format(robot.population))

	def say_hi(self):
		"""Generating by the robot"""

		print("Greeetings, my master calls me {}".format(self.name))

	@classmethod
	def how_many(cls):
		"""Prints the current population"""
		print("We have {:d} robots.".format(robot.population))

droid1 = robot('R2-D2')
droid1.say_hi()
robot.how_many()

droid2 = robot('C-3PO')
droid2.say_hi()
robot.how_many()

print("\nRobots can do some work here.\n")

droid1.die()
droid2.die()

robot.how_many()