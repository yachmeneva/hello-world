#encoding: utf-8

class Cafe(object):
	def __init__(self, name, type_cuisine):
		self.name = name
		self.type_cuisine =  type_cuisine

	def get_descriprion(self):
		print(self.name.title() + ", " + self.type_cuisine.title())


my_cafe = Cafe("Шоколадница", "кофейня")
my_cafe.get_descriprion()


class Restoran(Cafe):
	def __init__(self, name, type_cuisine):
		super(Restoran, self).__init__(name, type_cuisine)
		self.stars = 3

	def get_stars(self):
		print("\t" + str(self.stars) + " stars")


my_rest = Restoran("Жан-поль", "французская кухня")
my_rest.get_descriprion()
my_rest.get_stars()


	