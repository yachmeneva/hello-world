class User(object):
	def __init__(self, name, pwd):
		self.name = name
		self.pwd = pwd

	def get_full_name(self):
		return self.name + " / " + self.pwd


class Privilleges():
	def __init__(self, p_list):
		self.privilleges = p_list

	def get_privilleges(self):
		for p in self.privilleges:
			print(p.title())

class Admin(User):
	def __init__(self, name, pwd, p):
		super(Admin, self).__init__(name, pwd)
		self.privilleges = Privilleges(p)

	def set_privilleges(self, privilleges):
		self.privilleges = []
		for p in privilleges:
			self.privilleges.append(p)
