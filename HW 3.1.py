#Банкомат видає суму дрібними, але не більше 10 штук кожної дрібної купюри
banknote = int(input('Enter money: '))

list = [1, 2, 5, 10]

for i in list:
    print(f'Купюр по {i}: {banknote <= 10}')
    banknote %= i
    if not banknote:
        break