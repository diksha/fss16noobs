
from __future__ import division
import sys
import random
import time

class Model(object):
	def __init__(self, objectives, constraints, decisions):
		self.objectives = objectives
		self.constraints = constraints
		self.decisions = decisions

	def evaluate(self, solution):
		"""
		Calculates the score for a given solution using all objectives
		"""
		total = 0
		for objective in self.objectives:
			total = total + objective(solution)
		return total

	def ok(self, solution):
		"""
		Checks if solution is ok
		"""
		if self.constraints != None:
			for constraint in self.constraints:
				if not constraint(solution):
					return False
		return True

	def any(self):
		"""
		Generates a random solution
		"""
		valid = False
		solution = []
		while not valid:
			soln = []
			for dec in self.decisions:
				soln.append(random.randint(dec.low, dec.high))
			valid = self.ok(soln)
			if valid :
				solution = soln
		return solution
