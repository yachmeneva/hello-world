#encoding: utf-8
from cafe import Cafe
from cafe import Restoran
import user as u
from random import randint

my_cafe = Cafe("Шоколадница", "кофейня")
my_cafe.get_descriprion()


my_rest = Restoran("Жан-поль", "французская кухня", 4)
my_rest.get_descriprion()
my_rest.get_stars()



me_user = u.User("oy", 'qwerty123')
print(me_user.get_full_name())

print("\n\n")


p = ['Курить','Бухать', 'Опаздывать']
adm = u.Admin("md", "QwErTy123", p)
print(adm.get_full_name())
#adm.set_privilleges(p)
adm.privilleges.get_privilleges()


class Die():
	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self, number):
		print("\n\n")
		for i in range(0, number):
			print("Кубик выпал на: " + str(randint(1, self.sides)))

my_die = Die()
my_die.roll_die(10)

my_die10 = Die(10)
my_die10.roll_die(10)

my_die20 = Die(20)
my_die20.roll_die(10)


