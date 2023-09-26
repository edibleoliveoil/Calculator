c = True
def add(num1, num2):
  print(num1, "plus", num2, "is --->", num1 + num2)
  
def subtract(num1, num2):
  print(num1, "takeaway", num2, "is --->", num1 - num2)
  
def multiply(num1, num2):
  print(num1, "multiplied by", num2, "is --->", num1 * num2)
  
def divide(num1, num2):
  print(num1, "divided by", num2, "is --->", num1 / num2)

def remainder(num1, num2):
  print("The remainder of", num1, "divided by", num2, "is --->", num1 % num2)

def exponent(num1, num2):
  print(num1, "to the power of", num2, "is --->", num1 ** num2)

def main():
  numchoice = ("Now select your first number")
  add_ = ("Add")
  subtract_ = ("Subtract")
  multiply_ = ("Multiply")
  divide_ = ("Divide")
  remainder_ = ("find the remainder")
  exponent_ = ("find the exponent")
  print("Choose an operation")
  print("[1] Add")
  print("[2] Subtract") 
  print("[3] Multiply")
  print("[4] Divide")
  print("[5] Remainder")
  print("[6] Exponent")
  print('[1]', '[2]', '[3]', '[4]', '[5]', '[6]')
  you = ("You have chosen to ")
  choice = int(input())
  
  while choice > 6 :
    print("Invalid option please try again")
    print("Choose an operation")
    print("[1] Add")
    print("[2] Subtract") 
    print("[3] Multiply")
    print("[4] Divide")
    print("[5] Remainder")
    print("[6] Exponent")
    print('[1]', '[2]', '[3]', '[4]', '[5]', '[6]')
    choice = int(input())
  if choice == 6:
    print(you + exponent_)
    print(numchoice)
  if choice == 5:
    print(you + remainder_)
    print(numchoice)
  if choice == 4 :
    print(you + divide_)
    print(numchoice)
  elif choice == 3:
    print(you + multiply_)
    print(numchoice)
  elif choice == 2:
    print(you + subtract_)
    print(numchoice)
  elif choice == 1:
    print(you + add_)
    print(numchoice)
    
  num1 = int(input())
  print("You have chosen " + str(num1) + ", Now chose your second number")
  num2 = int(input())
  print("Your two numbers are " + str(num1) + " and " + str(num2))
  if choice == 1:
    add(num1, num2)
  elif choice == 2:
    subtract(num1, num2)
  elif choice == 3:
    multiply(num1, num2)
  elif choice == 4:
    divide(num1, num2)
  elif choice == 5:
    remainder(num1, num2)
  elif choice == 6:
    exponent(num1, num2)
  
def r():
  print("Would you like to do another calculation")
  print("Yes or No")
  r1 = input()
  r1 = r1.capitalize()
  if r1 == 'Yes':
    main()
    return(True)
  elif r1 == 'No':
    print("Thanks for using my calculator")
    return(False)
  else:
    print("Please type yes or no")
    r()
main()
while c == True:
  c = r()
  if (c != True):
    break