import os

phonebook = []

def display_menu():
    print("\nТелефонный справочник:")
    print("1. Вывести все записи")
    print("2. Добавить новую запись")
    print("3. Найти запись")
    print("4. Изменить запись")
    print("5. Удалить запись")
    print("6. Сохранить в файл")
    print("7. Загрузить из файла")
    print("8. Выход")

def display_contacts():
    if not phonebook:
        print("Телефонный справочник пуст.")
    else:
        print("\nЗаписи в телефонном справочнике:")
        for contact in phonebook:
            print(f"{contact['Фамилия']} {contact['Имя']} {contact['Отчество']}: {contact['Телефон']}")

def add_contact():
    contact = {}
    contact['Фамилия'] = input("Введите фамилию: ")
    contact['Имя'] = input("Введите имя: ")
    contact['Отчество'] = input("Введите отчество: ")
    contact['Телефон'] = input("Введите номер телефона: ")
    phonebook.append(contact)
    print("Запись добавлена.")

def find_contact():
    search_term = input("Введите имя или фамилию для поиска: ")
    found_contacts = [contact for contact in phonebook if
                      search_term.lower() in contact['Фамилия'].lower() or search_term.lower() in contact['Имя'].lower()]
    if found_contacts:
        print("\nНайденные записи:")
        for contact in found_contacts:
            print(f"{contact['Фамилия']} {contact['Имя']} {contact['Отчество']}: {contact['Телефон']}")
    else:
        print("Записи не найдены.")

def edit_contact():
    search_term = input("Введите имя или фамилию для поиска записи, которую вы хотите изменить: ")
    found_contacts = [contact for contact in phonebook if
                      search_term.lower() in contact['Фамилия'].lower() or search_term.lower() in contact['Имя'].lower()]
    if found_contacts:
        display_contacts()
        choice = int(input("Введите номер записи, которую вы хотите изменить: ")) - 1
        if 0 <= choice < len(found_contacts):
            contact = found_contacts[choice]
            print(f"\nРедактирование записи: {contact['Фамилия']} {contact['Имя']} {contact['Отчество']}: {contact['Телефон']}")
            contact['Фамилия'] = input("Введите новую фамилию: ")
            contact['Имя'] = input("Введите новое имя: ")
            contact['Отчество'] = input("Введите новое отчество: ")
            contact['Телефон'] = input("Введите новый номер телефона: ")
            print("Запись изменена.")
        else:
            print("Некорректный выбор.")
    else:
        print("Записи не найдены.")

def delete_contact():
    search_term = input("Введите имя или фамилию для поиска записи, которую вы хотите удалить: ")
    found_contacts = [contact for contact in phonebook if
                      search_term.lower() in contact['Фамилия'].lower() or search_term.lower() in contact['Имя'].lower()]
    if found_contacts:
        display_contacts()
        choice = int(input("Введите номер записи, которую вы хотите удалить: ")) - 1
        if 0 <= choice < len(found_contacts):
            contact = found_contacts[choice]
            phonebook.remove(contact)
            print("Запись удалена.")
        else:
            print("Некорректный выбор.")
    else:
        print("Записи не найдены.")

def save_to_file():
    filename = input("Введите имя файла для сохранения: ")
    with open(filename, 'w') as file:
        for contact in phonebook:
            file.write(f"{contact['Фамилия']} {contact['Имя']} {contact['Отчество']}: {contact['Телефон']}\n")
    print(f"Данные сохранены в файл {filename}.")

def load_from_file():
    filename = input("Введите имя файла для загрузки: ")
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            phonebook.clear()
            for line in lines:
                parts = line.split(':')
                name_parts = parts[0].split()
                contact = {
                    'Фамилия': name_parts[0],
                    'Имя': name_parts[1],
                    'Отчество': name_parts[2],
                    'Телефон': parts[1].strip()
                }
                phonebook.append(contact)
        print(f"Данные загружены из файла {filename}.")
    else:
        print("Файл не найден.")

def main():
    while True:
        display_menu()
        choice = int(input("Выберите операцию (от 1 до 8): "))
        if choice == 1:
            display_contacts()
        elif choice == 2:
            add_contact()
        elif choice == 3:
            find_contact()
        elif choice == 4:
            edit_contact()
        elif choice == 5:
            delete_contact()
        elif choice == 6:
            save_to_file()
        elif choice == 7:
            load_from_file()
        elif choice == 8:
            print("Программа завершена.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите от 1 до 8.")

if __name__ == "__main__":
    main()