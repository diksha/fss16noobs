from __future__ import division
import sys,random
sys.dont_write_bytecode=True

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return ("{name: "+self.name+", age: "+str(self.age)+"}")
    
    def __lt__(self, e):
        return self.age < e.age

print Employee("Alex", 34)

employees = [Employee("Alex", 32), Employee("Bob", 23), Employee("Jane", 27)]

print sorted(employees)