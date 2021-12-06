import random
left = int(input('Min число: '))
right = int(input('Max число: '))
print(f'Привет, загадай число от {left} до {right}, а я отгадаю его менее чем за 10 шагов')
current = random.randint(left, right)
attempts = 0
step = 0
while True:
    step+=1
    print(f"Шаг {step}")
    is_right = input(f'Ваше число - {current}? (да, >, <) ')
    attempts += 1
    if is_right=='>':
        current+=1
    elif is_right=='<':
        current-= 1
    else:
        print('Я угадал, ура!')
        break

