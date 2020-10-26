from socket import *
from gui.client_window import ClientWindow


if __name__ == '__main__':
    ip = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close())
          for s in [socket(AF_INET, SOCK_DGRAM)]][0][1]                    # -> получение ip

    client_app = ClientWindow()  # -> создание графического объекта
    client_app.open()  # -> запуск
