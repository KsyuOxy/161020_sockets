from socket import *
from tkinter import Label, Entry, Button
from tkinter import messagebox


class Client(object):
    def __init__(self, host, port, name):
        self.__host = host  # -> хост
        self.__port = port  # -> порт
        self.__address = (self.__host, self.__port)  # -> адрес
        self.__client = None
        self.__name = name  # -> имя клиента

    def connect(self):  # -> соединение
        if self.__client is None:
            self.__client = socket(AF_INET, SOCK_STREAM)  # -> создание сетевого сокета
            self.__client.connect(self.__address)  # -> соединение с сервером

    def work_gui(self, label: Label, entry: Entry, button: Button):  # -> определяет рабочий процесс

        def _append_label_text(new_text: str):  # -> формирует текст в виджете сообщений
            current_text = label.cget('text')
            current_text += '>>> ' + new_text + '\n'
            label.configure(text=current_text)

        _append_label_text(f'{self.__name}, введите сообщение:')

        def send_mess():
            mess = self.__name + ': ' + entry.get()  # -> формирует текст сообщения
            _append_label_text(mess)  # -> выводит в виджет

            data = str.encode(mess)  # -> кодирует сообщение
            self.connect()  # -> соединяется с сервером
            self.__client.send(data)  # -> отправляет сообщение
            _append_label_text('Сообщение отправлено')

            data = self.__client.recv(1024)  # -> читает данные из сокета; размер сообщ 1024 байт
            response = bytes.decode(data)  # -> раскодирывает сообщ из байтов в str
            _append_label_text(response)

            self.__client.close()  # -> закрывает сокет
            self.__client = None
            entry.delete(0, 'end')  # -> очищает поле ввода
            _append_label_text('Вы хотите продолжить (y/n)?')

            def get_answer():
                answer = entry.get()
                if answer == 'n':
                    messagebox.showwarning("Внимание!", "Вы подтвердили окончание работы программы.")
                    raise SystemExit  # -> выход из приложения
                else:
                    entry.delete(0, 'end')
                    _append_label_text(f'{self.__name}, введите сообщение:')
                    button.config(command=send_mess)

            button.config(command=get_answer)

        button.config(command=send_mess)
