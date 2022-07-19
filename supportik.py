import socket
print("""
Supportik v1.4 [18.07.2022]
Автор: Данил Пистолетов
Сайт: danil-pistoletov.org
GitHub: github.com/danilpistoletov/supportik
США какиш
""")

def getip():
    import urllib.request
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    print(external_ip)

def getdhcp():
    print(socket.gethostbyname(socket.gethostname()))

def gethelp():
    print("""
    Соблюдайте регистр команд и всё будет хорошо
    help / помощь - список команд и пояснение к ним
    getip / мойайпи - получение внешнего адреса компьютера
    getdhcp / получитьdhcp - получение вашего DHCP
    getpcname / имякомпа - получение имени вашего компьютера
    getdomainip / айписайта [ДОМЕН] - получение IP сайта (без http/https)
    sitestatus / статуссайта [ДОМЕН] - проверка статуса сайта (без http/https)
    speedtest / узнатьскорость - измерение скорости скачивания и загрузки
    getmac / получитьмак - получить MAC-адрес
    getmacnum / получитьмакцифры- получить MAC-адрес в виде числа
    scanportsonip / проверитьпортыайпи - проверить популярные открытые порты по IP
    scanportsondomain / проверитьпортыдомен - проверить популярные открытые порты по домену (без http/https)
    rangeportsdomain / диапазонпортовдомен - проверить открытые порты по домену (без http/https)
    rangeportsip / диапазонпортовайпи - проверить открытые порты по айпи
    getcoords / моикоординаты - узнать координаты по своему IP-адресу
    coordsbyip / координатыайпи - узнать координаты по указанному IP-адресу
    citybyip / городпоайпи - узнать город по IP-адресу
    """)

def getpcname():
    print(socket.getfqdn())

def getlocalip():
    host = socket.getaddrinfo(socket.gethostname(), None)
    ipv4_addresses = [i[4][0] for i in host if i[0] == socket.AF_INET]
    print(ipv4_addresses)

def getdomainip(x):
    print(socket.gethostbyname(x))

def sitestatus(x):
    import requests
    import urllib.request
    from urllib.error import URLError
    try:
        urllib.request.urlopen("https://" + x)
        print("Сайт доступен")
        status = requests.get('https://' + x)
        print("Код сайта: ", status.status_code)
    except URLError:
        print("Сайт недоступен")

def sspeedtest():
    import speedtest
    st = speedtest.Speedtest()
    download = round(st.download() / 1048576)
    upload = round(st.upload() / 1048576)
    print("Скачивание: ", download, "МБ/С | " "Загрузка: ", upload, "МБ/С")

def getmac():
    from uuid import getnode
    import re
    print(':'.join(re.findall('..', '%012x' % getnode())))

def getmacnum():
    print(getnode())

def scanports(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.07)
    try:
        connect = sock.connect((ip, i))
        print("Порт ", i, " открыт")
        sock.close()
    except:
        pass

def genpass():
    import random
    variable = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    length = int(input("Введите длину пароль\n"))
    password = ""
    for i in range(length):
        password += random.choice(variable)
    print(password)

def scanportsv2(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.08)
    try:
        connect = sock.connect((ip, i))
        print("Порт ", i, " открыт")
        sock.close()
    except:
        pass

while "anime" == "anime":
    command = input()
    if command == "getip" or command == "мойайпи":
        getip()
    elif command == "getdhcp" or command == "получитьdhcp":
        getdhcp()
    elif command == "help" or command == "помощь":
        gethelp()
    elif command == "getpcname" or command == "имякомпа":
        print(socket.getfqdn())
    elif command == "getlocalip":
        getlocalip()
    elif "getdomainip" in command:
        domain = command[12:]
        getdomainip(domain)
    elif "айписайта" in command:
        domain1 = command[10:]
        getdomainip(domain1)
    elif "sitestatus" in command:
        siteforcheck = command[11:]
        sitestatus(siteforcheck)
    elif "статуссайта" in command:
        siteforcheck1 = command[12:]
        sitestatus(siteforcheck1)
    elif command == "speedtest" or command == "узнатьскорость":
        sspeedtest()
    elif command == "getmac" or command == "получитьмак":
        getmac()
    elif command == "getmacnum" or command == "получитьмакцифры":
        getmacnum()
    elif "rangeportsip" in command:
        na4alo = int(input("Введите начальный порт\n"))
        predel = int(input("Введите последний порт\n"))
        for i in range(na4alo, predel):
            scanports(command[13:])
    elif "диапазонпортовайпи" in command:
        na4alo1 = int(input("Введите начальный порт\n"))
        predel1 = int(input("Введите последний порт\n"))
        for i in range(na4alo1, predel1):
            scanports(command[19:])
    elif "rangeportsdomain" in command:
        na4alo2 = int(input("Введите начальный порт\n"))
        predel2 = int(input("Введите последний порт\n"))
        for i in range(na4alo2, predel2):
            scanports(socket.gethostbyname(command[17:]))
    elif "диапазонпортовдомен" in command:
        na4alo3 = int(input("Введите начальный порт\n"))
        predel3 = int(input("Введите последний порт\n"))
        for i in range(na4alo3, predel3):
            scanports(socket.gethostbyname(command[20:]))
    elif "проверитьпортыдомен" in command:
        ports = [7, 20, 21, 22, 23, 25, 53, 69, 80, 81, 110, 115, 143, 389, 443, 587, 993, 995, 2083, 2087, 2222, 3128, 3306, 5432, 8080, 8083]
        for i in ports:
            scanportsv2(socket.gethostbyname(command[20:]))
    elif "scanportsondomain" in command:
        ports = [7, 20, 21, 22, 23, 25, 53, 69, 80, 81, 110, 115, 143, 389, 443, 587, 993, 995, 2083, 2087, 2222, 3128, 3306, 5432, 8080, 8083]
        for i in ports:
            scanportsv2(socket.gethostbyname(command[19:]))
    elif "проверитьпортыайпи" in command:
        ports = [7, 20, 21, 22, 23, 25, 53, 69, 80, 81, 110, 115, 143, 389, 443, 587, 993, 995, 2083, 2087, 2222, 3128, 3306, 5432, 8080, 8083]
        for i in ports:
            scanportsv2(command[19:])
    elif "scanportsonip" in command:
        ports = [7, 20, 21, 22, 23, 25, 53, 69, 80, 81, 110, 115, 143, 389, 443, 587, 993, 995, 2083, 2087, 2222, 3128, 3306, 5432, 8080, 8083]
        for i in ports:
            scanportsv2(command[14:])
    elif command == "genpass" or command == "сделатьпароль":
        genpass()
    elif command == "getcoords" or command == "моикоординаты":
        import geocoder
        g = geocoder.ipinfo("me")
        print(g.latlng)
    elif "coordsbyip" in command:
        import geocoder
        g1 = geocoder.ipinfo(command[11:])
        print(g1.latlng)
    elif "координатыайпи" in command:
        import geocoder
        g2 = geocoder.ipinfo(command[15:])
        print(g2.latlng)
    elif "citybyip" in command:
        import geocoder
        g3 = geocoder.ipinfo(command[9:])
        print(g3.city)
    elif "городпоайпи" in command:
        import geocoder
        g4 = geocoder.ipinfo(command[12:])
        print(g4.city)
    else:
        print("Неверная команда. Вы можете ввести \"помощь\" для просмотра всех команд")