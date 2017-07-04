
DO_PRINT = 0

def Log(message):
	if DO_PRINT:
		print(message)

def loadSpacy():
	import spacy
	print('loading SPACY english')
	nlp = spacy.load('en')
	return nlp


if __name__ == '__main__':
	# command line args (TODO)
	# steps for processing text

	nlp = loadSpacy()