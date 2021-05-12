x=5
while (x<10):
	print(x)
	x += 1
else:
	print("number is greater than or equal to 10")


# Break and continue keywords

name = 'Sammy'

for letter in name:
	if(letter=='m'):
		break  
	print(letter)


for letter in name:
	if(letter == 'm'):
		continue
	print(letter)s