import socket
import threading

IP_SERV = '0.0.0.0'
PORTA_N = '5005'

def receber_client(conexao, endereco):
    print(f"{conexao} ativa de {endereco}")
    try:
        while True:
            dados = conexao.recv(1024)
            if not dados:
                break
            mensagem = dados.decode()
            print(f"Notificacao de {endereco}: {mensagem}")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        conexao.close()
        print(f"{endereco} desconectou")

def iniciar_servidor():
    socket_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        socket_serv.bind((IP_SERV, int(PORTA_N)))
        socket_serv.listen(5)
        print(f"Servidor iniciado: {IP_SERV}:{PORTA_N}")
        print("Aguardando midia do client")
        while True:
            conexao, endereco = socket_serv.accept()
            thread_serv = threading.Thread(target=receber_client, args=(conexao, endereco))
            thread_serv.start()

            print(f"Conexoes ativas: {threading.active_count() - 1}")
    except Exception as e:
        print(f"Falha no servidor: {e}")
    finally:
        print(f"Cliente desconectou")
        socket_serv.close()

iniciar_servidor()