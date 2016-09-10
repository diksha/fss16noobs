"""

This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from Card import *


class FrequencyDict(dict):
    """Count the number of item x"""

    def count(self, x):
        self[x] = self.get(x, 0) + 1
        if self[x] == 0:
            del self[x]


class PokerHand(Hand):
    """Represents a poker hand."""

    all_labels = ['straightflush', 'fourkind', 'fullhouse', 'flush',
                  'straight', 'threekind', 'twopair', 'pair']

    def find_frequency(self):
        """Calculates frequency for suits and ranks
        """
        self.suits = FrequencyDict()
        self.ranks = FrequencyDict()
        
        for c in self.cards:
            self.suits.count(c.suit)
            self.ranks.count(c.rank)

        self.sets = self.ranks.values()
        self.sets.sort(reverse=True)
        
    def has_same_rank_set(self, *lst):
        """Checks whether self.sets contains sets that are
        at least as big as the requirements in t.

        t: list of int
        """
        i = 0
        for val in lst:
            if self.sets[i] >= val:
                i=i+1
            else:
                return False
        return True

    def has_pair(self):
        """Checks whether this hand has a pair."""
        return self.has_same_rank_set(2)
        
    def has_twopair(self):
        """This hand has two pair."""
        return self.has_same_rank_set(2, 2)
        
    def has_threekind(self):
        """This hand has three of a kind."""
        return self.has_same_rank_set(3)
        
    def has_fourkind(self):
        """This hand has four of a kind."""
        return self.has_same_rank_set(4)

    def has_fullhouse(self):
        """This hand has a full house."""
        return self.has_same_rank_set(3, 2)

    def has_flush(self):
        """This hand has a flush."""
        for val in self.suits.values():
            if val >= 5:
                return True
	return False

    def has_straight(self):
        """This hand has a straight."""
        ranks = self.ranks.copy()
        ranks[14] = ranks.get(1, 0)

        count = 0
        for i in xrange(1, 15):
            if ranks.get(i, 0):
                count += 1
                if count == 5: return True
            else:
                count = 0
        return False

    
    def has_straightflush(self):
        """This hand has a straight flush.
        """
        s = list()
        for c in self.cards:
            s.append((c.rank, c.suit))
            if c.rank == 1:
                s.append((14, c.suit))
        s.sort()
        for suit in xrange(4):
            count = 0
            for rank in xrange(1, 15):
                if (rank, suit) in s:
                    count += 1
                    if count == 5: return True
                else:
                    count = 0
        return False
                
    
    def findLabel(self):
        """Finds the label for this hand.
        """
        self.find_frequency()

        for label in PokerHand.all_labels:
            f = getattr(self, 'has_' + label)
            if f():
                return label;
        return 'highcard'



if __name__ == '__main__':
    #random.seed(1)
    # make a deck
    labelCount = {'straightflush':0, 'fourkind':0, 'fullhouse':0, 'flush':0,
                  'straight':0, 'threekind':0, 'twopair':0, 'pair':0, 'highcard':0}
    # deal the cards and classify the hands
    for j in xrange(1000) :
        deck = Deck()
        deck.shuffle()
        for i in xrange(7):
            hand = PokerHand()
            deck.move_cards(hand, 7)
            hand.sort()
            labelCount[hand.findLabel()]+=1
    
    for key in labelCount:
        print "Probability of ", key, " ", labelCount[key]/7000.0