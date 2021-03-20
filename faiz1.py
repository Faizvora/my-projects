temp =  eval(input("enter the percent"))

grade = None

if(temp >=0 and temp <=40):
	grade = "F"
elif(temp > 40 and temp <= 50):
	grade ="E"
elif(temp > 50 and temp <= 60):
	grade = "D"
elif(temp > 60 and temp <= 70):
	grade = "C"
elif(temp > 70 and temp<= 80):
	grade = "B"
elif(temp > 80 and temp<= 90):
	grade = "A"
elif(temp > 90 and temp<= 100):
	grade = "O"
else:
	print("working")
print (grade)


