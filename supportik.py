import socket
print("Supportik v 1.2")
print("Автор: Данил Пистолетов")
print("Дата релиза - 15.07.2022")
print("DIVANNIE PARNI DEVELOPMENT")
print("USA - shit, fuck USA!\n")

def getip():
    import urllib.request
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    print(external_ip)

def getdhcp():
    print(socket.gethostbyname(socket.gethostname()))

def gethelp():
    print("""
    help - список команд и пояснение к ним
    getip - получение внешнего адреса компьютера
    getdhcp - получение вашего DHCP
    getpcname - получение имени вашего компьютера
    getdomainip [ДОМЕН] - получение IP сайта (вводить без http/https)
    sitestatus [ДОМЕН] - проверка статуса сайта (вводить без http/https)
    speedtest - измерение скорости скачивания и загрузки
    getmac - получить MAC-адрес
    getmacnum - получить MAC-адрес в виде числа
    scanportsonip - проверить открытые порты по IP
    scanportsondomain - проверить открытые порты по домену (вводить без http/https)
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
    sock.settimeout(0.5)
    try:
        connect = sock.connect((ip, i))
        print("Порт ", i, " открыт")
        sock.close()
    except:
        pass

while "anime" == "anime":
    command = input()
    if command == "getip":
        getip()
    elif command == "getdhcp":
        getdhcp()
    elif command == "help":
        gethelp()
    elif command == "getpcname":
        print(socket.getfqdn())
    elif command == "getlocalip":
        getlocalip()
    elif "getdomainip" in command:
        domain = command[12:]
        getdomainip(domain)
    elif "sitestatus" in command:
        siteforcheck = command[11:]
        sitestatus(siteforcheck)
    elif command == "speedtest":
        sspeedtest()
    elif command == "getmac":
        getmac()
    elif command == "getmacnum":
        getmacnum()
    elif "scanportsonip" in command:
        for i in range(1000):
            scanports(command[14:])
    elif "scanportsondomain" in command:
        ipforscan = (socket.gethostbyname(command[18:]))
        for i in range(1000):
            scanports(ipforscan)
    else:
        print("Неверная команда. Вы можете ввести \"help\" для просмотра всех команд")