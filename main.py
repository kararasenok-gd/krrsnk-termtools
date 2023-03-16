import os

print("Приветсвую в установке KRRSNK TermTools!")
print("Для установки надо минимум 2гб свободного места!")
q = int(input("""Выберите нужное:
1. Установка
2. Выйти
>>>"""))

if q == 1:
    print("Начало установки....")
    os.system("bash setup.sh")
else:
    quit