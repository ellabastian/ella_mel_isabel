# QUESTION 1

# Answer version 1

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

# Answer version 2
cheese = ["Cheddar", "Stilton", "Cornish Yarg"]

cheese.append("Oke")
print(cheese)


# new_cheese = ["Red Leicester", "Mozzarella"]
# cheese.extend(new_cheese)
cheese.extend(["Red Leicester", "Mozzarella"])
print(cheese)

###

# QUESTION 2

# Version 1
# This prints 5
tup = 'Hello'
print(len(tup))

# But this prints 1 due to the trailing comma - thinks it's half a tuple so there is 1 x tuple.
tup = 'Hello',
print(len(tup))

# Version 2
# Measuring length of string
tup = 'Hello'
print(len(tup))

# Measuring length of tuple
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
import random

numbers_between_one_fifty = list(range(1, 50))

lottery = random.sample(numbers_between_one_fifty, 6)
print(f"Your lottery ticket numbers are:", str(lottery))