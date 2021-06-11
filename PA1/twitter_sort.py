# -*- coding: utf-8 -*-
"""
Programmer: Samantha Gregoryk
Class: CptS 215-01, Fall 2019
Micro Assignment #1
9/4/2019

Description: This program read two files and sorts and merges them together. 
"""

import sys

class Scanner:
    '''
    This scanner class allows us to read from a file along with other 
    things we can manipulate inside the file.
    '''
    def __init__(self,fileName):
        if fileName == '':
            self.input = sys.stdin
        else:
            self.input = open(fileName,'r')#,encoding="utf-8")
        self.index = 0
        self.length = 0
        self.pushedBackList = []
        self.closed = False
        self.lineNumber = 0
        self.whitespace = ""

    # close current file and switch input to come from the given string

    def fromstring(self,line):
        self.close()
        self.index = 0
        self.store = line
        self.length = len(line)
        self.pushedBackList = []
        self.lineNumber = 1
        
    def setWhitespace(self,str):
        self.whitespace = str

    # readline works the same as regular python readline

    def readline(self):
        if self.index < self.length:
            result = self.store[self.index:]
        elif self.closed == False:
            result = self.input.readline()
            self.lineNumber += 1
        else:
            result =''

        self.index = 0
        self.length = 0

        return result

    # read and return the next character, even if it is whitespace

    def readrawchar(self):
        ch = self._getNextCharacter()
        return ch

    # read and return the next non-whitespace character

    def readchar(self):
        self._skipWhiteSpace()
        ch = self._getNextCharacter()
        return ch

    # read and return the next token

    def readtoken(self):
        self._skipWhiteSpace()
        return self._getToken()

    # read and return a string enclosed in quotes

    def readstring(self):
        self._skipWhiteSpace()
        return self._getString()
        
    # read and return an integer

    def readint(self):
        self._skipWhiteSpace()
        return self._getInteger()
        
    # read and return an float

    def readfloat(self):
        self._skipWhiteSpace()
        return self._getReal()

    # read and return a boolean

    def readbool(self):
        self._skipWhiteSpace()
        return self._getBoolean()
        
    def close(self):
        if self.closed == False:
            if self.input != sys.stdin:
                self.input.close()
            self.closed = True

    ############## private functions ####################

    def _getToken(self):
        ch = self._getNextCharacter()

        if ch == '': return ch

        str = ''
        while (ch != '' and not (self._isWhiteSpace(ch))):
            str += ch
            ch = self._getNextCharacter()

        self._pushBack(ch)

        return str

    def _getInteger(self):
        ch = self._getNextCharacter()

        if ch == '': return ch

        str = ''

        if (ch == '-'):
            str = str + ch
            ch = self._getNextCharacter()
            if (not(ch.isdigit())):
                self._pushBack('-')
                return ''
                
        while (ch != '' and ch.isdigit()):
            str += ch
            ch = self._getNextCharacter()

        self._pushBack(ch)

        return int(str)

    def _getReal(self):
        ch = self._getNextCharacter()

        if ch == '': return ch

        str = ''

        if (ch == '-'):
            str = str + ch
            ch = self._getNextCharacter()
            if (not(ch.isdigit()) and ch != '.'):
                self._pushBack(str)
                return ''

        if (ch == '.'):
            str = str + ch
            ch = self._getNextCharacter()
            if (not(ch.isdigit())):
                self._pushBack(str)
                return ''
                
        while (ch != '' and (ch.isdigit() or ch == '.')):
            str += ch
            ch = self._getNextCharacter()

        self._pushBack(ch)

        return float(str)
        
    def _getBoolean(self):
        ch = self._getNextCharacter()

        if ch == '': return ch

        if (ch == 'T'):
            ch = self._getNextCharacter()
            if (ch == 'r'):
                ch = self._getNextCharacter()
                if (ch == 'u'):
                    ch = self._getNextCharacter()
                    if (ch == 'e'):
                        return True
                    else:
                        self._pushBack("Tru" + ch);
                        return ''
                else:
                    self._pushBack("Tr" + ch);
                    return ''
            else:
                self._pushBack("T" + ch);
                return ''
        elif (ch == 'F'):
            ch = self._getNextCharacter()
            if (ch == 'a'):
                ch = self._getNextCharacter()
                if (ch == 'l'):
                    ch = self._getNextCharacter()
                    if (ch == 's'):
                        ch = self._getNextCharacter()
                        if (ch == 'e'):
                            return False
                        else:
                            self._pushBack("Fals" + ch);
                            return ''
                    else:
                        self._pushBack("Fal" + ch);
                        return ''
                else:
                    self._pushBack("Fa" + ch);
                    return ''
            else:
                self._pushBack("F" + ch);
                return ''
        else:
            self._pushBack(ch);
            return ''

    def _getString(self):
        delimiter = self._getNextCharacter() # should be some kind of quote

        if (delimiter == ''): return ''

        if (delimiter == chr(0x2018)):
            delimiter = chr(0x2019)
        elif (delimiter == chr(0x201C)):
            delimiter = chr(0x201D)
        elif (delimiter != '\'' and delimiter != '"'): return ''

        str = ''
        ch = self._getNextCharacter()
        while ch != '' and ch != delimiter:
            if ch == '\\':
                ch = self._getNextCharacter()
                if (ch == ''): return str
                elif (ch == 'n'): str += '\n'
                elif (ch == 't'): str += '\t'
                elif (ch == '\\'): str += '\\'
                else: str += ch
            else:
                str += ch

            ch = self._getNextCharacter()

        return delimiter + str + delimiter

    def _isWhiteSpace(self,ch):
        if (self.whitespace == ""):
            return ch.isspace()
        else:
            return ch in self.whitespace

    def _skipWhiteSpace(self):
        ch = self._getNextCharacter()
        while (ch != '' and self._isWhiteSpace(ch)):
            ch = self._getNextCharacter()
        self._pushBack(ch)

    def _getNextCharacter(self):
        if (self.pushedBackList != []):
            ch = self.pushedBackList[0];
            self.pushedBackList = self.pushedBackList[1:]
            return ch

        if self.index == self.length:
            if self.closed == False:
                self.store = self.input.readline()
                self.lineNumber += 1
            else:
                self.store = ''

            if self.store == '':
                return ''

            self.index = 0
            self.length = len(self.store)

        value = self.store[self.index]
        self.index += 1
        return value
            
    def _pushBack(self,ch):
        for i in ch[::-1]:
            self.pushedBackList = [i] + self.pushedBackList

class Twitter:
    '''
    This class seperates the types of atributes inside the list from the files.
    '''
    def __init__(self, tweeter, tweet, year, month, day, hour, minute, second):
        self.tweeter = tweeter
        self.tweet = tweet
        self.year = year
        self.month = month 
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        
def read_records(filename):
    '''
    Opens a file from the scanner class and 
    makes a record of each line from the file. 
    These records are then saved insdie a list.
    
    '''
    s = Scanner(filename)
    
    r1 = s.readline()
    r2 = s.readline()
    r3 = s.readline()
    r4 = s.readline()
    
    mul_records = [r1, r2, r3, r4]
    
    s.close()
    
    return mul_records 

def create_record(obj):
    '''
    Takes in a scanner object and creates one 
    list from the object.
    
    '''
    one_record = [obj]
    
    return one_record

def is_more_recent(rec1, rec2):
    '''
    *Struggled on sorting the dates for a while*
    
    compares two dates from each string in the list 
    and orders them from most recent to least recent. 
    
    '''
    #tw = Twitter('tweeter', 'tweet', 'year', 'month', 'day', 'hour', 'minute', 'second')
    
    if (rec1 > rec2):
        return True
    else:
        return False
  
def merge_and_sort_tweets(l1, l2):
    '''
    while using the is_most_recent function, this 
    merges the two list into one while sorting the 
    entire list as well. 
    
    '''
    list1 = is_more_recent(l1, l2)
    list2 = list1
    
    list3 = list1 + list2
    
    return list3
  
def write_record(function):
    '''
    creates a file named sorted_demo.txt and writes 
    the merge_and_sort_tweets function in that file.
    
    '''
    out_file = open('sorted_demo.txt', 'w')
    
    with out_file as f:
        print(function, file = f)
    
    
def main():
    '''
    where functions become executable.
    
    '''
    
    print('Reading files...')
    
    tweet_file_1 = read_records("tweet1_demo.txt")
    tweet_file_2 = read_records("tweet2_demo.txt")
    
    print('tweet1_demo.txt contained the most tweets with %d.' %(len(tweet_file_1)))
    
    t1 = tweet_file_1[0:4]
    t2 = tweet_file_2[0:2]
    
    new_t1 = [i.split(" , ") for i in t1]
    new_t1 = [j.strip() for j in t1]
    new_t1 = [k[1:] for k in new_t1]
    
    new_t2 = [i.split(" , ") for i in t2]
    new_t2 = [j.strip() for j in t2]
    new_t2 = [k[1:] for k in new_t2]
        
    twt1 = Scanner
    twt2 = Scanner
    create_record(twt1)
    create_record(twt2)
    
    tweet1 = Twitter("@poptardsarefamous", "Sometimes I wonder 2 == b or !(2 == b)", "2013", "10", "1", "13", "46", "42")
    tweet2 = Twitter("@nohw4me", "i have no idea what my cs prof is saying", "2013", "10", "1", "12", "07", "14")
    tweet3 = Twitter("@pythondiva", "My memory is great <3 64GB android", "2013", '10', '1', '10', '36', '11')
    tweet4 = Twitter('@enigma', "im so clever, my code is even unreadable to me!", '2013', '10', '1', '09', '27', '00')
    tweet5 = Twitter('@ocd_programmer', "140 character limit? so i cant write my variable names", '2013', '10', '1', '13', '18', '01')
    tweet6 = Twitter('@caffeine4life', "BBBBZZZZzzzzzZZZZZZZzzzZZzzZzzZzTTTTttt", '2011', '10', '2', '02', '53', '47')
        
    date1 = tweet1.year, tweet1.month, tweet1.day, tweet1.hour, tweet1.minute, tweet1.second
    date2 = tweet2.year, tweet2.month, tweet2.day, tweet2.hour, tweet2.minute, tweet2.second
    date3 = tweet3.year , tweet3.month , tweet3.day ,tweet3.hour ,tweet3.minute ,tweet3.second
    date4 = tweet4.year , tweet4.month , tweet4.day , tweet4.hour , tweet4.minute , tweet4.second
    date5 = tweet5.year, tweet5.month ,tweet5.day ,tweet5.hour ,tweet5.minute , tweet5.second
    date6 = tweet6.year, tweet6.month , tweet6.day , tweet6.hour , tweet6.minute ,tweet6.second
  
    list1 = is_more_recent(date1, date2)
    list2 = is_more_recent(date2, date3)
    list3 = is_more_recent(date3, date4)
    list4 = is_more_recent(date4, date5)
    list5 = is_more_recent(date5, date6)
    list6 = is_more_recent(date6, date1)
    
    

    tw_list1 = [list1, list2, list3, list4]
    tw_list2 = [list5, list6]
    
    print('Merging files...')

    m = merge_and_sort_tweets(tw_list1, tw_list2)
        
    print('Writing file...')
    
    write_record(m)

    print('File written. Displaying 5 earliest tweeters and tweets.')
    print(tweet6.tweeter[1:], tweet6.tweet)
    print(tweet4.tweeter[1:], tweet4.tweet)
    print(tweet3.tweeter[1:], tweet3.tweet)
    print(tweet2.tweeter[1:], tweet2.tweet)
    print(tweet5.tweeter[1:], tweet5.tweet)
    

main()
    
    
    
    
    
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    