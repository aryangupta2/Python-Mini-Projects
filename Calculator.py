#!/usr/bin/env python
# coding: utf-8

# In[1]:


#calculator for simple arithmetic +-/*
while True:
    #intro sentences for calculator so user can understand what's going on
    print('Welcome to the Python Calculator!')
    print('You can perform simple arithmetic + - * /')
    print('1.Addition(+) \n2.Subtraction(-) \n3.Multiplication(*) \n4.Division(/)')
    #asks for user input for the type of arithmetic to be performed
    user_input_type_arithmetic = input('Please select the type of arithmetic you would like to perform by writing the corresponding number next to it: ')
    first_number = input('Please enter a first number: ')
    second_number = input('Please enter a second number: ')
    #logic for the calculator
    if user_input_type_arithmetic == '1':
        print(f'{first_number} + {second_number} = ' + str(int(first_number) + int(second_number)))
    elif user_input_type_arithmetic == '2':
        print(f'{first_number} - {second_number} = ' + str(int(first_number) - int(second_number)))
    elif user_input_type_arithmetic == '3':
        print(f'{first_number} * {second_number} = ' + str(int(first_number) * int(second_number)))
    else:
        print(f'{first_number} / {second_number} = ' + str(int(first_number) / int(second_number)))
    use_again = input('Would you like to use the calculator again? Please enter y or n: ').lower()
    if use_again == 'y':
        continue
    else:
        print('Thanks for using the Calculator!')
        break
    


# In[ ]:




