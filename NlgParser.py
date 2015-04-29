import time
import math
import random
from collections import defaultdict

class NlgParser:

	def __init__(self):
		self.X = 'I '
		self.grammer = []
		self.pos = ''
		self.exclusion = ['a', 'for', 'in', 'was', 'the', 'my']
		self.preps = ['who','what','when','where','how']
		self.verbs = ['am','is','did','do','fell','see','has','are']
		self.subjects = ['me','I', 'apple', 'ball', 'health pack', 'bomb', 'brick', 'gone', 'here','pagi guy', 'right hand','left hand']
	# def verb(action):
		# for verb in verbs:
			# if verb is action:
				# tense(verb, X, Y, time)
			# else
				# verbs.append(action)
				
	# def noun(X):
		# if X is not in subjects:
			# subjects.append(X)
	
	# def tense(time):
		
	
	def parseCommand(self, command):
		self.X = 'I'
		subject = ' nothing'
		verb = ' see'
		if 'findObj' in command:
			str = command.split(',')
			print str
			for word in str:
				for w in self.subjects:
					if word == w:
						subject =  ' ' + word
			print self.X + verb + subject