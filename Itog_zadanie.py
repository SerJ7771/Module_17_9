def list_input():
    # удаление пробелов из введенной последовательности и преобразование введенных элементов в числовой список
    while True:
        # Бесконечный цикл, который продолжает выполняться до возникновения исключения
        # Пробуем ввести набор чисел с клавиатуры и преобразовываем этот набор в список чисел
        try:
            data = input('Введите последовательность чисел через пробел = ')
            while len(data) == 0:
                print('Список не может быть пустым')
                data = input('Введите последовательность чисел через пробел = ')
            list_of_string = data.split()
            list_of_string = list(map(int, list_of_string))
        # Если полученный ввод не преобразовывается в список чисел, будет вызвано исключение
        except ValueError:
            # Цикл будет повторяться до правильного ввода
            print('Error! В наборе присутствуют нечисловые элементы.')
        # При успешном преобразовании в список чисел, цикл закончится.
        else:
            # возвращаем введенный и проверенный список
            return list_of_string
def element_input():
    # Бесконечный цикл, который продолжает выполняться до возникновения исключения
    while True:
        # Пробуем ввести число с клавиатуры и преобразовываем его в число
        try:
            element = input('Введите любое число = ')
            element = int(element)
        # Если полученный ввод не преобразовывается в число, будет вызвано исключение
        except ValueError:
            # Цикл будет повторяться до правильного ввода
            print('Error! Это не число, попробуйте снова.')
        # При успешном преобразовании в целое число, цикл закончится.
        else:
            # возвращаем введенный и проверенный element
            return element
def sort_array(list_of_string, input_element):
    list_of_string.append(input_element) # Добавляем введенное число в список
    # list_of_string.sort()  # это метод сортировки списка Python, так короче
    # сортировка списка по возрастанию. Этот вариант используется в модуле
    for i in range(1, len(list_of_string)):
        x = list_of_string[i]
        idx = i
        while idx > 0 and list_of_string[idx - 1] > x:
            list_of_string[idx] = list_of_string[idx - 1]
            idx -= 1
        list_of_string[idx] = x
    # k = 0
    #
    # for m in list_of_string:
    #     if input_element > m:
    #         k += 1
    #
    # list_of_string.insert(k, input_element)  # Добавление введенного числа в список по индексу
    # в бинарном поиске не работает
    # взвращаем отсортированный список
    return list_of_string
def binary_search(data_list, input_element, index_left, index_right):
    # Бинарный поиск
    if index_left > index_right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (index_right + index_left) // 2  # находим середину
    if data_list[middle] == input_element:  # если элемент в середине,
        x = data_list[: middle]  # ищем индекс последнего элемента в левой половине, он и есть ближайшее меньшее число
        # print(x)
        for i in x:
            if i == input_element:
                x.remove(input_element)
        index_1 = (len(x) - 1)
        y = data_list[middle:]  # # ищем индекс первого элемента в правой половине, он и есть ближайшее большее число
        for n in y:
            if n <= input_element and len(y) > 1:
                y.remove(n)
        f = y[0]
        index_2 = data_list.index(f)
        if index_1 < 0:
            print(
                f'Это первый элемент списка. Индекс слева Отсутствует. Индекс большего числа справа = {index_2}')
        elif index_2 == len(data_list) - 1:
            print(f'Индекс меньшего числа слева = {index_1}. Это последний элемент списка. Индекс справа отсутствует')
        else:
            print(f'Индекс меньшего числа слева = {index_1}. Индекс большего числа справа = {index_2}')
        return index_1, index_2  # возвращаем эти индексы
    elif input_element < data_list[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(data_list, input_element, index_left, middle - 1)
    else:  # иначе в правой
        return binary_search(data_list, input_element, middle + 1, index_right)
def main():
    array = list_input()
    element = element_input()
    sorting = sort_array(array, element)
    print(f'Сортированный список введенных данных = {sorting}')
    left = 0
    right = len(sorting)
    binary_search(sorting, element, left, right)
if __name__ == '__main__':
    main()
