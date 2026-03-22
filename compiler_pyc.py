class io:
    print_asm=["mov r0 1\nmov r1 \x05\nmov r2 \x05.len\nstore 0 \x06\n","pycall r0 1 r1 r2\npycall r0 1 0 1"]
    def print(string:str,end="\n") -> list[str,str]:
        return [io.print_asm[0].replace("\x05",string).replace("\x06",str(int.from_bytes(end.encode()))),io.print_asm[1]]
    calls={
        "print":print
    }
    externo=[
        
    ]
include={
    "io":io
}
class start:
    def __init__(self,tokens:list[str]):
        self.tokens=tokens
        self.vars={}
        self.funcs={}
        self.__data__=[".space 4"]
        self.__include__={}
        self.__func__=[]
        self.__code__=[]
        self.__extern__=[]
        self.code=""
    def act(self):
        posicao=0
        size=len(self.tokens)
        expand=[]
        print(self.tokens)
        param_names=[]
        # print(size)
        while posicao<size:
            typer,text= self.tokens[posicao]
            # print("type",typer)
            match typer:
                case "RULE":
                    posicao+=1
                    tx,txt= self.tokens[posicao]
                    self.__include__=self.__include__|include[txt[1:-1]].calls
                case "TYPE":
                    if text in ["int", "str","byte"]:
                        posicao+=1
                        tx,txt1= self.tokens[posicao]
                        self.__data__.append(f":{txt1}:")
                        posicao+=2
                        tx,txt= self.tokens[posicao]
                        self.__data__.append(f".{text} {txt}")
                        self.__data__.append(f"{txt1}.len = . - {txt1}")
                    if text == "fn":
                        posicao+=1
                        tx,txt1=self.tokens[posicao]
                        txt1=txt1[:-1]
                        self.__code__.append(f"\n:{txt1}:")
                        temp=[]
                        state="none"
                        posicao+=1
                        while True:
                            tx,txt=self.tokens[posicao]
                            if tx =="ID" and state!="funct":
                                state="name"
                                temp.append(txt)
                            elif tx =="FID":
                                state="funct"
                                temp.append(txt[:-1])
                            elif tx =="RPAREN" and state=="funct":
                                s,sf=self.__include__[temp[0]](*temp[1:])
                                print(s)
                                self.__code__.append(s)
                                self.__code__.append(f"call {temp[0]}")
                                if not temp[0] in expand:
                                    self.__func__.append(f":{temp[0]}:\n{sf}\nret")
                                    expand.append(temp[0])
                                state="none"
                            elif tx =="STRING":
                                tempx=bytes([len(self.__data__)*len(param_names)%26+65]).decode()
                                self.__data__.append(f":{txt1}{tempx}:\n.str {txt}\n"+
                                                    f"{txt1}{tempx}.len = . - {txt1}{tempx}")
                            elif tx =="ID" and state=="funct":
                                print(txt,"added")
                                temp.append(txt)
                            elif tx =="RBRACE":
                                break
                            print(posicao)
                            posicao+=1
                        print(temp)
                case "FID":
                    temp=[]
                    state="none"
                    posicao+=1
                    while True:
                        tx,txt=self.tokens[posicao]
                        if tx =="ID":
                            state="name"
                            temp.append(txt)
                        elif tx =="RPAREN":
                            self.__code__.append(f"go p31 {text[:-1]}")
                            break
                        elif tx =="ID":
                            print(txt,"added")
                            temp.append(txt)
                        # print(posicao)
                        posicao+=1
                    print(temp)
            posicao+=1
        print(self.__code__)
        self.code=".data\n"+"\n".join(self.__data__)+"\n.code"+"\n".join(self.__code__)+"\nhalt\n"+"\n".join(self.__func__)