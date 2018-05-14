import random
import sys
try:
	repeatCount = int(sys.argv[1])
	if repeatCount is None:
		repeatCount = 5
	if 0 < repeatCount < 10:
	  articles = ['a', 'an', 'the', 'one', 'some', 'few']
	  names = ['cat', 'dog', 'man', 'woman']
	  verbs = ['sang', 'jumped', 'feels', 'search']
	  adverbs = ['loudly', 'well', 'badly']
	  i = 0
	  while i < repeatCount:
		  choosenArcticle = random.choice(articles)
		  choosenName = random.choice(names)
		  choosenVerb = random.choice(verbs)
		  choosenAddverb = random.choice(adverbs)
		  structure = random.randint(0, 1)
		  if structure == 0:
			  print(choosenArcticle + " " + choosenName + " " + choosenVerb + " " +
			      choosenAddverb)
		  else:
			  print(choosenArcticle + " " + choosenName + " " + choosenVerb)
		  i += 1
	else:
		print('Invalid')
except IndexError:
	print('Usage randomWords.py <number>')	
