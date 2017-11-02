choice = None
menu = """
		1. encrypt file
		2. decrypt file
		3. encrypt string
		4. decrypt string
		5. exit
		set : """
#########################################################################
def take_something(type = str, text = "put something here : "):
	while(True):
		try:
			something = type(input(text))
			break;
		except:
			print("incorrect type")
	return something
#########################################################################
def encrypt(text, move = 13):
	encr_text = ""
	for char in text:
		if ord(char) >= 33 and ord(char) <= 126:
			encr_text += chr(ord(char) + move)
		else:
			encr_text += char
	return encr_text
#########################################################################
def decrypt(text, move = 13):
	decr_text = ""
	for char in text:
		if ord(char) - move >= 33 and ord(char) - move <= 126:
			decr_text += chr(ord(char) - move)
		else:
			decr_text += char
	return decr_text
#########################################################################
def encrypt_file(function = encrypt):

	FILE_NAME = None
	FILE = None

	while True:
		try:
			FILE_NAME = take_something(str, "\t\tfile path : ")

			if FILE_NAME == "back":
				return

			FILE = open(FILE_NAME, "r")
			break
		except OSError:
			print("\t\tcan not open file ", FILE_NAME, "for read, set 'back' to get back")

	encr_data = function(FILE.read())
	FILE.close()
	
	try:
		FILE = open(FILE_NAME, "w")
	except OSError:
		print("\t\tcan not open file ", FILE_NAME, "for write")
		return

	FILE.write(encr_data)
	FILE.close()
#########################################################################
def decrypt_file():
	encrypt_file(decrypt)
#########################################################################
def encrypt_string():
	STRING = take_something(str, "\t\tput your string here : ")
	print("\t\t", encrypt(STRING))
#########################################################################
def decrypt_string():
	STRING = take_something(str, "\t\tput your string here : ")
	print("\t\t", decrypt(STRING))
#########################################################################


#main cycle
while True:
	choice = take_something(int, menu)

	if choice == 1:
		encrypt_file()
	elif choice == 2:
		decrypt_file()
	elif choice == 3:
		encrypt_string()
	elif choice == 4:
		decrypt_string()
	elif choice == 5:
		exit()
	else:
		print("\t\tincorrect input")
