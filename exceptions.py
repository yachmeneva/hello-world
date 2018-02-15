#10-6, 10-7

message = "Input the number (type q to exit): "

def input_number():
	while True:
		n = input(message)
		try:
			n = int(n)
		except ValueError:
			print("You have not inputed two numbers! ")
		else: 
			return n

n = input_number()
m = input_number()
print("The sum is: " + str(n+m))


#10-8
def read_file(filename):
	with open(filename) as file_obj:
		print(file_obj.read())

files = ["files/catts.txt", "files/dogs.txt"]
for file in files:
	try:
		read_file(file)
	except FileNotFoundError:
		#print("Cannot open the file: " + file)
		pass
