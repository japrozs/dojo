import dojo
TGREEN= '\u001b[36m'
TWHITE = '\033[37m'
print(TGREEN + "Welcome to Dojo 1.0.0", TWHITE)
print("Use the shortcut ( Cmd + K) or (Ctrl + K) to clear the screen")
print("For queries pls visit https://github.com/Japroz-Saini/dojo")
print(TGREEN + "Type 'help' for more information!", TWHITE)

while True:
	text = input("dojo>>>")
	if text.strip() == "quit()": quit()
	if text.strip() == "help" :
		print("help")
	else:
		result, error = dojo.run('<stdin>', text)

		if error:
			print(error.as_string())
		elif result:
			if len(result.elements) == 1:
				print(TGREEN + repr(result.elements[0]), TWHITE)
			else:
				print(TGREEN + repr(result), TWHITE)
