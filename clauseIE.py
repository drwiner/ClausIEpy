
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
	"""
		1. Compute Dependency Parse (DP) for sentence
		2. Determine the set of clauses using DP
			A] simple mapping of dependency relations to clause constituents
				i] construct a clause for every subject dependency in the DP (e.g., nsubj)
				ii] all other constituents are dependants of the verb (objects, complmeents, adverbials)
			B] create synthetic clauses
				i] replace relative pronoun (e.g., "who" or "which") with antecendent (via rcmod dep)
				ii]
		3. For each clause, determine clause type
		4. Generate propositions from clauses
	"""

	nlp = loadSpacy()