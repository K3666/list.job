def add(x,y):
  return x + y
def subtract(x,y):
  return x - y
def multiply(x,y):
  return x * y
def divide(x,y):
  return x / y

print("value operation -\n" \
       "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")


 
value = "1"
  if value = ('1', '2', '3', '4'):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
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
      

          
