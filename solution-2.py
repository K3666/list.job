# program make a simple calulator
# this function adds two numbers
def add(x, y):
  return x + y
# this function subtracts two numbers 
def subtract(x, y):
  return x - y
# this function divides two numbers 
def divide(x, y):
  return x / y

print("select operation.")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

while "true":

  value = (1, 2, 3, 4)
  # check if the value is one of the four options
  if value = ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if value == '1':
        print(num1, "+", num2, "=", add(num1, num2))
     
    elif value == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
        
    elif value == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
          
    elif value == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    break
  else:
     print("invalid input ")
          
