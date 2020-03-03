import socket
# cria um objeto
skt = socket.socket()
# Usnado o socket para se conectar ao host
skt.connect(('10.10.35.12', 8080))
print("Conectado ao seguinte servidor localhost")

while True:
    mensagem = input("escreva algo para enviar ao servidor:")

    skt.send(mensagem.encode())

    print("[Aguardando uma resposta do servidor...]")
    # recebe mensagem
    print(skt.recv(1024).decode())
