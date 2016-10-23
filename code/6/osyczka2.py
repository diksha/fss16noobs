from __future__ import division
import sys
from model import Model
from decision import Decision
sys.dont_write_bytecode = True

class Osyczka2(Model):
	def __init__(self):
		self.name = "Osyczka"
		objectives = [objectiveOne, objectiveTwo]
		constraints = [constraintOne, constraintTwo, constraintThree, constraintFour, constraintFive, constraintSix]
		decisions = [Decision(0,10), Decision(0,10), Decision(1,5), Decision(0,6), Decision(1,5), Decision(0,10)]
		Model.__init__(self, objectives, constraints, decisions)

def objectiveOne(x):
	f1 = -(25*(x[0]-2)**2 + (x[1]-2)**2 + ((x[2]-1)*(x[3]-4))**2 + (x[4]-1)**2)
	return f1
def objectiveTwo(x):
	f2 = x[0]**2 + x[1]**2 + x[2]**2 + x[3]**2 + x[4]**2
	return f2
def constraintOne(x):
	return 0 <= x[0] + x[1] - 2
def constraintTwo(x):
	return 0 <= 6 - x[0] - x[1]
def constraintThree(x):
	return 0 <= 2 - x[1] + x[0]
def constraintFour(x):
	return  0 <= 2 - x[0] + 3*x[1]
def constraintFive(x):
	return 0 <= 4 - (x[2] - 3)**2  - x[3]
def constraintSix(x):
	return 0 <= (x[4] - 3)**3 + x[5] - 4
