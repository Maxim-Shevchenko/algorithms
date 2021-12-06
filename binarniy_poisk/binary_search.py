import random
left = int(input('Min число: '))
right = int(input('Max число: '))
print(f'Привет, загадай число от {left} до {right}, а я отгадаю его менее чем за 10 шагов')
current = random.randint(left, right)
attempts = 0
while True:
    is_right = input(f'Ваше число - {current}? (да, >, <) ')
    attempts += 1
    if is_right=='>':
        left = current + 1
        print(left, right)  # посмотрим теперь на левую границу диапазона
    elif is_right=='<':
        right = current-1 # правая граница – само число, но на 1 больше
        print(left, right)
    else:
        print('Я угадал, ура!')
        break
    current = round((left+right)/2) # округляем, потому что мы отгадываем целые числа.
