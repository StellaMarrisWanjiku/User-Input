# Ask the user for their name in a variable called Name.
name = input("What is your name? ")
# Ask the user for their Age in a variable called Age
Age = input("How old are you Age? ")
# Ask the user for their location in a varible called location
Location = input("Where do you live? ")
#personalized message using the user's name, age, and location.

print("Hello {}, you are {} years old and live in {}.".format(name, Age, Location))