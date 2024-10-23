# Name: Sinead Keane
# Course: ISCH620
# Title: Assignment 1
# Contact information: 857-294-2616; sinead.keane001@gmail.com
# Due Date: 09/17/2023

#modulo function= produces the remainder of 2 divided integers
def modulo(): 
    modinput_1 = int(input('choose a dividend: '))
    modinput_2= int(input('choose a divisor: '))
    if modinput_2 == 0:
        print("No zeroes please!")
        modulo()
    else: 
        mod_answer= (modinput_1%modinput_2)
        print("Your answer is",round(mod_answer,2))
        print()
        print()

#division function = produces the product of division of 2 integers
def division(): 
    divinput_1 = int(input('choose a dividend: '))
    divinput_2= int(input('choose a divisor: '))
    if divinput_2 == 0:
        print('No zeroes please!')
        division()
    else:
        div_answer= (divinput_1/divinput_2)
        print ("Your answer is",round(div_answer,2))
        print()
        print()

# Original Work for Binary- Kept pulling an error of "convert_bin() not defined"
# def convert_bin():
#     user_input= int(input('Pick a number between 0-255'))
#     user_rmndr =  user_input%2 
#     user_input_div = ''
#     while user_input > 0:
#         user_input_div = user_input/2
#         print(f'your number is {user_input} your binary is \
#                   {user_rmndr}.')
#             print ('binary is 0 for ', user_input, 'the binary is 0')
#         if user_input < 0:
#             print('Number must be above 0')
#         elif user_input>255:
#             print('Number must be below 255')
#             user_input
#         else:
#             print(f'Your number is {user_input}, the binary is 0')
# convert_bin()
 
#ChatGPT gave me the following instead:
# def convert_bin():
#     user_input = int(input('Pick a number between 0-255: '))

#     if user_input < 0:
#         print('Number must be above 0')
#     elif user_input > 255:
#         print('Number must be below 255')
#     else:
#         binary_representation = ''

#         while user_input > 0:
#             user_rmndr = user_input % 2
#             binary_representation = str(user_rmndr) + binary_representation
#             user_input //= 2

#         print(f'Your number is {user_input}, the binary is {binary_representation}')

# convert_bin()
# it seems as though I did it backwards? 
#when tested, it didnt return a binary for 0 though      

#Attempt 2 with my code/ChatGPT suggestions is below and works!

#convert_bin function: divides a base 10 numberby two and take the remainder 
# 1 or 0 as to identify binary of number. the series that is a result of 
# this is the binary. 
def convert_bin(user_input): 
    if user_input < 0:
        print('Number must be above 0')
        convert_bin()
    elif user_input > 255:
        print('Number must be below 255')
        convert_bin()
    elif user_input == 0:
        print(f'Your number is {user_input}, the binary is 0')
    else:
        binary_representation = ''
        keep_user_input = user_input

        while user_input > 0:
            user_rmndr = user_input % 2
            binary_representation = str(user_rmndr) + binary_representation
            user_input //= 2

        print(f'Your number is {keep_user_input}, the binary is {binary_representation}')


#convert to hexidecimal: here we need to divide by 16 and take the remainder. 
#Any remainders between 0-9 are the numbers 0-9, 10-15 are assigned A-F.
#the series that is a result of this is the hexidecimal.
def convert_hex(user_input):
    if user_input < 0:
        print('Number must be above 0')
        convert_hex()
    elif user_input > 255:
        print('Number must be below 255')
        convert_hex()
    elif user_input == 0:
        print(f'Your number is {user_input}, the hexidecimal is 0')
    else:
        hex_representation = ''
        keep_user_input = user_input

        while user_input > 0:
            user_rmndr = user_input % 16
            if user_rmndr == 10:
                user_rmndr = 'A'
            elif user_rmndr == 11:
                user_rmndr = 'B'                
            elif user_rmndr == 12:
                user_rmndr = 'C'
            elif user_rmndr == 13:
                user_rmndr = 'D'                
            elif user_rmndr == 14:
                user_rmndr = 'E'
            elif user_rmndr == 15:
                user_rmndr = 'F'
            hex_representation = str(user_rmndr) + hex_representation
            user_input = user_input//16

        print(f'Your number is {keep_user_input}, the hexidecimal is {hex_representation}')
        print()
        print()
# I took the Binary code and adjusted it for Hexidecimal. Has to maintain the user_input 
#so I added that in where hex_representation was mostly because it worked with that one.
# Professor, thank you for the tip.

#I came up with the convert all function to execute convert_bin and convert_hex
#however I was confused on how to use user_input once for both functions. Here I asked
#ChatGPT was used here as a means to understand how to run it.
#ChatGPT suggested using user_input in the convert_all/_bin/_hex argument for this 

#The convert_all function executes the convert_bin and convert_hex together with
# user_input
# MY ORIGINAL; THIS RESULTED IN THE INPUT BEING REQUESTED TWICE ---
#def convert_all():   
#     convert_bin(user_input)
#     convert_hex(user_input)
#     print()
#     print()

# NEW CODE BY CHATGPT ---
# def convert_all(user_input):
#     convert_bin(user_input)
#     convert_hex(user_input)

# MY ADJUSTED AFTER CHATGPT  (I also added user_input to the arguments in the
# other conversion functions)
def convert_all(user_input):   
    convert_bin(user_input)
    convert_hex(user_input)
    print()
    print()
    
    

#the full math menu that is continuous & :
def menu():
    while True:
        print("Welcome to the Math Menu!")
        print()
        print("Please select an option from below:")
        print('For Division: 1')
        print('For Modulo: 2')  
        print('For Conversion: 3')
        print('To Quit: 4')
        print()
        customer_choice= input("What would you like to do?  ")
        
        if customer_choice == '1':
            division()
        elif customer_choice == '2':
            modulo()
# ORIGINAL CODE
        # elif customer_choice == '3':
        #     convert_all()
# CHATGPT RECOMMENDATIOn
        # elif customer_choice == '3':
        #     user_input = int(input('Choose a number between 0-255: '))
        #     convert_all(user_input)  # Pass user_input to convert_all

# MY CODE AFTER CHATGPT RECOMMENDATION
        elif customer_choice == '3':
            user_input = int(input("Please choose a number between 0-255: "))
            convert_all(user_input)
        elif customer_choice == '4':
            print('Thanks for trying this out! Goodbye.')
            break
        else:
            print()
            print("Not an option, please try again.")
            print()
            menu()
menu()
