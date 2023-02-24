print("Good day and welcome. This is an arithmetic calculator where you will be asked to supply some inputs and an operation of your choice will be performed on that input.")

while True:
  try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multplication")
    print("4. Division")
    print("Pick an operation by selecting it's corresponding number.")
    choice = int(input("Choose an operation from the menu above: "))

    if choice < 1 or choice > 4:
        print("Please pick an operation from the list")
    else:
      if choice == 1:
          result = num1 + num2
          print(f"The sum of the two numbers is {result}")
      elif choice == 2:
          result = num1 - num2
          print(f"The difference between the two numbers is {result}")
      elif choice == 3:
          result = num1 * num2
          print(f"The product of the two numbers is {result}")
      elif choice == 4:
          result = num1/num2
          print(f"The result of the division between the two numbers is {result}")
      while True:
        choice2 = input('''Would you like to perform another operation; Y for "Yes" and N for "No": ''')
        if choice2.upper() == "Y":
          break
        elif choice2.upper() == "N":
          print("Goodbye for now!")
          exit()
        else:
          print("Pleas pick Y or N")          
  except ValueError:
     print("Please enter your input again, only numbers are accepted, decimals and letters are not accepted.")

# Code Explanation
# First, a welcome message which contains a greeting and the description of the program is displayed to the user.
# A while loop with it's condition set to True is the created and a try statement to help avoid errors is written inside the body of the while loop.
# A prompt asking the user for integer input is then displayed and a menu containing the list of operations that can be performed is also displayed to the user.
# A prompt that allows the user to choose the operation they will like to perform is printed out, and conditional statements for each operation is executed.
# For example, if the user, chooses 1 which is addition, the code under the body of the conditionl statement that controls addition is executed.
# After the conditional statements, another while loop is created with it's condition also set to True and a prompt that asks the user if they would like to perform another operation is then printed out to the screen.
# If the user chooses to perform another operation, that is choose "Y",the new loop is broken and the program restarts whereas if the user chooses not to continue that is "N", a message is printed out to the user, and the program ends.
# If the user enter neither Y or N, a message is displayed to the user and the prompt asking the user to input Y or N is displayed until the user chooses to input one of them.
# To avoid errors, an except ValueError statement is used and a message is printed out to the user if they enter an invalid input.
#      