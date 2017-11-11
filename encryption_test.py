"""
Единственная функция модуля позволяет протестировать взаимную обратность функций шифрования.
Принимает две функции, и тестируемую строку.
Возвращает True если декодирование закодированного исходного текста совпадает с исходным текстом.
"""

def cryption_function_testing(encrypt_function, decrypt_function, testing_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
	if testing_string == decrypt_function(encrypt_function(testing_string))
		return True
	else:
		return False
