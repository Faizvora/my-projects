
def add(x, y, z):
   return x + y + z

def subtract(x, y, z):
   return x - y -z


def multiply(x, y, z):
   return x * y * z

def divide(x, y, z):
   return x / y / z

for i in range(100):

   print("Select operation.")
   print("1.Add")
   print("2.Subtract")
   print("3.Multiply")
   print("4.Divide")

   choice = input("Enter choice(1/2/3/4):")

   num1 = eval(input("Enter first number: "))
   num2 = eval(input("Enter second number: "))
   num3 = eval(input("Enter third number: "))

   if choice == '1':
      print(num1,"+",num2,"+",num3,"=", add(num1,num2,num3))

   elif choice == '2':
      print(num1,"-",num2,"-",num3,"=", subtract(num1,num2,num3))

   elif choice == '3':
      print(num1,"*",num2,"*",num3,"=", multiply(num1,num2,num3))

   elif choice == '4':
      print(num1,"/",num2,"/",num3,"=", divide(num1,num2,num3))
   
   else:
      print("Invalid input")

      print("/n/n")


