import socket

def server():
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ('127.0.0.1', 5000)                             #host vazio sinaliza que o servidor aceitra conexões de qualquer fonte interna, mas obrigatoriamente o computador precisa saber qual porta "escuta" as requisições, é equivalente a 0.0.0.0 para IPv4 e :: para IPv6, 127.0.0.1 e localhost aceitariam apenas conexões internas

    s.bind(server_address)                                  #.bind() espera receber uma tupla com com o IP e a porta, por conta de socket.AF_INET, passado como primeiro argumento em socket.socket() (IPv4)
    # s.listen(1)                                             #Número de conexões em fila esperando ser processadas, após alcançar o limite as novas conexões serão recusadas, esta função apenas espera uma conexão e então chama .accept()

    # connection, address = s.accept()                        #Retorna um novo objeto do tipo socket, uma nova conexão diferente da de .listen(), para envio e recebimento de dados
    # print(address)

    data, address = s.recvfrom(1024)
    # while True:
        # data = connection.recv(1024)                            #Variavel conn, nunca havia sido declarada, recebe informações do cliente, 1024 é a quantidade máxima de dados a ser recebida de cada vez
        # if not data:                                            #Havia um erro que tentava enviar data quando a conexão s estava fechada
            # break
    print(data)
    MSG = data.decode().upper()
    s.sendto(str.encode(MSG), address)                     #Usar .send() faria com que tivessemos que checar se todos os dados foram enviados e então chamar .send() quantas vezes forem necessárias

                                      #Neste ponto existem dois sockets abertos, por isso ambos devem ser fechados, s sendo o servidor ouvindo requisições e connection sendo a conexão de transmissão de dados, aberta sempre que uma requisição é recebida
    s.close()                                               #O garbage colector do python realiza o close() automaticamente se for necessário, porém é uma má prática não fazer isso de forma esplicita

server()