# ***************************************
# Weekend Project Series
# Julia Di
# Mad Libs Generator
# February 5, 2015
# ***************************************

def madlibtemplate(*args):
	"""Empty template for the madlib."""
	print("The sky looks", *args[0], "so you and ", *args[1], "decide to go for a walk. ")

def words():
	wordlist = []
	wordlist.append(raw_input("Type an adjective: "))
	wordlist.append(raw_input("Type a name that isn't your own: "))

madlibtemplate(wordlist)