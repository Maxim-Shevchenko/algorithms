left = 1  # левая граница диапазона
right = 10  # правая граница диапазона
number = 10  # искомое число
lin_attempts = 0 # попытки линейного
bin_attempts = 0 # попытки бинарного
def linear():
    print(f"Я - алгоритм линейного поиска! Я буду искать число в диапазоне от {left} до {right}.")
    global lin_attempts
    current = left
    while True:
        lin_attempts += 1
        print(f"Я думаю, это число - {current}...")
        if number!=current:
            print("Не то, значит, увеличу на 1...")
            current += 1
        else:
            print(f"Ура, я нашел!")
            break
    print(f"Мне понадобилось {lin_attempts} попыток.")
linear()
print ()
print ()
def binary():
    print(f"А я - алгоритм бинарного поиска! Я тоже буду искать число от {left} до {right}.")
    global bin_attempts
    r = right
    l = left
    while True:
        bin_attempts += 1
        current = round((l + r) / 2)
        print(f"Делю диапазон пополам. Думаю, это число - {current}...")
        if number > current:
            print(f"А, нужное число больше, значит меньше {current} искать не стоит...")
            l = current + 1
        elif number < current:
            print(f"А, нужное число меньше, значит больше {current} искать не стоит...")
            r = current - 1
        else:
            print(f"Ура, я нашел! ")
            break
    print(f"Мне понадобилось {bin_attempts} попыток.")
binary()
print()

print (f"Результат соревнования: линейный поиск - {lin_attempts}, бинарный поиск- {bin_attempts}")