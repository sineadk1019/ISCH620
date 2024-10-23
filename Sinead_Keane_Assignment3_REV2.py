# -*- coding: utf-8 -*-
'''
Name: Sinead Keane
Due Date: 10/23/2023
Class: ISCH 620
Title: Assignment #2
Contact information: 857-294-2616; sinead.keane001@gmail.com


This is my final outcome from REV1
'''
# This program will review the contents of text file my_family.txt

'''Here I have my file call with my file error check. Which allows me to read 
a file and check if it exists.'''
def file_call(file_name):
        try:
            with open(file_name,'r'):
                print('File Existence Success! This is a file that exists.')
        except FileNotFoundError:
            print("File Not Found Error: Check the file name, this one doesn't exist.\n")
        
#This checks if the value exists in the file or returns a Value error. 
def test1_value(find_value):
    with open('my_family.txt','r') as family_doc:
        family_info= family_doc.read()
        try: 
            if str(find_value) in family_info:
                print(f'Test 1 Success! {find_value} is a value.')
            else:
                raise ValueError('Test 1 Value Error: This value does not exist.')
        except ValueError:
            print(f'Test 1 Value Error: {find_value} is not a value in this file.\n')

'''I actually did this test last because I attempted originally to use a 
Type Error in Test 1. It ended up not working right so I combined it with an
Arithmetic Error. So I actually technically have 5 tests but I wanted to make sure I had
all possible inputs for this one covered and that needed a 0 as well. '''
def test2_type(number):
    with open('my_family.txt', 'r') as family_doc:
        family_length = family_doc.read()
        try:
            x = len(family_length)-number
            if number > 0 :
                print(f'Test 2 Success! The difference in your number and the length of my document is {x}.')
            else: 
                raise ArithmeticError ("doesn't work")
        except ArithmeticError:
            print(f"Test 2 Arithmetic Error: Cannot divide by {number}.\n")
        except TypeError:
            print(f"Test 2 Type Error: {number} is a {type(number)} I need an integer or a float.")


'''Here I originally looked for the index but also noticed with some input 
I got Type errors. So I added it to this function as well.'''
def test3_index(find_index):
    with open('my_family.txt','r') as family_doc:
        family_info = family_doc.read()
        try:
            family_index = family_info[find_index]
            print(f"Test 3 Sucess! The index of {find_index} in this file is \
{family_index}.")
    
        except IndexError:
                print(f"Test 3 Index Error: {find_index} is out of range. \n")
        except TypeError:
                print(f"Test 3 Type Error: {find_index} is a {type(find_index)}, it needs to be a integer.")


'''This function calls an Assert statement. If it fails, an Assertion Error
is returned.It tested using what I learned about reading files, using string 
methods, and changing the object types from other chapters.''' 
def test4_assert(find_count):
    with open('my_family.txt', 'r') as family_doc:
        family_string= family_doc.read()
        str_check = str(find_count)
        try:
            count_number = family_string.count(str_check)
            assert count_number > 0
            print('Test 4 Success! This made my assertion true.')
        except AssertionError:
            print('Test 4 Assertion Error: This failed my assertion statement.')    

#here we have a __main__ function where all the above functions live. 
def __main__():
#successful file call proving file existence.
    file_call('my_family.txt')
#failed file call showing file does not exist.
    file_call('your_family.txt')
#success of first test showing existence of type within the file. 
    test1_value('dad')
# failure for a proper value, returning a Value Error. 
    test1_value(11)
#success of type and arithmetic; the value meets both requirements for this.
    test2_type(100)
#failure of Arithmetic and Type errors because it is divided by 0 or by a string
    test2_type('mom')
    test2_type(0)
# sucessful value input for index that is the proper type for this function.
    test3_index(15)
# failure of index range, returning an Index Error 
    test3_index(700)
# successful argument for Assertion
    test4_assert('dad')
# failure returning an Assertion Error
    test4_assert(23.5)
    
__main__()