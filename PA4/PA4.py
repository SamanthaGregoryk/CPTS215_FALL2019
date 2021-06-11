"""
Programmer: Samantha Gregoryk
Class: CptS 215-01, Fall 2019
Programming Assignment #4
10/20/2019

Description: This program predicts the next word in a sentence
 from the naturual language processor. It is already looking for 
 the next frequently used words based on words used in the past. 
 Hash maps are also involved in this program in order to making 
 the predictions useful for the user to use. 
"""

import random
import string
import timeit
import numpy as np

class HashTable:
    '''
    From Lecture 8-2 curtosey of Gina Sprint. 
    Data structure implemented as a class to 
    store data usuing hashing. It computes 
    an index into an array. Then, that the 
    element in the array is searched for. 
    Hashing saves time and is great for 
    predictions. 
    '''
    def __init__(self, size):
        '''
        Takes in size and creates an array 
        that is then multiplied by the size. 
        '''
        self.size = size
        self.slots = [None] * self.size
        
    def put(self, item):
        '''
        Place an item in the hash table.
        Return slot number if successful, -1 
        otherwise (no available slots, table
        is full)
        '''
        hashvalue = self.hashfunction(item)
        slot_placed = -1
        if self.slots[hashvalue] == None or self.slots[hashvalue] == item: # empty slot or slot contains item already
            self.slots[hashvalue] = item
            slot_placed = hashvalue
        else:
            nextslot = self.rehash(hashvalue)
            while self.slots[nextslot] != None and self.slots[nextslot] != item: 
                nextslot = self.rehash(nextslot)
                if nextslot == hashvalue: # we have done a full circle through the hash table
                    # no available slots
                    return slot_placed
    
            self.slots[nextslot] = item
            slot_placed = nextslot
        return slot_placed
        
    def get(self, item):
        '''
        Returns slot position if item in hashtable,
        -1 otherwise.
        '''
        startslot = self.hashfunction(item)
        
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == item:
                found = True
            else:
                position=self.rehash(position)
                if position == startslot:
                    stop = True
        if found:
            return position
        return -1
    
    def remove(self, item):
        '''
        Removes item.
        Returns slot position if item in hashtable, 
        -1 otherwise.
        '''
        startslot = self.hashfunction(item)
        
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == item:
                found = True
                self.slots[position] = None
            else:
                position=self.rehash(position)
                if position == startslot:
                    stop = True
        if found:
            return position
        return -1
    
    def hashfunction(self, item):
        '''
        Remainder method
        '''
        return item % self.size
    
    def rehash(self, oldhash):
        '''
        Plus 1 rehash for linear probing
        '''
        return (oldhash + 1) % self.size
    
class Map(HashTable):
    '''
    From Lecture 8-2 curtosey of Gina Sprint. 
    This Map class is an unordered collection of key 
    value pairs that is inherited from the HashTable 
    class. They have unique key values and in order 
    to look up a given key value, you must use the 
    hashtable and an arrary to store the values.
    '''
    def __init__(self, size):
       '''
       Takes in the size of the HashTable and stores 
       them in an array that is multiplied by the size 
       given. 
       '''
       super().__init__(size)
       self.values = [None] * self.size # holds values
        
    def __str__(self):
        '''
        Returns a string representation of the object. 
        '''
        s = ""
        for slot, key in enumerate(self.slots):
            value = self.values[slot]
            s += str(key) + ":" + str(value) + ", "
        return s
    
    def __len__(self):
        '''
        Return the number of key-value pairs stored 
        in the map.
        '''
        count = 0
        for item in self.slots:
            if item is not None:
                count += 1
        return count
    
    def __getitem__(self, key):
        '''
        Returns the value for the specified key.
        '''
        return self.get(key)
    
    def __setitem__(self, key, data):
        '''
        Appends the data.
        '''
        self.put(key,data)
        
    def __delitem__(self, key):
        '''
        Removes the data.
        '''
        self.remove(key)
        
    def __contains__(self, key):
        '''
        Returns the value for the specified key 
        if it is not equal to -1.

        '''
        return self.get(key) != -1
    
            
    def put(self, key, value):
        '''
        Add a new key-value pair to the map. 
        If the key is already in the map then 
        replace the old value with the new 
        value.
        '''
        slot = super().put(key)
        if slot != -1:
            self.values[slot] = value
        return -1
        
    def get(self, key):
        '''
        
        '''
        slot = super().get(key)
        if slot != -1:
            return self.values[slot]
        return -1
    
    def remove(self, key):
        '''
        Removes key:value pair.
        Returns slot location if item in 
        hashtable, -1 otherwise
        '''
        slot = super().remove(key)
        if slot != -1:
            self.values[slot] = None
        return slot
    
    def hashfunction(self, item):
        '''
        Remainder method
        '''
        key = 0
        for x in item:
            key += ord(x)
        return key % self.size
    
    def chaining(self, key):
        slot = self.hashfunction(key)
        if key in self.slots[slot]:
            return -1
        else:
            self.slots[slot].append(key)
            return slot

class DictEntry():
    '''
    This class represents a word and its 
    unigram probability.
    '''
    def __init__(self, word, prob): # string, float
        '''
        Creates a new entry given a word 
        and probability.
        '''
        self.word = word
        self.prob = prob
    
    def get_word(self): # returns string
        '''
        Returns the word given. 
        '''
        return self.word
    
    def get_prob(self): # returns float
        '''
        Returns the probability given.
        '''
        return self.prob
    
    # does this word match the given pattern?
    def match_pattern(self, pattern): # returns string             
        '''
        Checks to see if the word matches 
        the pattern that was given by the 
        user. 
        '''
        my_list = []
        match = filter(lambda x: pattern in x, my_list) #filters the elements being iterated in the list to be true or not. 
        return match

class WordPredictor():
    '''
    This a class always learning the predictions 
    of the next word to give to the user. This 
    is based on the training data that is given. 
    '''
    
    # train the unigram model on all the words in the given file
    def train(self, training_file): # string                     
        '''
        Trains (learns) the unigram model on all 
        words given on the file that was inputted. 
        '''
        word_to_count = Map()
        
        file = open(training_file, 'a')
        for f in file:
            if f is open:
                word_to_count.values += 1
                f.strip()
                f.lower()
                f.close()
                return True
            else:
                print('Could not open training file: %s' %(training_file))
                return False


    # train on just a single word
    def train_word(self, word): # string                                 
        '''
        Trains (learns) from just an individual 
        word. 
        '''
        return [word]
        
    
    # get the number of total words we've trained on
    def get_training_count(self, file, word): # returns integer                   
        '''
        Returns the total number of words that were 
        trained from the unigram and individual words.
        '''
        total = len(self.train(file)) + len(self.train_word(word))
        return total
    
    # get the number of times we've seen this word (0 if never)
    def get_word_count(self, word): # string. returns integer           
        '''
        Returns the number of times the word was seen.
        '''
        count = 0
        arr = []
        
        for i in range(len(arr)): 
            if arr[i:i + len(word)] == word:
                count += 1
            else:
                return 0
        return count
    
    '''
    Loop over all possible (key, value) pairs in word_to_count.
    
    For each pair: Calculate the probability of that word given 
    its count and the number of training words. Create a new DictEntry
    object representing this word and its probability.
    
    For each pair: Loop over all possible prefixes of the word. That 
    is from a prefix of only the first letter to a "prefix" that is the 
    entire word.
    
        For each prefix, if the current key (word) has a probability strictly 
        greater than what is currently stored for that prefix, replace the 
        old value (a DictEntry object) with the new object.
    '''
    
    # recompute the word probabilities and prefix mapping
    def build(self):                                                  
        '''
        Once training data is added, this method must
        be called so the class can recompute the most
        likely word for all possible prefixes
        '''
        word_to_count = Map()
        
        for key, value in word_to_count:
            probability(self.get_word_count(value), self.get_training_count())
            
            nd = DictEntry()
            
            for pf in nd.get_word():
                mn = min(pf)
                mx = max(pf)
                for v, k in enumerate(mn):
                    if k != mx[v]:
                        return mn[:v]
            return mn
            
    # return the most likely DictEntry object given a word prefix
    def get_best(self, prefix, a): # string. returns DictEntry             
        '''
        Returns the most likely object from the 
        DictEntry class that is given a word prefix. 
        '''
        de = DictEntry()
        count = {}
        
        for pf in de:
            if pf in count:
                count[pf] +=1
                return de
            else:
                count[pf] = 1
                return de
            
def probability(a, b):
    '''
    Probability of a given b 
    '''
    de = DictEntry()
    
    prob = (de.get_prob(a) * de.get_prob(b)) / de.get_prob(b)
    
    return prob
    
def random_load_test(wp):
    '''
    
    '''
    print("random load test: ")
    VALID = string.ascii_lowercase
    TEST_NUM = 10000000
    hits = 0
    for i in range(TEST_NUM):
        prefix = ""
        for j in range(0, random.randint(1, 6), 1):
            prefix += VALID[random.randrange(0, len(VALID))]
        de = wp.get_best(prefix)
        if de.get_word() != "null":
            hits += 1
            
    print("Hit = %.2f%%" %(hits / TEST_NUM * 100))

def main():
    '''
    From keyboard_test.py curtosey of Gina Sprint. 
    Execution of all functions and methods. 
    '''
        
    # train a model on the first bit of Moby Dick
    wp = WordPredictor()
    print("bad1 = %s" %(wp.get_best("the")))
    wp.train("moby_start.txt")
    print("training words = %d" %(wp.get_training_count()))
    
    # try and crash things on bad input
    print("bad2 = %s" %(wp.get_best("the")))
    wp.train("thisfiledoesnotexist.txt")
    print("training words = %d\n" %(wp.get_training_count()))
    
    words = ["the", "me", "zebra", "ishmael", "savage"]
    for word in words:
        print("count, %s = %d" %(word, wp.get_word_count(word)))
    wp.train("moby_end.txt")
    print()
    # check the counts again after training on the end of the book
    for word in words:
        print("count, %s = %d" %(word, wp.get_word_count(word)))
    print()
    
    # Get the object ready to start looking things up
    wp.build()
    
    # do some prefix loopups
    test = ["a", "ab", "b", "be", "t", "th", "archang"]
    for prefix in test:
        print("%s -> %s\t\t\t%.6f" %(prefix, wp.get_best(prefix), wp.get_best(prefix).get_prob()))
    print("training words = %d\n" %(wp.get_training_count()))
    
    # add two individual words to the training data
    wp.train_word("beefeater")
    wp.train_word("BEEFEATER!")
    wp.train_word("Pneumonoultramicroscopicsilicovolcanoconiosis")
 
    # The change should have no effect for prefix lookup until we build()
    print("before, b -> %s\t\t%.6f" %(wp.get_best("b"),  wp.get_best("b").get_prob()))
    print("before, pn -> %s\t\t%.6f" %(wp.get_best("pn"),  wp.get_best("pn").get_prob()))
    wp.build()
    print("after, b -> %s\t\t%.6f" %(wp.get_best("b"),  wp.get_best("b").get_prob()))
    print("after, pn -> %s\t\t%.6f" %(wp.get_best("pn"),  wp.get_best("pn").get_prob()))
    print("training words = %d\n" %(wp.get_training_count()))
    
    # test out training on a big file, timing the training as well
    start = timeit.default_timer()
    wp.train("mobydick.txt")
    wp.build()
    for prefix in test:
        print("%s -> %s\t\t\t%.6f" %(prefix, wp.get_best(prefix), wp.get_best(prefix).get_prob()))
    print("training words = %d\n" %(wp.get_training_count()))
    stop = timeit.default_timer()
    elapsed = (stop - start)
    print("elapsed (s): %.6f" %(elapsed))
    
    # test lookup using random prefixes between 1-6 characters
    start = timeit.default_timer()
    random_load_test(wp)
    stop = timeit.default_timer()
    elapsed = (stop - start)
    print("elapsed (s): %.6f" %(elapsed))
    
main()