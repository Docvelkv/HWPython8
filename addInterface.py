from random import randint as irand, random as frand


def correct_int() -> int:
    """
    Ввод целого числа с обработкой некорректного введения.

    Returns:
        int: целое число или предложение ввести снова.
    """
    is_correct = True
    while is_correct:
        num_int = input()
        try:
            num_int = int(num_int)
            is_correct = False
            return num_int
        except ValueError:
            print("Это не целое число. Введите снова:")


def creat_int_list(num_elm=10, min_val=0, max_val=10) -> list:
    """
    Создание списка из целых чисел.

    Args:
        num_elm (int, optional): количество элементов списка. Defaults to 10.
        min_val (int, optional): начало диапазона. Defaults to 0.
        max_val (int, optional): конец диапазона. Defaults to 10.

    Returns:
        list[]:
    """
    list_1 = [irand(min_val, max_val) for i in range(num_elm)]
    return list_1


def creat_float_list(num_elm=10, min_val=0, max_val=10, num_dig=1) -> list:
    """
    Создание списка из вещественных чисел.

    Args:
        num_elm (int, optional): количество элементов списка. Defaults to 10.
        min_val (int, optional): начало диапазона. Defaults to 0.
        max_val (int, optional): конец диапазона. Defaults to 10.
        num_dig (int, optional): количество цифр после запятой. Defaults to 1.

    Returns:
        list[]:
    """
    list_1 = [irand(min_val, max_val) + round(frand(), num_dig)
              for i in range(num_elm)]
    return list_1


def divisors_num(num: int) -> list:
    """
    Поиск делителей числа

    Args:
        num (int): Число

    Returns:
        list: Список делителей, исключая само число
    """
    list_divisors = []
    num_k = num
    for i in range(num_k // 2, 0, -1):
        if num_k % i == 0:
            list_divisors.append(i)
    return list_divisors
