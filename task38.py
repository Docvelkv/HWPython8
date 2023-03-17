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
    Поиск в файле и вывод в консоль строки, содержащей введённые символы.

    Returns:
        str: Все найденные строки с исходной нумерацией.
    """
    print("Введите данные для поиска: ", end="")
    str_search = input()
    list_str = []
    with open(book, "r", encoding="utf-8") as file:
        for num, line in enumerate(file, 1):
            if str_search.lower() in line.lower():
                list_str.append(f"{num}. {line}")
    if len(list_str) > 0:
        for i in list_str:
            print(i, end="\r")
    else:
        print("Контакт не найден.")


def changing_contact():
    """
    Переписывает выбранную строку новыми данными
    """
    all_contacts = []
    with open(book, "r", encoding="utf-8") as file:
        for num, line in enumerate(file, 1):
            print(f"{num}. {line.strip()}")
            all_contacts.append(line)
    print("Введите номер контакта для изменения: ", end="")
    change_num = correct_int()
    print(all_contacts[change_num - 1])
    print("Введите новые данные.")
    print("Введите ФИО: ", end="")
    full_name = input()
    print("Введите номер телефона: ", end="")
    num_tel = input()
    new_contact = f"{full_name} | {num_tel}"
    all_contacts.pop(change_num - 1)
    all_contacts.insert(change_num - 1, new_contact)
    with open(book, "w", encoding="utf-8") as file:
        file.writelines(all_contacts)
    print("Контакт обновлён.")


def deleting_contact():
    """
    Выводит все строки файла и удаляет строку с выбранным номером.
    """
    all_contacts = []
    with open(book, "r", encoding="utf-8") as file:
        for num, line in enumerate(file, 1):
            print(f"{num}. {line.strip()}")
            all_contacts.append(line)
        print("Выберите номер строки для удаления: ", end="")
        del_num = correct_int()
        all_contacts.pop(del_num - 1)
    with open(book, "w", encoding="utf-8") as file:
        file.writelines(all_contacts)
    print("Контакт удалён.")


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
              "3 - Найти контакт.\n"
              "4 - Изменить контакт.\n"
              "5 - Удалить контакт.\n"
              "0 - Выход.")
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
        elif act == 4:
            changing_contact()
            is_phonebook_mode = False
        elif act == 5:
            deleting_contact()
            is_phonebook_mode = False
        elif act == 0:
            is_phonebook_mode = False
        else:
            print("Такого режима работы нет. "
                  "Внимательно прочитайте и введите снова: ")


menu_phone_book()
