word = input("Word to find: ").upper()
strn = input("String to search through: ").upper()

found = True
start = 0

for character in word:
	pos = strn.find(character, start) 
	if pos < 0:
		found = False
		break
	start = pos + 1
if found:
	print("Found!")
else:
	print("Not found :(")
