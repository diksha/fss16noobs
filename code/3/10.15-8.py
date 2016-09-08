from __future__ import division
import sys,random
sys.dont_write_bytecode=True

def has_duplicates(lst):
    for i in xrange(len(lst)):
        for j in xrange(i+1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False

def birthday_paradox(num_students, num_samples):
    # Stores number of samples containing duplicates
    positive_samples = 0
    
    for _ in xrange(num_samples):
        # Generate random sample of 'num_students' students
        rand_list = [random.randint(1,365) for r in xrange(num_students)]
        positive_samples += int(has_duplicates(rand_list))
        
    print positive_samples/num_samples, "chance that 2 students have same birthday."

# Test cases
print has_duplicates([1])
print has_duplicates([1,2,1])

birthday_paradox(23, 100)