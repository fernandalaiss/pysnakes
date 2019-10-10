from _thread import *
import threading
import socket

lock = threading.Lock()

def thread_cliente(conn):
    while True:
        #receber informações do jogador
        data = conn.recv(1024) 
        #se não mandar mais informações o jogador morreu e deve ser exibida tela de game over ou de ganhador
        if not data: 
            print('GameOver ou Parabéns')
            #jogador desbloqueando com o lock
            lock.release() 
            break
  
        # reverse the given string from client // não sei o qe fazer aqui ainda mas é o processamento do jogo
        #data = data[::-1] 
  
        # send back reversed string to client // mandar info do jogo pro cliente
        conn.send(data) 
  
    #conexão finalizada com o cliente pois o mesmo morreu ou ganhou
    conn.close()

def Main():
    #host posteriormente pode ter valor "", significa que pode se conectar com todas as interfaces IPV4 disponíveis
    HOST = '127.0.0.1'
    #port escolhida possibilitar a conexão
    PORT = 54321

    #criando um contexto de atuação para o objeto socket
    #AF_INET é o endereço para IPV4
    #SOCK_STREAM é a referência para a conexão do tipo TCP, o protocolo de internet que será usado para transmitir e receber mensagens
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #bins associa nossa conexão com a interface de network escolhida e a porta TCP que trás a conexão de clientes
        s.bind((HOST,PORT))
        print('Configurada a interface de conexão na porta', PORT)

        #fazendo a interface encontrar conexões na porta
        s.listen()

        #criando conexões até que os clientes encerrarem
        while True:
            #estabelecendo conexão com um cliente
            conn, addr = s.accept()
            #cliente bloquando com o lock
            lock.acquire()
            print('Conectado com ', addr[0],':', addr[1])

            #iniciando uma nova thread para controlar o cliente
            start_new_thread(thread_cliente, (conn,))
            

if __name__ == "__main__":
    Main()    