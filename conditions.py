#encoding: utf-8
print("Привет, OY!")

p = 'red'
if p == 'green':
	print("You won 5 points")
elif p == 'yellow':
	print("Your won 10 points")
else:
	print("You won nothing.")

colors = ['red', 'green', 'blue']
if 'red' in colors:
	print('Red is allowed.')
if 'redd' not in colors:
	print('Redd is not allowed')

#users = ['masha', 'peet', 'user1', 'admin', 'vasya']
users = []
if users:
	for user in users:
		if user == 'admin':
			print("Hello " + user.title() + "! would you like to see a report?")
		else:
			print("Hello " + user.title() + "! welcome back!")
	print('There are ' + str(len(users)) + " in the system.")
else:
	print("There is no users in the list.")

usernames = ['ray', 'iVan3', 'Vasiliy', 'admin']
new_users = ['masha', 'ivan3']
for user in new_users:
	for exist_user in usernames:	
		if user.lower() == exist_user.lower():
			print("This name is already used: " + user)
		else:
			print("This name is free! " + user)

digits = list(range(1, 10))
print(digits)
for digit in digits:
	if digit == 1:
		print(str(digit) + "st")
	elif digit == 2:
		print(str(digit) + "nd")
	elif digit == 3:
		print(str(digit) + "rd")
	else:
		print(str(digit) + "th")

person = {
	'first_name': 'Olga',
	'last_name': 'Yachmeneva',
	'age': 20,
	'city': 'Moscow',
}
print(person['age'])
person['age'] = 30
print(person['age'])
del person['age']
print(person)




