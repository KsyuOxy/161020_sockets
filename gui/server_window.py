from tkinter import *
from lib.server import Server
from socket import *
from lib.threads import MyServerThread


class ServerWindow:  # -> графический объект Окно сервера
    def __init__(self):
        self.__root = Tk()  # -> корневое окно
        self.__frame = Frame(self.__root)  # -> фрейм для виджетов
        self.__label = Label(self.__frame)  # -> отображает ip сервера
        self.__chat = Label(self.__frame)  # -> для вывода сообщений

        self.__host = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close())
                       for s in [socket(AF_INET, SOCK_DGRAM)]][0][1]  # -> получение ip

        self.__port = 9001  # номер порта
        self.__server = Server(self.__host, self.__port)  # -> создание объекта класса Server
        self.__server_thread = MyServerThread(self.__server, self.__chat)  # -> создание потока

    def config(self):  # -> параметры окна и виджетов
        self.__root.title('Серверный модуль')
        self.__root.geometry('500x700+700+50')
        self.__root.config(bg='PaleTurquoise')
        self.__root.resizable(True, False)

        self.__label.config(text=str(self.__host), font='Arial 12 bold', fg='SteelBlue')
        self.__chat.config(text=str(self.__host), font='Arial 10', fg='navy', justify=LEFT, width=100, wraplength=400)

    def layout(self):  # -> размещение виджетов
        self.__frame.pack(pady=15, padx=15)
        self.__label.pack(padx=15)
        self.__chat.pack(pady=15, padx=15)

    def open(self):  # -> запускает объект данного класса
        self.config()
        self.layout()
        self.__server_thread.daemon = True  # -> объявляет поток демоническим

        self.__server_thread.start()
        self.__root.mainloop()
