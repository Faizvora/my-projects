num = eval(input("enter your number"))
if (num < 0):
	num = (-1) * num
temp = num
digits = len(str(num))
sum = 0

for i in range(digits):
	temp1 = num % 10
	sum = sum + temp1**digits
	num = num//10
if(sum == temp):
	print("armstrong")
else:
	print("not armstrong")