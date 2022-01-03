# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
years_remainig = 90 - int(age)
months_remaining = years_remainig * 12
weeks_remaining = years_remainig * 52
days_remaining = years_remainig * 365

print(
    f'You have {days_remaining} days, {weeks_remaining} weeks, and ' +
    f'{months_remaining} months left.'
)
