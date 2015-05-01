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
		self.adj = ['some','few','many']
		self.verbs = ['am','is','did','do','fell','see','has','are']
		self.subjects = ['me','I', 'apple', 'poison jar', 'ball', 'health pack', 'bomb', 'brick', 'gone', 'here','pagi guy', 'right hand','left hand']
	# def verb(action):
		# for verb in verbs:
			# if verb is action:
				# tense(verb, X, Y, time)
			# else
				# verbs.append(action)
				
	def isPlural(count):
		if count > 1:
			return True
		return False
		
	def isCountable(amount):
		if amound > 5 or amount == -1:
			return False
		return True
		
	#"an vs a" function that checks to see if a word starts with a consonant or vowel
	def startsWithVowel(self, word):
		if word[0].lower() == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':
			return True
		return False
		
	
	def parseCommand(self, command):
		self.X = 'I'
		subject = ' nothing'
		verb = ' see'
		if 'findObj' in command:
			str = command.split(',')
			print str
			if len(str) >= 3:
				for word in str:
					for w in self.subjects:
						if word == w:
							if (self.startsWithVowel(word)):
								subject = ' an ' + w
							else:
								subject = ' a ' + w
		if 'addForce' in command:
			str = command.split(',')
				if len(str) >= 3:
					for word in str:
						if word == 'J':
							verb = ' jump'
						else:
							verb = ' move'
			print self.X + verb + subject