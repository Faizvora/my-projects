import random
winner=None
print("1.rock\n2.paper\n3.siczzor")
user_input = int(input())
comp_choice=random.randint(1,3)
# 1=user,2=comp,
if(user_input == comp_choice):
	winner = 0
elif(user_input == 1):
	if(comp_choice == 2):
		winner = 1
	elif(comp_choice == 3):
		winner = 1
elif(user_input == 2):
	if(comp_choice == 1):
		winner = 2
	elif(comp_choice == 3):
		winner = 2
elif(user_input == 3):
	if(comp_choice == 1):
		winner = 2
	elif(comp_choice == 2):
		winner = 1
if(winner == 0):
	print("TIE")
elif(winner == 1):
	print("user wins")
elif(winner == 2):
	print("comp wins")
