a = "Experiments"
print(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10])
print(a[-11],a[-10],a[-9],a[-8],a[-7],a[-6],a[-5],a[-4],a[-3],a[-2],a[-1])
#The indexation of string ocurs in two ways , from left to the right 
#and from right to the left .Lef to the right use values from 0 to the 
#final caracter and from right to the left use values from -1 to the 
#(-) value of first character
phrase = input("Type a phrase: ")
i = int(-len(phrase))
f = -1
print("A frase ao contrario e :", end="")
while f >= i:
	print(phrase[f] , end ="")
	f = f-1
print()
