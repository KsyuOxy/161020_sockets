from socket import *
from time import ctime
from tkinter import Label
from tkinter import messagebox


class Server(object):
    def __init__(self, host, port):
        self.__host = host  # -> хост
        self.__port = port  # -> порт
        self.__address = (self.__host, self.__port)  # -> адрес
        self.__listener = socket(AF_INET, SOCK_STREAM)  # -> создание сетевого сокета

    def config(self):  # -> конфигурация
        self.__listener.bind(self.__address)  # -> инициализация ip и порта
        self.__listener.listen(15)  # -> количество клиентских соединений

    def work_gui(self, label: Label):  # -> определяет рабочий процесс
        self.config()

        def _append_label_text(new_text: str):  # -> формирует текст в виджете сообщений
            current_text = label.cget('text')
            current_text += '>>>' + new_text + '\n'
            label.configure(text=current_text)

        while True:
            _append_label_text('Сервер в режиме ожидания запросов на соединение')
            # -> блокир.приложение до получ.сообщ; присваивает conn - адресс
            conn, client = self.__listener.accept()
            _append_label_text(f'{ctime()}: получен запрос на соединение от {client}')

            data = conn.recv(1024)  # -> читает данные из сокета; размер сообщ 1024 байт
            mess = bytes.decode(data)  # -> раскодирывает сообщ из байтов в str

            name = mess[0:mess.find(':')]  # -> получ имя клиента
            text = mess[mess.find(':')+1:]  # -> получ сообщ клиента
            _append_label_text(f'{name} -> {text}')

            response = f'Сообщение от клиента {name}: [{text}] успешно доставлено'
            data = str.encode(response)  # -> кодирует сообщение
            conn.send(data)  # -> отправляет сообщение
            conn.close()  # -> закрывает сокет

            if text == ' StopServer2020111':  # -> условный код для остановки сервера от имени админа
                _append_label_text('Сервер остановлен по команде администратора')
                messagebox.showwarning("Внимание!", "Сервер остановлен по команде администратора.")
                break
