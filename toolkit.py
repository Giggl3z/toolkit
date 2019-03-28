import time
import random

def menu2():
	menu()

def clear():
	cls = " \n\n"*200
	print(cls)

def startip():
	print("Coming Soon...")
	time.sleep(1)
	clear()
	menu2()


def startguess():
	randomnumber = random.randint(1, 10)
	print("")
	print("Guess the lucky Number\n")
	print("Pick a number between 1 and 10\n")
	lucky = int(input(">> "))

	if lucky == randomnumber:
		print("Congrats! The lucky number is", randomnumber)
		time.sleep(1)
		clear()
		menu2()

	else:
		print("")
		print("Try again, lucky number was not", lucky)
		print("")
		time.sleep(1)
		clear()
		menu2()


def qr():
	print("")
	print("Type 'exit' to show the menu.")
	print("")
	stuff = input("Type your hidden message: ")
	print("")

	if stuff == "exit":
		clear()
		menu2()

	if len(stuff) == 0:
		print("Please type something before continuing")
		print("")
		time.sleep(1)
	else:
		clear()
		api = "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=" + stuff.replace(" ", "+")
		print("Generated QR Code: " + api)
		print("")
		time.sleep(1)

def startqr():
	while True:
		qr()

def menu():
	print("Giggl3z’s Toolbox (USELESSa)\n\n")
	print("Pick an option.\n")
	print("1. QR Code Generator")
	print("2. Guess the Lucky Nunber")
	print("3. IP Lookup\n")

	choice = input(">> ")

	if choice == "1":
		clear()
		startqr()

	if choice == "2":
		clear()
		startguess()

	if choice == "3":
		print("")
		startip()

	if choice == "0":
		print("\nUnknown command or invalid character\n")
		time.sleep(1)
		clear()
		menu()

	if choice > "3":
		print("\nUnknown command or invalid character\n")
		time.sleep(1)
		clear()
		menu()

menu()
