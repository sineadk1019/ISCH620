# -*- coding: utf-8 -*-
'''
Name: Sinead Keane
Due Date: 10/27/2023
Class: ISCH 620
Title: Assignment #4
Contact information: 857-294-2616; sinead.keane001@gmail.com


This is REV1
'''

import random
#from datetime import datetime ; to do time complexity analysis

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
#print(list_a) #checking list to see against sort. 

#function 1 = sort
def function_sorted():#will put list a in here
    #list_sorted = []
    #attempt to create new sorted list V1
    # for x in range(len(list_a)):
    #     for y in range(len(list_a)):
    #         if list[x] >= list[y]:
    #             list_sorted.append(i)
    #             ctr+=1
    #             list_sorted[x], list_sorted[y] = list_sorted[y], list_sorted[x]
    #         else:
                # print(list_sorted)
    #sorted_least = sorted_greatest[::-1]
    #include run time. len(list_a) * ctr?
    #time = input time it took to run this using the ctr value to multiply by.
    print("sorted result will be here, run time will be here")
        
def function_merge_sorted(): #
      print("sorted result #2 will be here, run time #2 will be here")

#main function will eventually have list_a as it's argument
def main():
    function_sorted()
    function_merge_sorted()
    print("time complexity details")
    
main()

