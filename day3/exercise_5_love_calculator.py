# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

"""

# First answer before class.

true = 0
love = 0

name1_lower = name1.lower()
name2_lower = name2.lower()

true += name1_lower.count('t')
true += name2_lower.count('t')
true += name1_lower.count('r')
true += name2_lower.count('r')
true += name1_lower.count('u')
true += name2_lower.count('u')
true += name1_lower.count('e')
true += name2_lower.count('e')

love += name1_lower.count('l')
love += name2_lower.count('l')
love += name1_lower.count('o')
love += name2_lower.count('o')
love += name1_lower.count('v')
love += name2_lower.count('v')
love += name1_lower.count('e')
love += name2_lower.count('e')

score = int(str(true) + str(love))

if score < 10 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif score >= 40 and score <= 50:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}.')

"""


# Final answer after watched the class.
true = 0
love = 0

combined_names_lower = name1.lower() + name2.lower()

true += combined_names_lower.count('t')
true += combined_names_lower.count('r')
true += combined_names_lower.count('u')
true += combined_names_lower.count('e')

love += combined_names_lower.count('l')
love += combined_names_lower.count('o')
love += combined_names_lower.count('v')
love += combined_names_lower.count('e')

score = int(str(true) + str(love))

if score < 10 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif score >= 40 and score <= 50:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}.')
