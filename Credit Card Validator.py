#!/usr/bin/env python
# coding: utf-8

# In[38]:


#Credit Card Validator using the check digit and Luhn's Algorithm

card_num_input = input('Please enter a 16 digit credit card number, without spaces: ')
credit_card = [int(num) for num in card_num_input]
#Multiply every other number except last, by 2
credit_card[0:-1:2] = [num * 2 for num in credit_card[0:-1:2]]
#removing last digit as the check digit
check_digit = credit_card.pop()
print(f'Your check digit is {check_digit}')
#converting double digit numbers into single digits and summing them together
for num in credit_card:
    if num >= 10:
        credit_card.remove(num)
        double_digit_sums = sum(list(map(int,str(num)))) 
        credit_card.append(double_digit_sums)
#summing credit card numbers together        
sum_card = sum(credit_card)
#checking to see if the total sum is evenly divisible by 10
if (sum_card + check_digit) % 10 == 0:
    print('This credit card is valid')
else:
    print('This credit card is not valid')


# In[ ]:




