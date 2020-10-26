from tkinter import *
from lib.client import Client
from socket import *
from lib.threads import MyClientThread


class ClientWindow:  # -> графический объект Окно клиента
    def __init__(self):
        self.__root = Tk()  # -> корневое окно
        self.__frame = Frame(self.__root)  # -> фрейм для виджетов
        self.__label = Label(self.__frame)  # -> отображает ip сервера
        self.__chat = Label(self.__frame)  # -> для вывода сообщений
        self.__entry_mess = Entry(self.__root)  # -> для ввода сообщений
        self.__btn = Button(self.__root)  # -> кнопка отправить сообщение

        self.__host = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close())
                       for s in [socket(AF_INET, SOCK_DGRAM)]][0][1]            # -> получение ip

        self.__port = 9001  # номер порта
        self.__server = Client(self.__host, self.__port, "Oksana")  # -> создание объекта класса Client
        self.__client_thread = MyClientThread(self.__server, self.__chat, self.__entry_mess, self.__btn)  # -> создание
        #                                                                                                    # потока

    def config(self):  # -> параметры окна и виджетов
        self.__root.title('Клиентский модуль')
        self.__root.geometry('500x700+100+50')
        self.__root.configure(bg='RosyBrown')
        self.__root.resizable(True, False)

        self.__label.config(text=str(self.__host), font='Arial 12 bold', fg='LightCoral')
        self.__chat.config(text=str(self.__host), font='Arial 10', fg='navy', justify=LEFT, width=100, wraplength=400)
        self.__entry_mess.config(font='Arial 10', bg='LightCyan', width=66)
        self.__btn.config(text='Отправить', bg='white')

    def layout(self):  # -> размещение виджетов
        self.__frame.pack(pady=15, padx=15)
        self.__label.pack(padx=15)
        self.__chat.pack(pady=15, padx=15)
        self.__entry_mess.place(height=40, x=15, y=600)
        self.__btn.place(x=413, y=650)

    def open(self):  # -> запускает объект данного класса
        self.config()
        self.layout()
        self.__client_thread.daemon = True  # -> объявляет поток демоническим
        self.__client_thread.start()

        self.__root.mainloop()
