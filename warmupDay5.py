# File name: warmupDay5.py
myName = "Anastasia"
userGuess = input("Try to guess my name.")

while userGuess != myName:
    print("Sorry, that's not my name!")
    userGuess = input("Try again.")
else:
    print("Congratulations! That's my name!")
