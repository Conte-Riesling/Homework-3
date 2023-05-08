#Написати fizzbuzz
a = int(input('Введіть число fizz: '))
b = int(input('Введіть число buzz: '))
c = int(input('Введіть число, до якого необхідно рахувати: '))

for num in range(1, c+1):
    if num % a == 0 and num % b == 0:
        print('FizzBuzz', end = ' ')
    elif num % a == 0:
        print('Fizz', end = ' ')
    elif num % b == 0:
        print('Buzz', end = ' ')
    else:
        print(num, end = ' ')