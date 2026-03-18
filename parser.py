from lexer_risc import lexar as risclx0
from lexer_pyos import lexar as pyoslx1
from pyos import __mems__ ,risc_v as rv_core
from json import loads
from sereal import generator as  dumper

import time
def medir_tempo(func):
    """Decorator simples pra medir qualquer função"""
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()
        print(f"⏱️  {func.__name__} levou {fim - inicio:.6f} segundos")
        return resultado
    return wrapper
def somar_(a,b):
    return a+b
def subtrair_(a,b):
    return a+b
def dividir_(a,b):
    return a+b
def multiplicar_(a,b):
    return a+b
operacao={
    "+":somar_,
    "-":subtrair_,
    "*":multiplicar_,
    "/":dividir_
}
class riscv:
    page=4096
    mod={
        ".data":0,
        ".rodata":page,
        ".bss":page*2
        }
    
    rcha={
        "@object":".data",
        "@function":".text",
        '@progbits':".text"
    }
    n_m={
        "zero":0,
        "ra":1,
        "sp":2,
        "gp":3,
        "tp":4,
        "t0":5,
        "t1":6,
        "t2":7,
        "s0":8,
        "fp":8,
        "s1":9,
        "a0":10,
        "a1":11,
        "a2":12,
        "a3":13,
        "a4":14,
        "a5":15,
        "a6":16,
        "a7":17,
        "s2":18,
        "s3":19,
        "s4":20,
        "s5":21,
        "s6":22,
        "s7":23,
        "s8":24,
        "s9":25,
        "s10":26,
        "s11":27,
        "t3":28,
        "t4":29,
        "t5":30,
        "t6":31
    }
    last_globl=""
    
    def __init__(self,did:str,cpu:rv_core):
        self.tokens=risclx0(did,True)
        self.__code__=[]
        self.__memory__= __mems__(1024)
        self.__labels__={}
        self.__pos__=0
        self.cpu=cpu
    @medir_tempo
    def init(self):
        nsect=[]
        mode=True
        data_include=(".data", ".rodata", ".bss",".sdata", ".srodata", ".sbss")
        temp0=""
        math=""
        temp1={}
        temp2=0
        temp3=[]
        temp4=False
        types={

        }
        data_pos=0
        print([x for x in enumerate(self.tokens)])
        posicao=0
        # return
        while posicao<len(self.tokens):
            typer,text=self.tokens[posicao]
            text:str
            typer:str
            # print("analynzing :",typer,text)
            if typer=="SECTION":
                mode= (text in data_include)==True
                # print(text)
                # if mode:
                #     print("data mode")
                # else:
                #     print("text mode")
            elif typer=="LABEL":
                label=text.replace(":",'')
                if label in types:
                    mode= types[label] in data_include
                    print(f"{label} tranferido para {types[label]}")
                if mode or text.startswith("."):
                    mode=True
                    self.__labels__[label]=data_pos
                else:
                    mode=False
                    self.__labels__[label]=len(self.__code__)
            elif typer=="SYMBOL" and mode:
                x1=1
                opera="+"
                print(f"posição {posicao} e x1 {x1} lengh {len(self.tokens)}")
                tx,txt=self.tokens[posicao+x1]
                
                if tx=="DYNATT":
                    x1=2
                    self.__labels__[text]=0
                    while True:
                        tx,txt=self.tokens[posicao+x1]
                        print("analisando ",txt," sobre ",text)
                        if tx=="CURRENT_POS":
                            self.__labels__[text]=operacao[opera](
                                self.__labels__[text],
                                data_pos)
                        elif tx=="DIRECIVE":
                            self.__labels__[text]=operacao[opera](
                                self.__labels__[text],
                                int(txt)
                            )
                        elif tx=="SYMBOL":
                            self.__labels__[text]=operacao[opera](
                                self.__labels__[text],
                                int(self.__labels__[txt])
                            )
                        elif tx=="LINE":
                            x1+= 1
                            tx,txt=self.tokens[posicao+x1]
                            if tx=="LINEB":
                                x1+=1
                            else:
                                break
                        x1+=1
                    posicao+=x1
            elif typer=="DIRECTIVE":
            #     
                match text:
                    case ".byte":
                        x1=1
                        while True:
                            tx,txt=self.tokens[posicao+x1]
                            if tx=="IMMEDIATE":
                                txt:str
                                if txt.startswith("0x"):
                                    self.__memory__[data_pos] = int(txt,16) & 0xFF
                                else:
                                    self.__memory__[data_pos] = int(txt) & 0xFF
                                data_pos += 1
                                x1+=1
                            elif tx=="COMMA":
                                x1+=1
                            else:
                                break

                    case ".space":
                        posicao+=1
                        size = int(self.tokens[posicao][1])
                        data_pos += size 
                    case ".align":
                        posicao+=1
                        align = 1 << int(self.tokens[posicao][1])
                        data_pos = (data_pos +align -1) & ~(align -1)
                    case ".type":
                        posicao+=1
                        a,value=self.tokens[posicao]
                        posicao+=1
                        a,tipo=self.tokens[posicao]
                        types[value]=tipo

            elif typer=="MNEMONIC":
                try:
                    self.__code__.append([getattr(self.cpu,text.replace(".","_")),[]])
                except:
                    print("not mapped",text)
                mode=False
                temp4=True
                x1=1
                gsilva=False
                while len(self.tokens)>posicao+x1:
                    if gsilva:
                        print("deu ruim")
                    tx,txt=self.tokens[posicao+x1]
                    print("tx e txt",tx,txt)
                    if tx=="IMMEDIATE":
                        txt:str
                        if txt.startswith("0x"):
                            self.__code__[-1][1].append(int(txt,16))
                        else:
                            self.__code__[-1][1].append(int(txt))
                        
                    elif tx=="MATH":
                        self.__code__[-1][-1].append(txt)
                    elif tx=="REGISTER":
                        if txt.startswith("x"):
                            self.__code__[-1][-1].append(int(txt.removeprefix("x")))
                        else:
                            self.__code__[-1][-1].append(self.n_m[txt])
                        
                    elif tx=="SYMMOD":
                        self.__code__[-1][-1].append([txt])
                        x1+=1
                        self.__code__[-1][-1][-1].append(self.tokens[posicao+x1][1])
                        
                    elif tx=="SYMBOL":
                        self.__code__[-1][-1].append(txt)
                        
                    elif tx=="LINE":
                        print("linha quebrada")
                        gsilva=True
                        break
                    x1+=1
            elif typer=="MOD":
                temp3.append(self.rcha[text])
            # 
            # elif typer=="IMMEDIATE":
            #     print(f"data mode : {mode}")
            #     if not temp4:
            #         temp3.append(int(text))
            #     elif temp4:
            #         # print(self.__code__)
            #         self.__code__[-1][1].append(int(text))
                    
            elif typer=="STRING":
                self.__memory__
                for char in text:
                    self.__memory__[data_pos] = ord(char)
                    data_pos += 1
                self.__memory__[data_pos] = 0  # null terminator
                data_pos += 1
            posicao+=1
class pyos64:
    page=4096
    mod={
        ".data":0
        }
    
    rcha={
        "@data":".data",
        "@code":".code",
        '@high':".high"
    }
    n_m={
        f"r{x}":x for x in range(64)

    }| {
        f"p{x}":x+32 for x in range(32)
    }| {
        f"m{x}":x*4 for x in range(16)
    }| {
        f"t{x}":x+16 for x in range(32)
    } | {"zero":0}
    last_globl=""
    
    def __init__(self,did:str,cpu:rv_core):
        # self.tokens=pyoslx1(did,True)
        self.tokens=tuple(tuple(x) for x in pyoslx1(did, True))
        self.__code__=[]
        self.__memory__= __mems__(10240)
        self.__labels__={}
        self.__pos__=0
        self.__high__={}
        self.cpu=cpu
        self.__last_data__=0
    @medir_tempo
    # @cython.locals(i=cython.int, token=cython.p_char)
    def init(self):
        nsect=[]
        mode=True
        data_include=(".data", ".high")
        temp0=""
        math=""
        temp1={}
        temp2=0
        temp3=[]
        temp4=False
        types={

        }
        last_label=""
        data_pos=0
        print([x for x in enumerate(self.tokens)])
        posicao=0
        # return
        while posicao<len(self.tokens):
            typer,text=self.tokens[posicao]
            text:str
            typer:str
            # print("analynzing :",typer,text)
            if typer=="SECTION":
                mode= (text in data_include)==True
                # print(text)
                # if mode:
                #     print("data mode")
                # else:
                #     print("text mode")
            elif typer=="LABEL":
                label=text.replace(":",'')
                if label in types:
                    mode= types[label] in data_include
                    # print(f"{label} tranferido para {types[label]}")
                if mode or text.startswith("."):
                    mode=True
                    self.__labels__[label]=data_pos
                else:
                    mode=False
                    self.__labels__[label]=len(self.__code__)
                last_label=label
            elif typer=="SYMBOL" and mode:
                x1=1
                opera="+"
                # print(f"posição {posicao} e x1 {x1} lengh {len(self.tokens)}")
                tx,txt=self.tokens[posicao+x1]
                
                if tx=="DYNATT":
                    x1=2
                    self.__labels__[text]=0
                    while True:
                        tx,txt=self.tokens[posicao+x1]
                        # print("analisando ",txt," sobre ",text)
                        if tx=="CURRENT_POS":
                            self.__labels__[text]=operacao[opera](
                                self.__labels__[text],
                                data_pos)
                        elif tx=="DIRECIVE":
                            self.__labels__[text]=operacao[opera](
                                self.__labels__[text],
                                int(txt)
                            )
                        elif tx=="SYMBOL":
                            self.__labels__[text]=operacao[opera](
                                self.__labels__[text],
                                int(self.__labels__[txt])
                            )
                        elif tx=="LINE":
                            x1+= 1
                            tx,txt=self.tokens[posicao+x1]
                            if tx=="LINEB":
                                x1+=1
                            else:
                                break
                        x1+=1
                    posicao+=x1
            elif typer=="DIRECTIVE":
            #   
                match text:
                    case ".byte":
                        x1=1
                        while True:
                            tx,txt=self.tokens[posicao+x1]
                            if tx=="IMMEDIATE":
                                txt:str
                                if txt.startswith("0x"):
                                    self.__memory__[data_pos] = int(txt,16) & 0xFF
                                else:
                                    self.__memory__[data_pos] = int(txt) & 0xFF
                                data_pos += 1
                                x1+=1
                            elif tx=="COMMA":
                                x1+=1
                            else:
                                break

                    case ".space":
                        posicao+=1
                        size = int(self.tokens[posicao][1])
                        data_pos += size 
                    case ".align":
                        posicao+=1
                        align = 1 << int(self.tokens[posicao][1])
                        data_pos = (data_pos +align -1) & ~(align -1)
                    case ".type":
                        posicao+=1
                        a,value=self.tokens[posicao]
                        posicao+=1
                        a,tipo=self.tokens[posicao]
                        types[value]=tipo
                    case ".string":
                        posicao+=1
                        a,value=self.tokens[posicao]
                        for char in value[1:-2]:
                            self.__memory__[data_pos] = ord(char)
                            data_pos += 1
                        self.__memory__[data_pos] = 0  # null terminator
                        data_pos += 1
                    case ".array":
                        while True:
                            posicao+=1
                            a,key=self.tokens[posicao]
                            if a=="LBRACE":
                                break
                        # print("chamado")
                        if a == "LBRACE":
                            diciona= {}
                            temp=[]
                            # tempkey=[]
                            count=1
                            keymode=True
                            kkey=""
                            posicao+=1
                            # listmode=False
                            dictmode=True
                            histomode=[]
                            while count>0:
                                a,value=self.tokens[posicao]
                                # if dictmode:
                                #     print("dictmode")
                                # print(f"len of eachother:{len(temp)==len(histomode)}")
                                # print(temp)
                                if dictmode:
                                    if a=="STRING":
                                        value=value[1:-1]
                                        # print(f"keymode {keymode}")
                                        if keymode:
                                            kkey=value
                                        else:
                                            if len(temp)>0:
                                                # print(f"usado: {kkey} = {value}")
                                                temp[-1][kkey]=value
                                                keymode=True
                                            else:            
                                                # print("did it")                            
                                                diciona[kkey]=value
                                                keymode=True
                                    elif a=="IMMEDIATE" and not keymode:
                                        if value.startswith("0x"):
                                            valor=int(value,16)
                                        else:
                                            valor=int(value)
                                        if len(temp)>0:
                                            temp[-1][kkey]=valor
                                        else:            
                                            # print("did it")                            
                                            diciona[kkey]=valor
                                        keymode=True
                                    elif a=="COLON":
                                        keymode=False
                                    elif a=="LBRACE":
                                        temp.append({})
                                        histomode.append([True,kkey])
                                        kkey="$"
                                        keymode=True
                                    elif a=="LBRACKET":
                                        # print(f"{temp}\n\n{tempkey}\n\n")
                                        temp.append([])
                                        histomode.append([True,kkey])
                                        dictmode=False
                                    elif a=="RBRACE":
                                        # print(len(tempkey))
                                        if len(temp)>0:
                                            valor=temp.pop()
                                        else:
                                            break
                                        # print(f"valor atribuido {valor}, kkey {kkey}, len {len(tempkey)}")
                                        if len(histomode)==1:
                                            diciona[histomode[-1][1]]=valor
                                        elif len(histomode)>1:
                                            if histomode[-1][0]:
                                                popado=histomode[-1][1]
                                                # print(f"popado {popado}")

                                                keymode=True
                                                try:

                                                    temp[-1][popado]=valor
                                                except:
                                                    break
                                            else:
                                                temp[-1].append(valor)
                                        elif len(temp)==0:
                                            break
                                        dictmode,_=histomode.pop()
                                else:
                                    if a=="STRING":
                                        value=value[1:-1]
                                        temp[-1].append(value)
                                    elif a=="IMMEDIATE":
                                        if value.startswith("0x"):
                                            valor=int(value,16)
                                        else:
                                            valor=int(value)
                                        temp[-1].append(valor)
                                    elif a=="LBRACE":
                                        # print(f"{temp}\n{len(temp)==len(histomode)}\n{tempkey}\n\n")
                                        temp.append({})
                                        histomode.append([False,None])
                                        kkey="$"
                                        dictmode=True
                                        keymode=True
                                    elif a=="LBRACKET":
                                        temp.append([])
                                        histomode.append(False,None)
                                    elif a=="RBRACKET":
                                        # print("colchete fechado")
                                        valor=temp.pop()
                                        # print(f"valor atribuido {valor}")
                                        if histomode[-1][0]==True:
                                            try:
                                                temp[-1][histomode[-1][1]]=valor
                                                keymode=True
                                            except:
                                                # print(histomode[-1])
                                                raise
                                        else:
                                            temp[-1].append(valor)
                                        dictmode,_=histomode.pop()
                                        
                                posicao+=1
                            hj=dumper([diciona])
                            ff=hj.dump()
                            self.__labels__[last_label]=data_pos
                            # print(hj.reverts(ff))
                            for bit in ff:
                                self.__memory__[data_pos]=bit
                                data_pos+=1
                            self.__labels__[last_label+"_len"]=data_pos

            elif typer=="MNEMONIC":
                try:
                    self.__code__.append([getattr(self.cpu,text.replace(".","_")),[]])
                except:
                    print("not mapped",text)
                mode=False
                temp4=True
                x1=1
                gsilva=False
                while len(self.tokens)>posicao+x1:
                    # if gsilva:
                    #     print("deu ruim")
                    tx,txt=self.tokens[posicao+x1]
                    # print("tx e txt",tx,txt)
                    if tx=="IMMEDIATE":
                        txt:str
                        if txt.startswith("0x"):
                            self.__code__[-1][1].append([0,int(txt,16)])
                        else:
                            self.__code__[-1][1].append([0,int(txt)])
                        
                    elif tx=="MATH":
                        self.__code__[-1][-1].append(txt)
                    elif tx=="REGISTER":
                        # print(f"register {txt}, {self.n_m[txt]}")
                        self.__code__[-1][-1].append([1,self.n_m[txt]])
                    elif tx=="STRING":
                        self.__code__[-1][-1].append(txt)
                    elif tx=="SYMMOD":
                        self.__code__[-1][-1].append([txt])
                        self.__code__[-1][-1][-1].append(self.tokens[posicao+x1][1])
                    elif tx=="SYMBOL":
                        self.__code__[-1][-1].append(txt)
                    elif tx=="LINE":
                        # print("linha quebrada")
                        gsilva=True
                        break
                    x1+=1
            elif typer=="MOD":
                temp3.append(self.rcha[text])
            # 
            # elif typer=="IMMEDIATE":
            #     print(f"data mode : {mode}")
            #     if not temp4:
            #         temp3.append(int(text))
            #     elif temp4:
            #         # print(self.__code__)
            #         self.__code__[-1][1].append(int(text))
                    
            # elif typer=="STRING":
            #     self.__memory__
            #     for char in text:
            #         self.__memory__[data_pos] = ord(char)
            #         data_pos += 1
            #     self.__memory__[data_pos] = 0  # null terminator
            #     data_pos += 1
            posicao+=1
        self.__last_data__=data_pos
class make:
    def __init__(self,tokens):
        self.__tokens__=tokens
        self.__labels__={}
        self.__mode__=".text"
        self.__globl__="_start"
        self.__data__={}
        self.__code__=[]