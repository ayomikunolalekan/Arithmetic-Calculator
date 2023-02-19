while True:
  a = int(input("Enter a number: "))
  b = int(input("Enter a number: "))

  if a < 0 or b < 0:
    print("You can only input numbers that are greater than 0.")
  else:
    print(a+b)
    print(a-b)
    print(a*b)
    break

# Program explanation
# First, we create a while loop and set the condition to be true.
# Next, we collect some input from the user and store in variables a and b respectively.
# We then set a condition to ensure that the program only works if either of the input is greater than 0.
# If any of the input is less than 0, we print out a message for the user, else, we perform the sum, difference and product of the two numbers.

