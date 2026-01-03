import socket,pickle,asyncio
from rich import print
def pyos():
    from pyos import pyos64
    from kernel import compilador
    return pyos64,compilador
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Porta não privilegiada (>1024)
mode = {b"x11":"screen","asm":"code"}
version=1
class air():
    def __init__(self,arch:str,name:str,host:str=HOST,port:int=PORT):
        self.socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host=host
        self.port=port
        self.arch=arch
        self.name=name
class server(air):
    def __init__(self,arch:str,name:str,host:str=HOST,port:int=PORT):
        super().__init__(arch,name,host,port)
        # print(self.host,self.port)
        self.socket.bind((self.host,self.port))
        self.socket.listen()
        self.code=[]
        if __name__==".":
            self.socket=self.socket
        self.conn={}
        print(self.__dict__)
        self.micro_id={}
        self.socket.listen()
        self.down=False
    async def search(self):
        self.down = 1
        loop = asyncio.get_running_loop()
        print("inicio")
        conn, addr = await loop.run_in_executor(None, self.socket.accept)
        self.last_id = addr[0]
        self.conn[addr[0]] = conn
        self.down = 0
        print("last id",addr[0])
    def activate(self,addr):
        print(f"{addr} trying to connect")
        self.micro_id[addr]= self.conn[addr].recv(1024).decode()
        print(self.micro_id,"micro id recived")
        print("first step finished , trying to send metadata")
        intern=f"{self.name}@{self.arch}"
        self.conn[addr].sendall(intern.encode())
        confirm:bytes=self.conn[addr].recv(len(intern))
        if confirm.decode()==intern:
            print("metadata passed, stable connection")
        else:
            print("meta erro",confirm.decode())
    def get(self,addr):
        # print(f"geting data from {self.micro_id}")
        tip=self.conn[addr].recv(3).decode()
        buffer_size=int.from_bytes(self.conn[addr].recv(16))
        brute=self.conn[addr].recv(buffer_size)
        if tip=="obj":
            data=pickle.loads(brute)
        elif tip=="str":
            data=brute.decode()
        elif tip=="asm":
            data=pickle.loads(brute)
            self.code.append()
        else:
            print(tip)
            return None
        return data
    def send_obj(self,info:object):
        data=pickle.dumps(info)
        self.conn.sendall(b"obj")
        lens=len(data).to_bytes(16)
        self.conn.sendall(lens)
        self.conn.sendall(data)
    def send_str(self,info:str):
        data=info.encode()
        self.conn.sendall(b"str")
        lens=len(data).to_bytes(16)
        self.conn.sendall(lens)
        self.conn.sendall(data)
class client(air):
    def __init__(self,arch:str,name:str,host:str=HOST,port:int=PORT):
        super().__init__(arch,name,host,port)
        while True:
            try:
                if self.socket.connect_ex((self.host,self.port)):
                    break
            except:
                pass
        self.socket.sendall(f"{self.name}@{self.arch}".encode())
        self.micro_id=self.socket.recv(1024).decode()
        print(f"server micro_id {self.micro_id}")
        print(f"confirming metadata to {self.host} server host")
        self.socket.sendall(self.micro_id.encode())
    def get(self):
        print(f"geting data from {self.micro_id}")
        tip=self.socket.recv(3)
        buffer_size=int.from_bytes(self.socket.recv(16))
        brute=self.socket.recv(buffer_size)
        if tip=="obj":
            data=pickle.loads(brute)
        elif tip=="str":
            data=brute.decode()
        elif tip=="asm":
            data=pickle.loads(brute)
            self.code.append()
        return data
    def send_obj(self,info:object):
        data=pickle.dumps(info)
        self.socket.sendall(b"obj")
        lens=len(data).to_bytes(16)
        self.socket.sendall(lens)
        self.socket.sendall(data)
    def send_str(self,info:str):
        data=info.encode()
        self.socket.sendall(b"str")
        lens=len(data).to_bytes(16)
        self.socket.sendall(lens)
        self.socket.sendall(data)
print("Wireless air protocol started")
# 1. Criar o objeto socket (AF_INET = IPv4, SOCK_STREAM = TCP)
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     # 2. Vincular o socket ao endereço e porta
#     s.bind((HOST, PORT))
#     # 3. Escutar conexões
#     s.listen()
#     print(f"Servidor ouvindo em {HOST}:{PORT}...")
    
#     # 4. Aceitar a conexão do cliente
#     conn, addr = s.accept()
#     with conn:
#         print(f"Conectado por {addr}")
#         while True:
#             # 5. Receber dados
#             data = conn.recv(1024)
#             if not data:
#                 break
#             print(f"Recebido: {data.decode()}")
#             # 6. Enviar resposta
#             conn.sendall(b"Mensagem recebida")

# 1. Criar o objeto socket
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # 2. Conectar ao servidor
# client_socket.connect((HOST, PORT))

# # 3. Enviar dados
# client_socket.sendall(b'Ola, servidor!')

# # 4. Receber resposta
# data = client_socket.recv(1024)
# print('Recebido:', data.decode())

# # 5. Fechar a conexão
# client_socket.close()