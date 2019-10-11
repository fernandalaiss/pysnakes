import socket

def Main():
    HOST = '127.0.0.1'
    PORT = 54321

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    #conectando ao servidor na porta configurada
    s.connect((HOST,PORT))

    msg = 'Mensagem'
    while True:
        s.sendall(msg.encode('ascii'))
        data = s.recv(1024)
        print('Mensagem recebida: ',str(data.decode('ascii')))

        #processamento do jogador
        #se morrer ou ganhar o jogo encerra 
        continua = 'n'
        if continua == 's':
            continue
        else:
            s.sendall(("out").encode('ascii'))
            break
    s.close()

if __name__ == "__main__":
    Main()