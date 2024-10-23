# -*- coding: utf-8 -*-
'''
Name: Sinead Keane
Due Date: 10/23/2023
Class: ISCH 620
Title: Assignment #2
Contact information: 857-294-2616; sinead.keane001@gmail.com




This is my original vision into what I wanted to do. Revision 1'''

def file_call():
    print('this will call the file from my_family.txt, or pull an Import\
Error')

def test1_find():
    print('here I will try check if an attribute is there.I.E is their DOB\
 or city of origin in there. Pull an Attribute Error if not.')

def test2_index():
    print('this will test for the index of an object in the file. It will\
push an Index Error if out of range.')

def test3_older():
    print('this test will check if one is older than the other. \
Return an Arithmetic Error if not.')

def test4_findname():
    print('this will find if the name of my family member is in there \
planning on attempting a Name Error exception if I am understanding it right')
    
def test5_year():
    print('This will take the age the person is and give the year. If no age\
 or no person in the file it wont work. Could return an Object Error')
    
def __main__():
    file_call()
    test1_find()
    test2_index()
    test3_older()
    test4_findname()
    test5_year()
    print('success! if it all works, failure... if not.')
    
__main__()