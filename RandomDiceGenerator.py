# ************************************************
# Weekend Project #1
# Rolling Dice Simulator
# Julia Di
# Python, February 5, 2015
# ************************************************

import random

def dice():
	"""Random dice generator quick project."""

	print("Hello.")

	again = "Yes"

	while(again == "Yes"):
		number = int(random.randrange(1,7))
		print("You have rolled", number, "as your number.")
		again = raw_input("Would you like to roll again? (Yes or No) ")

dice()