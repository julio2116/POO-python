import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 5000)

s.bind(server_address)                                  #.bind() espera receber uma tupla com com o IP e a porta, por conta de socket.AF_INET, passado como primeiro argumento em socket.socket() (IPv4)
s.listen(1)                                             #Número de conexões em fila esperando ser processadas, após alcançar o limite as novas conexões serão recusadas, esta função apenas espera uma conexão e então chama .accept()

connection, address = s.accept()                        #Retorna um novo objeto do tipo socket, uma nova conexão diferente da de .listen(), para envio e recebimento de dados

data = connection.recv(1024)                            #Variavel conn, nunca havia sido declarada, recebe informações do cliente

if not data:
    connection.sendall(data)
print(data)
MSG = data.decode().upper()
connection.sendall(str.encode(MSG))

connection.close()
s.close()                                               #O garbage colector do python realiza o close() automaticamente se for necessário, porém é uma má prática não fazer isso de forma esplicita
