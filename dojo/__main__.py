import dojo
TGREEN= '\u001b[36m'
TWHITE = '\033[37m'
print(TGREEN + "Welcome to Dojo 1.0.0", TWHITE)
print("Use the shortcut ( Cmd + K) or (Ctrl + K) to clear the screen")
print("For queries pls visit https://github.com/Japroz-Saini/dojo")
print(TGREEN + "Type 'help', 'contribute', 'creator' or 'quit' for more information!", TWHITE)

def main():
	while True:
		text = input("dojo>>>")
		if text.strip() == "quit()": quit()
		if text.strip() == "help" :
			## Information about the language
			print("Dojo is a microlanguage based off of Python")
			print("Features of Dojo : ")
			print("* Function Declaration")
			print("* Variable Declaration")
			print("* Basic Arithmetic")
			print("To get started create a file called <filename>.dojo")
			print("Type the following things inside of the file : ")
			print("""
			FUN greet(int, string)
			\tFOR i = 0 TO int THEN
			\t\tPRINT(string)
			\tEND
			END
			\n
			greet(2, "Hello from Dojo")
			""")
			print("Then type the following commands inside of the terminal")
			print("\tpython3 shell.py")
			print("\tdojo>>> RUN('<pathtothefilename>.dojo')")
			print("You should see the following output:")
			print("Hello from Dojo")
			print("Hello from Dojo")
			print("\n")
			print("You can also add comments with '#'")
			print("For more information you can visit https://github.com/Japroz-Saini/dojo")
		elif text.strip() == "creator":
			## Information about the creator
			print(TGREEN + "Dojo is a microlanguage based off of Python")
			print("Dojo has a variety of functions and simple features like")
			print("* Function Declaration")
			print("* Variable Declaration")
			print("* Basic Arithmetic")
			print("It was created by Japroz Singh Saini in September 2020", TWHITE)
		elif text.strip() == "contribute":
			## Information about contribute
			print(TGREEN + "You can visit https://github.com/Japroz-Saini/dojo/blob/master/CONTRIBUTE.md")
			print("for more information about contributing", TWHITE)
		elif "RUN(" in text.strip() and ".dojo" not in text.strip():
			print("THe extension of the file has to be '.dojo'")
		else:
			result, error = dojo.run('<stdin>', text)

			if error:
				print(error.as_string())
			elif result:
				if len(result.elements) == 1:
					print(TGREEN + repr(result.elements[0]), TWHITE)
				else:
					print(TGREEN + repr(result), TWHITE)
if __name__ == "__main__":
    main()
