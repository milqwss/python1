# Форматирование строк

def formatting_strings():

    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    age = input("Введите возраст: ")

    # format
    formatted_string_format = "Имя: {}, Фамилия: {}, Возраст: {} лет".format(name, surname, age)
    print("Реализация через .format():")
    print(formatted_string_format)

    # f-string
    formatted_string_fstring = f"Имя: {name}, Фамилия: {surname}, Возраст: {age} лет"
    print("Реализация через f-string:")
    print(formatted_string_fstring)

formatting_strings()


# Четность числа

def chetnost_chisla():

    try:
        input_number = input("Введите целое число: ")
        number = int(input_number)

        if number <= 0:
            print("Внимание: Требуется положительное число.")
            return

        if number % 2 == 0:
            print(f"Число {number} - четное")
        else:
            print(f"Число {number} - нечетное")

    except ValueError:
        print("Ошибка: Некорректный ввод. Введите целое число.")

chetnost_chisla()

# Проверка возраста

def proverka_vozrasta():

    try:
        input_age = input("Укажите ваш возраст: ")
        age = int(input_age)

        if age < 0:
            print("Некорректный возраст!")
        elif age >= 18:
            print("Вы - взрослый человек.")
        else:
            print("Вы - ребенок.")

    except ValueError:
        print("Ошибка: Необходимо ввести число!")

proverka_vozrasta()

# Длина числа

def dlina_chisla():

    while True:
        entry = input("Введите число (или 'exit' для выхода): → ")

        if entry.lower() == "exit":
            print("Завершение работы...")
            break

        # Проверка на число, включая отрицательные
        if entry.lstrip('-').isdigit():
            digit_number = entry.lstrip('-')
            print(f"Число состоит из {len(digit_number)} цифр.")
        else:
            print("Ошибка: Это не число.")

dlina_chisla()