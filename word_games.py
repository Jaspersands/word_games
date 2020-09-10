with open("scrabble.txt", "r") as f:
	player = 1
	words = []
	word = ""
	for line in f:
		words.append(line.rstrip("\n"))
	letter = input("enter letter: ")
	count = 3
	for x in words:
		if x == (word += letter):
			print("player " + player + " loses")

	for x in words:
		if x.startswith(word += letter) == False:
			count -= 1
			if count = 0:
				print("you lose")
			elif count == 2
				print("not a word. You have 2 tries left.")
			else
				print("not a word. You have 1 try left.")
	print(word)


