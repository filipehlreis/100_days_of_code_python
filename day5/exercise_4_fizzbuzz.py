# Write your code below this row 👇

for number in range(1, 101):
    if number % 3 == 0:
        if number % 5 == 0:
            print('FizzBuzz')
        else:
            print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
