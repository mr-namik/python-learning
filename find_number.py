import random

random_number=random.randint(1,100)

n=0

while n<7:
    try:
        user_number=int(input("Угадай число от 1 до 100: "))
        n+=1
        if user_number < random_number:
            print("Загаданное число больше.")
        elif user_number > random_number:
            print("Загаданное число меньше.")
        else:
            print("Поздравляем! Вы угадали число!")
            break
    except ValueError:
        print("Пожалуйста, введите целое число.")
if n > 7:
    print("К сожалению, вы не угадали число. Загаданное число было:", random_number)