from connect import test_connection
from connect import add_name
from connect import read_names

db = test_connection()
print("Welcome to the names database.")
while True:
	selection = input("Please choose one of the following options:\n1: Input name\n2: Read names\nQuit: Quits the program\n\nPlease input your option: ")
	# yes, IF-ELSE chains are really super messy, but I'm too lazy to download Python 3.10, which includes a nice switch statement equivalent.
	if selection == '1':
		name_dict = {}
		name_dict[u'firstname'] = input("Enter a first name: ")
		name_dict[u'lastname'] = input("Enter a last name: ")
		print("Adding...")
		add_name(db, name_dict)
	elif selection == '2':
		read_names(db)
	elif selection.lower() == 'quit':
		break
	else:
		print("Invalid choice!\n")