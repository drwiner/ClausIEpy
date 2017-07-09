from subprocess import Popen, PIPE

p1 = Popen(['java', '-jar', 'clausie.jar', '-c', 'resources/clausie.conf', '-v', '-p', '-o', 'testing.txt'], stdin=PIPE)


sentence1 = b'This is a sentence\n'
sentence2 = b'She was not going to parse another sentence\n'
sentence3 = b'The man goes from point A to point B\n'
sentence4 = b'He breathes without his lungs.\n'
sents = [sentence1, sentence2, sentence3,sentence4]

for sent in sents:
	p1.stdin.write(sent)
	
p1.communicate()


clause_frame_dict = {
	'SVC': [4,6,7],
	'SV' : [1,3],
	'SVA': [1,2,12,13,22,27],
	'SVOO': [14,15],
	'SVOC': [5],
	'SVO': [26,34,1,2,8,9,10,11,33],
	'SVOA': [1,2,8,9,10,11,15,16,17,18,19,20,21,30,31,33,24,28,29,32,35]}
	
from nltk.corpus import wordnet as wn
	
clause_types = []
verb_lemmas = []
with open('testing.txt','r') as fp:
	last_line = None
	last_id = 0
	for line in fp:
		if line[0] == '#':
			last_line = line
			# print(line)
		elif line.split()[0] == last_id:
			continue
		else:
			last_id = line.split()[0]
			# This is an output, last line has clause type
			sep_line = last_line.split()
			clause_type = sep_line[2]
			#print(line.split())
			
			verb_instance = None
			for i, item in enumerate(sep_line[3:]):
				if 'V:' in item:
					verb_instance = sep_line[3+i+1]
					break
			verb_instance = verb_instance.split('@')[0]
			#print(verb_instance)
			#print(sep_line)
			#print('\n')
			#verb_lemma = line.split('\"')[3]
			
			verb_lemmas.append(verb_instance)
			clause_types.append(clause_type)
			
#sent_zip = list(it.chain.from_iterable(it.izip(sents,clause_types,verb_lemmas)))
sent_zip = zip(sents, clause_types, verb_lemmas)
for sent, ctype, vlemma in sent_zip:
	print('{} : {} : {}'.format(sent, ctype, vlemma))
	frameids = clause_frame_dict[ctype]
	for i, synset in enumerate(wn.synsets(vlemma)):
		fids = synset.frame_ids()
		interfids = list(set(frameids) & set(fids))
		if len(interfids) > 0:
			print('{}: {}'.format(i,synset.definition()))
	print('\n')
			
			
		