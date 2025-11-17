import socket

def clientRequest(msg):
    server_address = (socket.gethostname(), 5000)                   #Trocar o host pela função .gethostname() retorna o Ip de rede local

    MSG = msg

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           #Ao usar socket.SOCKET_STREAM, por padrão usamos o protocolo TCP

    s.connect(server_address)                                       #Estabelece a conxão com o servidor
                                                                    #.connect() espera receber uma tupla com com o IP e a porta
    s.sendall(str.encode(MSG))                                      #Envia informações a conexão

    data = s.recv(1024)

    print(data)

    s.close()

msg = input("Informe a mesagem:\n")
clientRequest(msg)

#TCP é um protocolo confiável que garante a transmissão de toda informação,
#pois considerando as limitações de internet, e processamento de cada dispositivo,
#é possível perda de parte dos dados