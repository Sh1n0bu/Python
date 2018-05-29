#Program to convert celsius to fahrenheit using functions 
def celsius_to_fahrenheit(celsius):
	fahrenheit = (9*(celsius))/5 +32
	return fahrenheit

#celsius = float(input("Type the temperature in celsius: "))

#if celsius < -273.15 :
#	print("The minimun temperature is the absolute zero , thats equal to -273.15")

#else:
#	print(celsius_to_fahrenheit(celsius))
temperature=[10, -20, -289, 100]
a = 0

for i in temperature:
	if temperature[a] < -273.15:
		print("The minimun temperature is the absolute zero , thats equal to -273.15")
	else :
		print(celsius_to_fahrenheit(temperature[a]))
	a = a+1
		

