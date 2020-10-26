from threading import Thread
from lib.server import Server
from lib.client import Client
from tkinter import Label, Entry, Button


class MyServerThread(Thread):  # -> класс поток сервера
    def __init__(self, server: Server, lbl: Label):
        super().__init__()
        self.__server = server
        self.__lbl = lbl

    def run(self):  # -> запускает поток
        self.__server.work_gui(self.__lbl)


class MyClientThread(Thread):  # -> класс поток клиента
    def __init__(self, server: Client, lbl: Label, entry: Entry, button: Button):
        super().__init__()
        self.__server = server
        self.__lbl = lbl
        self.__entry = entry
        self.__button = button

    def run(self):  # -> запускает поток
        self.__server.work_gui(self.__lbl, self.__entry, self.__button)
