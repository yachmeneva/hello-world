#encoding: utf-8
filename = "files/learning_python.txt"
#10-1
with open(filename) as file_obj:
	#all_file = file_obj.read()
	#print("All file:")
	#print(all_file)

	#print("File by strings:")
	#for line in file_obj:
	#	print(line.rstrip())

	print("File in list:")
	file_list = []
	for line in file_obj:
		file_list.append(line.rstrip())

for line in file_list:
	print(line)

#10-2
for line in file_list:
	new_line = line.replace("Python", "Java")
	print(new_line)

#10-3
print("\n\n")
# с русскими буквами инпут не пашет в 2.7
username = input("Введите ваше имя: ")
print(username.title())
with open("files/guests.txt", 'w') as file_obj2:
	file_obj2.write(username)

#10-4
while True:
	user = input("Input your name please. \nInput q to exit: ")
	if user == 'q':
		break
	else:
		with open("files/users.txt", 'a') as f_obj:
			f_obj.write(user.title() + "\n")





