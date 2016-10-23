import sys
import math
from model import Model
from decision import Decision

class Kursawe(Model):
	def __init__(self):
		self.name = "Kursawe"
		objectives = [objectiveOne, objectiveTwo]
		decisions = [Decision(-5,5), Decision(-5,5), Decision(-5,5)]
		Model.__init__(self, objectives, None, decisions)

def objectiveOne(s):
	total = 0
	for i in xrange(len(s)-1):
		value = -10 * math.exp((-0.2 * ((s[i])**2) + ((s[i+1])**2)))
		total += value
	return total

def objectiveTwo(s):
	a = 0.8
	b = 1
	total = 0
	for i in xrange(len(s)):
		value = (abs(s[i])**a) + (5 * math.sin((s[i])**b))
		total += value
	return total
