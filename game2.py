import random


comp_choice = random.randint(1,10)
chance = 3
print(comp_choice)
while True:
	usr = int(input('enter:'))
	if (usr == comp_choice):
		print("you win")
		break
	chance = chance - 1
	if(chance == 0):
		print("you lose")
		break
	print("try again\n")
