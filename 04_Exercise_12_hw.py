# QUESTION 1

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += 'Oke'
print(cheese)
# printing cheese returns with 'o', 'k', 'e' rather than as one word appended

# Using append function adds this to the end of the list
cheese.append('Oke')
print(cheese)

# to add multiple new values, use .extend([''])
cheese.extend(['brie', 'camembert'])
print(cheese)

###

# QUESTION 2
# This prints 5
tup = 'Hello'
print(len(tup))

# But this prints 1 due to the trailing comma - thinks it's half a tuple so there is 1 x tuple.
tup = 'Hello',
print(len(tup))

###


### Method 1
# Lottery numbers
import random

# Create empty list to store the numbers
lottery_numbers = []

# Question: should it be to 50 or 51
for i in range (0,6):
    number = random.randint(1, 51)
    # Check if this number has been added to the empty list
    while number in lottery_numbers:
        number = random.sample(1,51)


    # now that we've got the unique number, append it to the list:
    lottery_numbers.append(number)

print(lottery_numbers)

### Method 2 (Ellas)
