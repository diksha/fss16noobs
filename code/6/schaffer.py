import sys
from model import Model
from decision import Decision

class Schaffer(Model):
	def __init__(self):
		self.name = "schaffer"
		objectives = [objectiveOne, objectiveTwo]
		decisions = [Decision(-10**5, 10**5)]
		Model.__init__(self, objectives, None, decisions)

def objectiveOne(solution):
	return solution[0]**2

def objectiveTwo(solution):
	return (solution[0]-2)**2
