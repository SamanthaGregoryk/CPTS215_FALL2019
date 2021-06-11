'''
Programmer: Samantha Gregoryk     
Class: CptS 215-01, Fall 2019     
Programming Assignment #6   
11/6/2019   
 
Description: Once the user has inputted their actor
 or actress of choice, the game will find the 
 correlating bacon number they have. The bacon number
 is determined by how many movies they have been in
 with costars who circle back to Kevin Bacon.
'''

def largest_finite_bacon_number():
    '''
    Finds the largest number in
    the dataset and returns it.
    '''
    a_dict = {int(d[0]) for d in actors}
    largest = max(a_dict)
    return largest

def avg_bacon_number():
    '''
    Finds the average bacon number
    by adding up all them and 
    dividing by how many are in the
    dataset. 
    '''
    a_dict = {int(d[0]) for d in actors}
    avg = sum(a_dict) / len(a_dict)
    return int(avg)