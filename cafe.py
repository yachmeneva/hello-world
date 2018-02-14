class Cafe(object):
	def __init__(self, name, type_cuisine):
		self.name = name
		self.type_cuisine =  type_cuisine

	def get_descriprion(self):
		print(self.name.title() + ", " + self.type_cuisine.title())

class Restoran(Cafe):
	def __init__(self, name, type_cuisine, stars):
		super(Restoran, self).__init__(name, type_cuisine)
		self.stars = stars

	def get_stars(self):
		print("\t" + str(self.stars) + " stars")