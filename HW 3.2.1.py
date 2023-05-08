#Написати fizzbuzz для 20 комплектів по три числа, які записані \n
# в файл. Читайте із файлу перший рядок з трьома числами, беріть \n
# із нього числа, рахуйте для них fizzbuzz, виводите, продовжуйте \n
# з наступним рядком і так до кінця файла.

with open('numbers.txt', 'r') as f:
    items = f.read().split('\n')
    for i in items:
        numbers.append([int(n) for n in i.split(',')])

for nums in numbers:
    for num in range(1, nums[2]+1):
        if num % nums[0] == 0 and num % nums[1] == 0:
            print('FizzBuzz', end = ' ')
        elif num % nums[0] == 0:
            print('Fizz', end = ' ')
        elif num % nums[1] == 0:
            print('Buzz', end = ' ')
        else:
            print(num, end = ' ')