import random

numbers_between_one_fifty = list(range(1, 50))

lottery = random.sample(numbers_between_one_fifty, 6)
print(f"Your lottery ticket numbers are:", str(lottery))






