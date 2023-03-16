import os

banner = open("banner.sh", "a")
userfind = open("userfind.sh", "a")
arhc = open("arhc.sh", "a")
internet = open("internet.sh", "a")
starter = open("start.py", "a")

banner.write("""cd Termux-Banner/zsh
chmod +x requirement.sh t-ban.sh
bash requirement.sh
bash t-ban.sh""")

userfind.write("""cd UserFinder && bash UserFinder.sh""")

arhc.write("""cd AllRegionHostChecker && python main.py""")

internet.write('''echo -n "Введите URL сайта: "
read URL

w3m $URL''')

starter.write('''import os

print("""Выбирите нужное:
1. Установить баннер
2. Найти профили по нику в интернете
3. Проверка отклика сайта
4. Интернет
5. Выход""")

select = int(input(">>>"))

if select == 1:
    os.system("bash banner.sh")
elif select  == 2:
    os.system("bash userfind.sh")
elif select == 3:
    os.system("bash arhc.sh")
elif select == 4:
    os.system("bash internet.sh")
else:
    os.system("python quit.py")''')

banner.close()
userfind.close()
arhc.close()
internet.close()
starter.close()

os.system("clear")

os.system("rm setup.sh")
os.system("rm main.py")

os.system("python finale.py")