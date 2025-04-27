# Возведение в степень

def power_operations():

    numbers_input = input("Введите числа через пробел: ")
    numbers = numbers_input.split()

    try:
        power = int(input("Введите степень: "))
    except ValueError:
        print("Ошибка: степень должна быть целым числом.")
        return

    result = []
    for item in numbers:
        try:
            num = float(item)
            result.append(num ** power)
        except ValueError:
            result.append(item * power)

    print("Вывод:", ' '.join(map(str, result)))

power_operations()

# Преобразование словаря

def dictionary_to_sets():

    dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}

    key_set = set(dct.keys())
    value_set = set(dct.values())

    print("Множество ключей:", key_set)
    print("Множество значений:", value_set)

    combined_set = key_set.union(value_set)
    print("Объединение множеств:", combined_set)

dictionary_to_sets()

# Пересечение двух списков

def find_common_elements():

    try:
        list1_str = input("Введите первый список: ")
        list1 = set(map(int, list1_str.split()))

        list2_str = input("Введите второй список: ")
        list2 = set(map(int, list2_str.split()))

        common_elements = list1.intersection(list2)

        print("Общие элементы:", *common_elements)

    except ValueError:
        print("Ошибка: Введите целые числа, разделенные пробелами.")

find_common_elements()

# Подсчет количества слов

def word_count():

    text = input("Введите строку: ").lower()
    words = text.split()
    word_counts = {}

    for word in words:
        count = words.count(word)
        word_counts[word] = count

    for word, count in word_counts.items():
        print(f"{word}: {count}")

word_count()