# преобразуем полученную последовательность в список
def string_to_list(numbers):
    list_of_strings = numbers.split()
    string_to_numbers = list(map(int, list_of_strings))

    return string_to_numbers


# запрашиваем у пользователя ввод числа для поиска
def input_search_num(string_to_numbers):
    try:
        num = int(input('Введите число для поиска: '))

        if min(string_to_numbers) < num <= max(string_to_numbers):

            return num

        else:
            print(f'Указанное число не входит в числовую последовательность с границами '
                  f'[{min(string_to_numbers)}:{max(string_to_numbers)}], необходимо повторить ввод.')
            input_search_num(string_to_numbers)

    except ValueError:
        print('Указано не целое число, необходимо повторить ввод.')
        input_search_num(string_to_numbers)


# выполняем сортировку слиянием
# 1й этап = делим список на две части
def merge_sort(string_to_numbers):
    if len(string_to_numbers) < 2:

        return string_to_numbers[:]

    else:
        middle = len(string_to_numbers) // 2
        left = merge_sort(string_to_numbers[:middle])
        right = merge_sort(string_to_numbers[middle:])

        return merge(left, right)


# 2й этап - объединяем списки в один
def merge(left, right):
    sorted_list = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    while i < len(left):
        sorted_list.append(left[i])
        i += 1

    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list


# поиск индекса искомого числа
def binary_search(sorted_list, num, left, right):
    if left > right:

        return f'Число {num} в списке отсутствует'

    middle = (right + left) // 2
    if sorted_list[middle] == num:

        return middle

    elif num < sorted_list[middle]:

        return binary_search(sorted_list, num, left, middle - 1)

    else:

        return binary_search(sorted_list, num, middle + 1, right)


if __name__ == '__main__':
    # запрашиваем у пользователя ввод чисел через пробел
    nums = input("Введите числа через пробел: ")

    # определяем переменную для преобразования строки с числами в список
    str_to_num = string_to_list(nums)

    # определяем переменную для запроса у пользователя отдельного числа
    int_num = input_search_num(str_to_num)

    # определяем переменную для сортированного списка
    sort_list = merge_sort(str_to_num)

    # выводим индекс искомого элемента
    index_search_item = binary_search(sort_list, int_num, 0, len(str_to_num))

    # если число в списке есть, то выводим его индекс
    if type(index_search_item) == int:
        print(f'Индекс числа {int_num}: {index_search_item}')
    elif type(index_search_item) == str:
        print(f'Число {int_num} в списке отсутствует')
