ENCRYPT_DICT = { chr(i) : chr(i + 13) for i in range(33, 127 - 13) }
ENCRYPT_DICT.update( { chr(i) : chr(i - 94 + 13) for i in range(127 - 13, 127) } )
#########################################################################
keys = list(ENCRYPT_DICT.keys())
values = list(ENCRYPT_DICT.values())
#########################################################################
DEENCRYPT_DICT = {}
for i in range(len(keys)):
	DEENCRYPT_DICT.update( { values[i] : keys[i] } )
#########################################################################
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
def ROT13_ENCRYPT(text):

	crypted_text = ""

	for i in text:
		if i in ENCRYPT_DICT:
			crypted_text += ENCRYPT_DICT.get(i)
		else:
			crypted_text += i

	return crypted_text
#########################################################################
def ROT13_DECRYPT(text):

	decrypted_text = ""

	for i in text:
		if i in DEENCRYPT_DICT.keys():
			decrypted_text += DEENCRYPT_DICT.get(i)
		else:
			decrypted_text += i

	return decrypted_text
#########################################################################
def file_work(function):
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
def encrypt_file():
	file_work(ROT13_ENCRYPT)
#########################################################################
def decrypt_file():
	file_work(ROT13_DECRYPT)
#########################################################################
def encrypt_string():
	STRING = take_something(str, "\t\tput your string here : ")
	print("\t\t", ROT13_ENCRYPT(STRING))
#########################################################################
def decrypt_string():
	STRING = take_something(str, "\t\tput your string here : ")
	print("\t\t", ROT13_DECRYPT(STRING))
#########################################################################


#main cycle

if __name__ == "main":
	import encryption_test

	assert encryption_test.cryption_function_testing(), "crypt functions error"

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
