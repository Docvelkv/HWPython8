# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать
# функционал для изменения и удаления данных
from addInterface import correct_int

book = "phone_book.txt"


def read_all_contacts() -> list[str]:
    """
    Построчное чтение файла.

    Returns:
        list[str]: Пронумерованный список строк.
    """
    with open(book, "r", encoding="utf-8") as file:
        for num, line in enumerate(file, 1):
            print(f"{num}. {line.strip()}")


def new_contact():
    """
    Создание и запись в файл новой строки.
    """
    print("Введите ФИО: ", end="")
    full_name = input()
    print("Введите номер телефона: ", end="")
    num_tel = input()
    with open(book, "a", encoding="utf-8") as file:
        file.writelines(f"{full_name} | {num_tel}\n")
        print("Контакт добавлен.")


def contact_search() -> str:
    """
    Поиск в файле и вывод в консоль строки, содержащей
    введённые символы.

    Returns:
        str: Все найденные строки с исходной нумерацией.
    """
    print("Введите данные для поиска: ", end="")
    str_search = input()
    with open(book, "r", encoding="utf-8") as file:
        for num, line in enumerate(file, 1):
            if str_search.lower() in line.lower():
                print(f"{num}. {line.strip()}")


def menu_phone_book():
    """
    Выбор режима работы с файлом.

    Returns:
        function: Запускает выбранную функцию.
    """
    is_phonebook_mode = True
    while is_phonebook_mode:
        print("Выберите режим работы:\n"
              "1 - Прочитать весь справочник.\n"
              "2 - Добавить новый контакт.\n"
              "3 - Найти контакт.")
        act = correct_int()
        if act == 1:
            read_all_contacts()
            is_phonebook_mode = False
        elif act == 2:
            new_contact()
            is_phonebook_mode = False
        elif act == 3:
            contact_search()
            is_phonebook_mode = False
        else:
            print("Такого режима работы нет. "
                  "Внимательно прочитайте и введите снова: ")


menu_phone_book()
