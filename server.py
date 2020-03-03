import socket
# Criando um objeto do tipo socket
sock = socket.socket()
# definindo as portas do servidor
host = 'localhost'
porta = 8080
# Informando ao socket qual será o endereço que ele ouvirá
# anexa o endereço ao socket
sock.bind((host, porta))

# 5 é o maximo de conexoes
sock.listen(5)

cliente = None

while True:
    
    if cliente is None:
        print("[Aguardando os clientes se conectarem...]")
        # Fica esperando a conexão e quando for aceita
        # joga a conexao em cliente e o endereço em endereco
        cliente, endereco = sock.accept()
        #prita o endeco do cliente
        print("Conexão recebida do seguinte endereço" , endereco)

    else:
        print("[Aguardando mensagem do cliente...]")
        # printa mensagem do cliente
        # decode converte de byte para string
        print(cliente.recv(1024).decode())

        resposta = input("Escreva algo para enviar para o cliente:")
        # retorna mensagem para o cliente
        # encode converte de string para byte
        cliente.send(resposta.encode())

