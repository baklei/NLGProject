import time
import math
import random
from NlgParser import NlgParser
from collections import defaultdict
from pagi_api import *

cs = connectSocket()
# cs = connectSocket('129.161.58.14')
agent = Agent(cs)
poison = False
count = 0
found = False
n = NlgParser()

while (count < 200):
	#MAIN LOOP.
	#check any new messages that were sent
	responses = getMessages(cs)
	for r in responses:
		if r != "":
			print "Message received: " + r
			n.parseCommand(r)
			
	send("findObj,apple,PD\n", cs)
	
	count += 1
	time.sleep(1)
	
closeClient()

exit()