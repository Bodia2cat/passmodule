#IPL - InputPasswordLoger
def code():
	print("Hi, here will be your code!!! ")
	exit()
def idloger():
	handle = open("id12.txt", "r")
	data = handle.read()
	handle.close()
	if data == "43454345":
		print("Sucsessful!!! ")
		code()

def Loger():
	print("This is password loger ")
	print("Do you have ID? ")
	idlog = input("... ")
	if idlog == "yes":
		idloger()
	if idlog == "no":
		pass
	print("Login: ")
	log = input("... ")
	if log == "Bodia":
		pas = input("password ")
		if pas == "ConyCony":
			code()
Loger()
