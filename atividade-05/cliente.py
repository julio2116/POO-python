import socket

server_address = ('127.0.0.1', 5000)

MSG = input("Informe a mesagem:\n")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           #Ao usar socket.SOCKET_STREAM, por padrão usamos o protocolo TCP

s.connect(server_address)                                       #Estabelece a conxão com o servidor
                                                                #.connect() espera receber uma tupla com com o IP e a porta
s.sendall(str.encode(MSG))                                      #Envia informações a conexão

data = s.recv(1024)

print(data)

s.close()

#TCP é um protocolo confiável que garante a transmissão de toda informação,
#pois considerando as limitações de internet, e processamento de cada dispositivo,
#é possível perda de parte dos dados