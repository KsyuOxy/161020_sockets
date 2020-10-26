from socket import *
from gui.server_window import ServerWindow

if __name__ == '__main__':
    ip = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close())
          for s in [socket(AF_INET, SOCK_DGRAM)]][0][1]                    # -> получение ip

    server_app = ServerWindow()  # -> создание графического объекта
    server_app.open()  # -> запуск
