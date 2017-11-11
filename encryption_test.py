def cryption_function_testing(encrypt_function, decrypt_function, testing_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
	if encrypt_function(testing_string) == decrypt_function(encrypt_function(testing_string))
		return True
	else:
		return False
