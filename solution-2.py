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

print("value operation -\n" \
       "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")



# Take input from the user 
value = input("Enter value 1, 2, 3, 4 :"))
Enter value (1/2/3/4):3
  # check if the value is one of the four options
  if value = ('1', '2', '3', '4'):
    num1 = int(input("Enter first number: "))
    Enter first number: 50
    num2 = int(input("Enter second number: "))
    Enter second number: 30
    
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
      
50 * 30 = 1500
          
