word = input("Type a word: ")
number = input("Type a number: ")
if (int(number) <= len(word) ) :
	print("The" ,number,"character of your word is :" , word[int(number)])
else :
	print("Your word is to short")

