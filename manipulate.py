file = open("fruits.txt", 'r')
content = file.readlines()
content = [i.rstrip() for i in content]
file.close
a = 0
for k in content:
	print(len(content[a]))
	a+=1
#Other form to do this 
for s in content:
	print(len(s.strip()))#In this case , the line 3,5,8 is unnecessary
