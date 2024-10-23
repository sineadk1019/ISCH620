# -*- coding: utf-8 -*-
'''
Name: Sinead Keane
Due Date: 11/10/2023
Class: ISCH 620
Title: Assignment #4
Contact information: 857-294-2616; sinead.keane001@gmail.com


This is REV2
'''

import random
from datetime import datetime

def user_argument():
    user_input = input('Please choose Ascending or Descending: ')
    return user_input
    

#This function randomly generates a list. I have modified with the version in 
# the professors example because my original attempt wasn't random.
def random_gen(seed_val):
    list_a = []
    random.seed(seed_val)  # Set the seed to ensure reproducibility
    while len(list_a) <600:
        val = random.randrange(1, 1200)
        if val not in list_a:
            list_a.append(val)
    return list_a

#assign the function to a variable to use in the sorting functions. 
list_a = random_gen(600)
    
#print(list_a); used this to check the list.

#function 1 = Sorting this way is exhaustive. Each item is reviewed one by one 
#and sorted accordingly.
def function_sorted(user_input):
    list_sorted = list_a.copy()
    start_time = datetime.now()
    for x in range(len(list_sorted)):
        for y in range(x+1, len(list_sorted)):
            if list_sorted[x] > list_sorted[y]:
                list_sorted[x], list_sorted[y] = list_sorted[y], list_sorted[x]
    # print(list_sorted); used this to check the list sort
    sorted_greatest = list_sorted[::-1]
    end_time = datetime.now()
    time_cost = end_time - start_time
    if user_input.lower() == 'ascending': 
        print(f"Here's the list from least to greatest: \n{list_sorted}\
  \n \nThis took {time_cost} seconds to sort a 600 item list.")
    elif user_input.lower() == 'descending':
        print("Here's the list from greatest to least:\n{sorted_greatest}\n\n \
This took {time_cost} seconds to sort a 600 item list.")
    else: 
        print("Sorry that isn't an option.")

#Merge Sorted: this list uses the divide and conquer method to sort the list
#it results in significantly less time to sort. 
def function_sort_2(user_input):
    start_time = datetime.now()
    full_list = list_a.copy()
    '''The merge function will be used in the merge_sort to compare the values by
    dividing into two lists.'''
    def merge(list_1, list_2, compare):
        result= []
        i,j = 0,0
        while i< len(list_1) and j < len(list_2):
            if compare(list_1[i], list_2[j]):
                result.append(list_1[i])
                i+=1
            else:
                result.append(list_2[j])
                j+=1 
        while (i<len(list_1)):
            result.append(list_1[i])
            i+=1
        while (j< len(list_2)):
            result.append(list_2[j])
            j+=1
        return result
    ''' This portion will then use the  methods in the merge function to finalize
     the comparison and produce a nice sorted, combined list.'''
    def merge_sort(full_list, compare = lambda x, y: x<y):
        if len(full_list)<2:
            return full_list[:]
        else:
            middle = len(full_list)//2
            list_1 = merge_sort (full_list[:middle], compare)
            list_2 = merge_sort(full_list[middle:], compare)
            return merge(list_1, list_2, compare)
    least_great = merge_sort(full_list)
    great_least = least_great[::-1]
    end_time = datetime.now()
    time_cost = end_time - start_time
    if user_input.lower() == 'ascending': 
        print(f"Here's the merge sorted list from least to greatest: \n{least_great}\
  \n \nThis took {time_cost} seconds to sort a 600 item list.")
    elif user_input.lower() == 'descending':
        print(f"Here's the merge sorted list from greatest to least:\n{great_least}\
\n This took {time_cost} seconds to sort a 600 item list.")
    else:
        print("Sorry that's not a choice")

#main function to run all of the above in a decipherable way.
def __main__():
    user_input = user_argument()
    print()
    print("This is the first type of sort; Sorted - \n")
    function_sorted(user_input)
    print()
    print('This is the second type of sort; Merge Sorted - \n')
    function_sort_2(user_input)
    print()
    print()
    print("The first scenario is shorter but more linear, so I believe this is \
Big O(len(L)). This goes one by one and checks everything results in the worst \
case scenario of a belabored 00.012002 seconds. The second is much more complex.\
It has several loops and functions resulting in greater complexity. This does \
however, split \the sort by sorting the two lists separately then merging them \
together. This is more representative of a Big Theta(len(L)) time complexity as it cuts \
the time siginifcantly, coming in at 0:00:00.000986. that is a difference of \
.011 seconds")
__main__()  

