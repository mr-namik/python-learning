spisok =[]

while True:
    try:
        number = int(input("Enter a number (1 - Добавить задачу, 2 - Удалить задачу, 3 - Показать задачи, 4 - Выход): "))
        if number == 1:
            task = input("Введите задачу: ")
            spisok.append(task)
        elif number == 2:
            task = input("Введите задачу для удаления: ")
            if task in spisok:
                spisok.remove(task)
            else:
                print("Задача не найдена.")
        elif number == 3:
            print("Список задач:")
            for task in spisok:
                print(task)
        elif number == 4:
            print("Выход из программы.")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")