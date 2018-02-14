#encoding: utf-8
def favorite_book(name):
	print("One of my favorite book is '" + name.title() + "'.")
favorite_book('dracula')

def print_ref_info(name, age, passport="no date"):
	print("\nName is: "+ name)
	print("Age is: " + str(age))
	print("Passport number is: " + passport)

print_ref_info("OY", "52", "7698 763425")
print_ref_info(age="42", name="Бомж")
print_ref_info("Fly_sky", "18")
print_ref_info("32", "Fly_sky_1")

def make_shirt(text="Love python", size="XL"):
	"""Печать футболок"""
	print("\nText is: '" + text + "'.")
	print("Size: " + size)

make_shirt('buy.', 'M')
make_shirt(text="xxx", size="S")
make_shirt()
make_shirt(size="L")
make_shirt("XXL")

def city_country(city, country):
	return(city.title() + ', ' + country.title())
print(city_country("moscow", "russia"))

def make_album(author, title, traks=""):
	album = {}
	album['author'] = author
	album['title'] = title
	if traks:
		album['traks'] = traks
	return album
print(make_album("nirvana", "nevermind"))
print(make_album("kino", "gruppa krovi", 10))