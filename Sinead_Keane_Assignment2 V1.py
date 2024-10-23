# # -*- coding: utf-8 -*-
''' Name: Sinead Keane 
    Class: ISCH 620
    Title: Assignment #2
    Contact information: 857-294-2616; sinead.keane001@gmail.com
    Due: 10/04/2023'''
# Spyder Editor

# This is a temporary script file.
# """

''' This takes an empty list named dino_list and allows the user to append it
then choose the order their dinos are in. '''
def dino_list():
    def dino_order ():
        print("Would you like to see your favorite dinosaur? Choose 1-4 to see\
where they are.")
        dino_order_input = int(input("Choose a number 1-4: "))
         
        if dino_order_input in range (1,5):
            if dino_order_input == 1:
               print("Number one is ", first_dino)
            elif dino_order_input == 2:
               print("Number two is ", second_dino)
            elif dino_order_input == 3:
               print("Number three is ", third_dino)
            elif dino_order_input == 4:
                print("Number four is ", fourth_dino)
#this below piece of the code checks for errors in input
        else:
            print("So sorry, that's not an option. Let's try again")    
    print ("Excellent, you selected L for List")
    dino_list=[]
    user_input = input("I love dinosaurs. Can you tell me your favorite? ")
    dino_list.append(user_input)
    for i in range (3): 
        user_input = input("What's about your next favorite?  ")
        dino_list.append(user_input)
    if len(dino_list) == 4:
        print('That works for now. Your list is:  ', dino_list)
        
    first_dino = dino_list[0]
    second_dino = dino_list[1]
    third_dino = dino_list[2]
    fourth_dino = dino_list[3]
    
    

    dino_order ()
     

'''Sets are not ordered, immutable, and cannot be repeated. This required me to 
understand how to create a set without being able to append or extend it like lists.'''

def dino_set():
    print ("Excellent, you selected S for Set")
    user_input = input("Where do you think were dinosaurs found? ")
    user_input_2 = input("Good point, where else? ")
    user_input_3 = input("How many do you think were found  ")
    user_input_4 = input("Who were they found by  ")
    dino_user_set = {user_input, user_input_2, user_input_3, user_input_4}
    print(f'Wow, thanks for the information. You think dinos were found in\
{user_input} and {user_input_2}. There were {user_input_3} found by\
{user_input_4} so your set looks like this {dino_user_set}')
    def user_choices ():
        user_choice = input("Out of the following questions, which would you like to see \
    again?\n1. Who found them? \n2. Where were they found? \n3. How many were found?\n\
    Pick 1-3. ")
        if user_choice == "1":
            print("They were found by", user_input_4)
        elif user_choice == "2":
            print(f'They were found in {user_input} and {user_input_2}')
        elif user_choice == "3":
            print(f'There were {user_input_3} found')
#this below piece of the code checks for errors in input
        else:
            print("Oops, I got nothing for you. Remember it must be 1,2, or 3")
            user_choices ()
            
    user_choices()

''' This is a dictionary. Again, it begins empty then asks the user about dinos
and size. This is made into a dictionary that they can choose from.'''
def dino_dictionary(): 
    print ("Excellent, you selected D for Dictionary")
    dino_list=[]
    dino_size=[]
    sizes = ['Big', 'big', 'Medium', 'medium', 'Small', 'small']
    print("Dinosaurs are big, small, and everything inbetween. Let's \
  learn about your favorites!")
    while len(dino_list) < 4 and len(dino_size) < 4:  
        for i in range (4): 
            user_input = input("What is one of your favorite dinos?  ")
            user_input_2 = input ("Are they big, medium, or small? ")
            if user_input_2 in sizes:
                dino_size.append (user_input_2)
                dino_list.append(user_input)
                break
                # if len(dino_size)== 4 and len(dino_list) == 4:
                #     dino_size_dictionary = {dino_list[0]:dino_size[0], dino_list[1]:dino_size[1],
                #     dino_list[2]: dino_size[2],dino_list[3]:dino_size[3]}
                #     print("Here's your dictionary: ",dino_size_dictionary)
    #this below piece of the code checks for errors in input
            else:
                print("sorry that's not an option. Please enter again.")
            
    if len(dino_size)== 4 and len(dino_list) == 4:
        dino_size_dictionary = {dino_list[0]:dino_size[0], dino_list[1]:dino_size[1],
        dino_list[2]: dino_size[2],dino_list[3]:dino_size[3]}
    print("Here's your dictionary: ", dino_size_dictionary)
    print()
    
    dictionary_pull = input(f'Pick one of your dictionary values from {dino_size_dictionary}')
    if dictionary_pull in dino_list:
        print(dino_size_dictionary[dictionary_pull])
    elif dictionary_pull in dino_size:
        print(dino_size_dictionary[dictionary_pull])
#this below piece of the code checks for errors in input
    else:
        print("Sorry that's not in our dictionary.")
        dictionary_pull


''' Here is out tuple list. Tuples are immutable so I created variables then 
made it a tuple by calling those variables'''
def dino_tuple():
    print ("Excellent, you selected T for Tuple")
    print("Now let's make a tuple of our dino friends")
    print()
    dino_friend_1 = input("What would you name a t-rex with a bowtie? ")    
    dino_friend_2 = input("What would you name a triceratops that loves to read? ")
    dino_friend_3 = input("What would you name a velociraptor with glasses? ")    
    dino_friend_4 = input("What would you name a pterodactyl with a mohawk? ") 
    dino_tuple = (dino_friend_1,dino_friend_2,dino_friend_3,dino_friend_4)
    print(f'Your tuple is {dino_tuple}')
    for index, i in dino_tuple():
        print (index, ": ", i)
    # print("1. ", dino_friend_1, )
    # print("2. ", dino_friend_2)
    # print("3. ", dino_friend_3)
    # print("4. ", dino_friend_4)        
    dino_friend_choice = input("Which dino friend would you like to learn more\
about? \n\Please pick 1-4:  ")
    if dino_friend_choice == "1":
        print()
        print(f' This is {dino_tuple[0]}, they like dressing up.')
        print()
    elif dino_friend_choice == "2":
        print()
        print(f'This is {dino_tuple[1]}, they love fiction books.')
        print()
    elif dino_friend_choice == "3":
        print()
        print(f'This is {dino_tuple[2]}, they love legos.')
        print()
    elif dino_friend_choice == "4":
        print()
        print(f'This is {dino_tuple[3]}, they love rock music.')
        print()
#this below piece of the code checks for errors in input
    else:
        print("oops, no go, let's try again")
        dino_friend_choice
dino_tuple()
#Checks the menu input for errors.
def input_check(menu_user_input):
    if menu_user_input == "L" or menu_user_input == "l":
        dino_list()
    elif menu_user_input == "T" or menu_user_input == "t":
        dino_tuple()
    elif menu_user_input == "D" or menu_user_input == "d":
        dino_dictionary()
    elif menu_user_input == "S" or menu_user_input == "s":  
        dino_set()
    elif menu_user_input == "Q" or menu_user_input == "q":
        print ("OK another time then. Bye!")
    else:
        print("That's not an option for this menu")
        print()
        print("Let's try again")
        return __main__()
 
'''This is our main function calling all of the above and using recursion to 
return if no valid input is entered.'''
def __main__():
    menu_user_input = input("Menu Options: \n\
1. Type L for list \n\
2. Type T for Tuple \n\
3 Type D for dictionary \n\
4.Type S for set \n\
5. Type Q to quit \n\
What will it be?  ")
    input_check(menu_user_input)
    return __main__()
__main__()


        
   

    
    
    

    
        
    

