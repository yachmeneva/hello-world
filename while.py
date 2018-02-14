#7-8
sandwich_orders = ['tuna', 'chicken', 'vegan']
finished = []
while sandwich_orders:
	current = sandwich_orders.pop()
	print('I made you ' + current + ' sandwich.')
	finished.append(current)
print(finished)

#7-9
sandwich_orders_2 = ['tuna', 'pastrami', 'chicken', 'pastrami', 'pastrami', 'vegan']
finished_2 = []
print("Unfortunately there is no more pastrami:(")
while ('pastrami' in sandwich_orders_2):
	sandwich_orders_2.remove('pastrami')

while sandwich_orders_2:
	current = sandwich_orders_2.pop()
	print('I made you ' + current + ' sandwich.')
	finished.append(current)
print(finished)

#7-10
prompt = "What is your dream vacation place? "
prompt += "\n For exit type 'quit' __"
places = []
while True:
	place = input(prompt)
	if place == 'quit':
		break
	else:
		places.append(place)
print("Yep! now save your money to tickets to:\n")
print(places)
