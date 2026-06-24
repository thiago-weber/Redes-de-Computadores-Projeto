import threading
import socket
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

IP_PC = '192.168.1.129'
PORTA_N = '5005'

caminho_midias = "/midia/midia/"

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket_client.connect((IP_PC, int(PORTA_N)))
except Exception as e:
    print(f"Erro: {e}")

class notificarEventos(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            mensagem = f"Novo arquivo na pasta: {event.src_path}"
            print(mensagem)
            try:
                socket_client.sendall(mensagem.encode())
            except Exception as e:
                print(f"Erro: {e}")

handler = notificarEventos()
observador = Observer()
observador.schedule(handler, caminho_midias, recursive = True)

def monitorar():
    print(f"Monitorando a pasta: {caminho_midias}")
    observador.start()
    try:
        observador.join()
    except KeyboardInterrupt:
        observador.stop()
    observador.join()

thread_monitorar = threading.Thread(target=monitorar, daemon = True)
thread_monitorar.start()

try:
    input("Aperte Enter para finalizar...\n")
except KeyboardInterrupt:
    pass
finally:
    observador.stop()
    observador.join()
    socket_client.close()
    print("Monitoramento e conexao finalizados")