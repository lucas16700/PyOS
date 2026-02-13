# from kernel import compilador
from random import randbytes,randint
# from json import dumps, loads
from lib import JA
# from lib.wprotoc import server,client
from time import time
from pickle import dumps as upld,loads as dowld
import pygame
from numba import jit,njit
import serializador,asyncio
from pympler import asizeof
from utils_grafic.surfs import surf
import asyncio
if __name__ =="mojang":
    from kernel import compilador as kernel # para eu editar no vs code
version=1.0
print("pyos booted")
def ps(*arg,**karg):
    pass
# depois de testes isso se tornou um peso desnessessario por conta da criação de wigets#
# que esta dentro de JA, que é sigla para Json Application
# atualmente uso esse cenario para fazer tudo no sistema
# class caching:
#     memory={}
#     def get(func):
#         def temp(self,__value):
#             if self.__value in caching.memory:
#                 return caching.memory[__value]
#             else:
#                 return func(self,__value)
#     def set(func):
#         def temp(self,__value):
class dinamica:
    @property
    def get_init_win(self):
        print("get init")
        return int(pygame.get_init())
class speed:
    @njit(cache=True)
    def add(a:int,b:int):
        c=a+b
        return c
    
    @njit(cache=True)
    def sub(a:int,b:int):
        c=a-b
        return c
    
    @njit(cache=True)
    def div(a:int,b:int):
        c=a/b
        return c
    
    @njit(cache=True)
    def mul(a:int,b:int):
        c=a*b
        return c
    
    @njit(cache=True)
    def until(a:int,b:int):
        c=a%b
        return c
    
    @njit(cache=True)
    def sqr(a:int,b:int):
        c=a**b
        return c
    
    @njit(cache=True)
    def root(a:int,b:int):
        c=a**(1/b)
        return c

def debuga(func):
    def nfunc(self:"pyos64",any):
        try:
            func(self,any)
        except:
            print(self.__pos__)
            print(any)
    return nfunc

class risc_v:
    INSTRUCTION_PATTERNS = {
        # FAKE i
        "sect_0_": ["out", "out", "out", "out", "out"],
        "label_0_": ["out", "out", "out", "out", "out"],

        # I-type (rd, rs1, imm)
        'addi':   ['out', 'in', 'in'],
        'addiw':  ['out', 'in', 'in'],
        'slti':   ['out', 'in', 'in'],
        'lb':     ['out', 'mem'],     # mem = offset(rs1)
        'lbu':    ['out', 'mem'],
        'lh':     ['out', 'mem'],
        'lw':     ['out', 'mem'],
        'ld':     ['out', 'mem'],

        # R-type (rd, rs1, rs2)
        'add':    ['out', 'in', 'in'],
        'sub':    ['out', 'in', 'in'],
        'and':    ['out', 'in', 'in'],
        'or':     ['out', 'in', 'in'],
        'xor':    ['out', 'in', 'in'],
        'sll':    ['out', 'in', 'in'],
        'srl':    ['out', 'in', 'in'],
        'sra':    ['out', 'in', 'in'],
        'slt':    ['out', 'in', 'in'],

        # S-type (rs2, imm(rs1)) — note: sem out!
        'sb':     ['in', 'mem'],      # rs2 é fonte (in), mem é destino
        'sh':     ['in', 'mem'],
        'sw':     ['in', 'mem'],
        'sd':     ['in', 'mem'],

        # Branches (rs1, rs2, label/offset)
        'beq':    ['in', 'in', 'label'],
        'bne':    ['in', 'in', 'label'],
        'blt':    ['in', 'in', 'label'],
        'bge':    ['in', 'in', 'label'],

        # Jumps
        'jal':    ['out', 'label'],   # rd, label
        'jalr':   ['out', 'mem'],     # rd, offset(rs1)

        # U-type
        'lui':    ['out', 'in'],      # rd, imm
        'auipc':  ['out', 'in'],

        # Pseudos
        'li':     ['out', 'in'],
        'la':     ['out', 'label'],
        'mv':     ['out', 'in'],
        'ret':    [],                 # sem args
        'nop':    [],

        # Syscall
        "ecall":  []
    }
    __data_sect_need__=True
    __inst_arr_need__=True
    def __init__(self,tread):
        self.tread=tread
        self.reg=self.__reg__(self)
        self.__code__=[]
        self.__stack__=[]
        self.__mem__={n:0 for n in range(128)}
        self.__ZF__=0
        self.__NF__=0
        self.__CF__=0
        self.__pos__=0
        self._debug_=False
        self.__func__={}
        self.__real__:kernel=tread
        self.__states__={}
        #self.__graf__=self.imagem_compose(self)
        self.__recursion__=[]
        self.__env__={}
        self.__ui__=JA.boot(self)
        self.__clock__=0
        self.__var__={}
        self.__events__={}
        self.__async_f__=[]
        self.__x__=1
        self.__labels__={}
        self.__data__={}
        self.__point__={}
        self.heap_start = 0x10000000  # endereço após .data
        self.heap_end = self.heap_start
        self.__sections__={
            "globl":"_start",
            "currenct":"",
            "section":".text",
        }
    class __reg__:
        def __init__(self,tread:"risc_v"):
            self.values={
                a:0 for a in range(32),
            }
            self.real=tread
            self.vari={
                "x":0,
                "a":10,
                "s":8,
                "t":5
            }
            self.history=[asizeof.asizeof(self)]
        def __getstate__(self):
            return self.values
        def __setstate__(self,values):
            self.values=values
        def __getitem__(self,__value:str):
            prefix=__value[0]
            f__value=
            try:
                # print(f"get {__value} -> {self.values[__value]}")
                return self.values[f__value]
            except:
                return 0
                # print(f"get --> {__value}")
                # print(__value)
                
        def __setitem__(self,__key,__value):
                try:
                    # print(f"set {__key} <- {__value}")
                    self.values[__key]=__value
                except:
                    self.real.__data__[__key]=__value
                    
                # self.history.append(asizeof.asizeof())
        def __repr__(self):
            return f"internal registers:\n{self.values}"
        def __str__(self):
            return str(self.values)
        def copy(self):
            copy=self.real.__reg__(self.real)
            copy.values=self.values.copy()
            return copy
    # Métodos existentes (mantive e ajustei)
    def nop(self,any):
        pass
    def sect_0_(self,any): # .text | .string
        # print(f"section {any[0]}")
        pass
    def label_0_(self,any): #label: | variavel: .alguma coisa
        # print(f"label {any[0]}")
        pass
    def NONES_label_space(self,any=None):
        pass
    def li(self, any):
        rd, imm = any[0], int(any[1])
        self.reg[rd] = imm

    def la(self, any):
        rd, label = any[0], any[1]
        # Assume label resolvido para endereço (ex.: de .data)
        self.reg[rd] = label  # ou endereço virtual
    def lb(self, any):
        """
        lb rd, offset(rs1)
        any = [rd, offset, rs1]   # ex.: ['t0', 0, 'a1']
        """
        rd = any[0]          # registrador destino
        offset = int(any[1][0]) # pode ser string ou int, converta
        rs1 = any[1][0]         # registrador base

        # Calcula endereço
        base_addr = self.reg[rs1]
        addr = base_addr + offset

        # Lê 1 byte da memória
        byte_val = self.__mem__.get(addr, 0) & 0xFF  # garante 0-255

        # Extensão de sinal (signed byte → int64)
        if byte_val & 0x80:  # bit de sinal ligado (128-255)
            byte_val -= 256   # transforma em -128 a -1

        self.reg[rd] = byte_val
    def sb(self, any):
        """
        sb rs2, offset(rs1)
        any = [rs2, offset, rs1]   # ex.: ['t0', 0, 'a1']
        """
        print(any)
        rs2 = any[0]          # registrador que contém o byte a escrever
        offset = int(any[1])
        rs1 = any[2]          # registrador base

        # Calcula endereço
        base_addr = self.reg[rs1]
        addr = base_addr + offset

        # Pega só o byte menos significativo (0–255)
        byte_val = self.reg[rs2] & 0xFF

        # Escreve na memória
        self.__mem__[addr] = byte_val
    def sh(self, any):
        rs2 = any[0]
        offset = int(any[1])
        rs1 = any[2]
        addr = self.reg[rs1] + offset
        half_val = self.reg[rs2] & 0xFFFF  # 16 bits
        self.__mem__[addr]   = half_val & 0xFF
        self.__mem__[addr+1] = (half_val >> 8) & 0xFF
    def sw(self, any):
        rs2 = any[0]
        offset = int(any[1])
        rs1 = any[2]
        addr = self.reg[rs1] + offset
        word_val = self.reg[rs2] & 0xFFFFFFFF  # 32 bits
        for i in range(4):
            self.__mem__[addr + i] = (word_val >> (i*8)) & 0xFF
    def addi(self, any):
        rd, rs1, imm = any[0], any[1], int(any[2])
        self.reg[rd] = self.reg[rs1] + imm

    def add(self, any):
        rd, rs1, rs2 = any[0], any[1], any[2]
        self.reg[rd] = self.reg[rs1] + self.reg[rs2]

    def lui(self, any):
        rd, imm = any[0], int(any[1])
        # Carrega 20 bits altos + zeros baixos
        self.reg[rd] = (imm << 12) & 0xFFFFFFFFFFFFF000  # sign-extend se necessário

    def auipc(self, any):
        rd, imm = any[0], int(any[1])
        # AUIPC: endereço atual + upper imm
        self.reg[rd] = self.__pos__ + (imm << 12)

    def sub(self, any):
        rd, rs1, rs2 = any[0], any[1], any[2]
        self.reg[rd] = self.reg[rs1] - self.reg[rs2]

    def mul(self, any):
        rd, rs1, rs2 = any[0], any[1], any[2]
        self.reg[rd] = self.reg[rs1] * self.reg[rs2]  # Assumindo M extension

    def div(self, any):
        rd, rs1, rs2 = any[0], any[1], any[2]
        if self.reg[rs2] == 0:
            # Trap ou erro (implemente exception)
            print("Divisão por zero!")
            return
        self.reg[rd] = self.reg[rs1] // self.reg[rs2]  # signed div

    def and_(self, any):  # Renomeei para and_ pois 'and' é keyword Python
        rd, rs1, rs2 = any[0], any[1], any[2]
        self.reg[rd] = self.reg[rs1] & self.reg[rs2]

    def or_(self, any):
        rd, rs1, rs2 = any[0], any[1], any[2]
        self.reg[rd] = self.reg[rs1] | self.reg[rs2]

    def xor(self, any):
        rd, rs1, rs2 = any[0], any[1], any[2]
        self.reg[rd] = self.reg[rs1] ^ self.reg[rs2]

    def sll(self, any):
        rd, rs1, rs2 = any[0], any[1], any[2]
        self.reg[rd] = self.reg[rs1] << self.reg[rs2]

    def srl(self, any):
        rd, rs1, rs2 = any[0], any[1], any[2]
        self.reg[rd] = self.reg[rs1] >> self.reg[rs2]  # logical right

    def sra(self, any):
        rd, rs1, rs2 = any[0], any[1], any[2]
        self.reg[rd] = self.reg[rs1] >> self.reg[rs2]  # arithmetic right (preserva sinal)

    def slt(self, any):
        rd, rs1, rs2 = any[0], any[1], any[2]
        self.reg[rd] = 1 if self.reg[rs1] < self.reg[rs2] else 0  # signed

    def sltu(self, any):
        rd, rs1, rs2 = any[0], any[1], any[2]
        self.reg[rd] = 1 if abs(self.reg[rs1]) < abs(self.reg[rs2]) else 0  # unsigned

    def beq(self, any):
        rs1, rs2, label = any[0], any[1], any[2]
        if self.reg[rs1] == self.reg[rs2]:
            self.__pos__ = self.__labels__[label]

    def bne(self, any):
        rs1, rs2, label = any[0], any[1], any[2]
        if self.reg[rs1] != self.reg[rs2]:
            self.__pos__ = self.__labels__[label]

    def blt(self, any):
        rs1, rs2, label = any[0], any[1], any[2]
        if self.reg[rs1] < self.reg[rs2]:  # signed
            self.__pos__ = self.__labels__[label]

    def bge(self, any):
        rs1, rs2, label = any[0], any[1], any[2]
        if self.reg[rs1] >= self.reg[rs2]:
            self.__pos__ = self.__labels__[label]

    def bltu(self, any):
        rs1, rs2, label = any[0], any[1], any[2]
        if abs(self.reg[rs1]) < abs(self.reg[rs2]):  # unsigned
            self.__pos__ = self.__labels__[label]

    def bgeu(self, any):
        rs1, rs2, label = any[0], any[1], any[2]
        if abs(self.reg[rs1]) >= abs(self.reg[rs2]):
            self.__pos__ = self.__labels__[label]

    def jal(self, any):
        rd, label = any[0], any[1]
        self.reg[rd] = self.__pos__ + 1  # salva PC+1
        self.__pos__ = self.__labels__[label]

    def jalr(self, any):
        rd, rs1, imm = any[0], any[1], int(any[2])
        self.reg[rd] = self.__pos__ + 1
        self.__pos__ = (self.reg[rs1] + imm) & ~1  # alinha para par

    def ret(self, any):
        # Pseudoinstrução: jalr x0, ra, 0
        self.__pos__ = self.reg['ra']

    def ld(self, any):
        rd, offset, rs1 = any[0], int(any[1]), any[2]
        addr = self.reg[rs1] + offset
        self.reg[rd] = self.__mem__.get(addr, 0)  # 64-bit load

    def sd(self, any):
        rs2, offset, rs1 = any[0], int(any[1]), any[2]
        addr = self.reg[rs1] + offset
        self.__mem__[addr] = self.reg[rs2]  # 64-bit store

    # Similar para lw/sw (32-bit), lh/sh (16-bit), lb/sb (8-bit)
    def lw(self, any):
        rd, offset, rs1 = any[0], int(any[1]), any[2]
        addr = self.reg[rs1] + offset
        self.reg[rd] = self.__mem__.get(addr, 0) & 0xFFFFFFFF  # sign-extend?

    # ... adicione os outros loads/stores semelhantes

    def fence(self, any):
        # Barreira de memória (simples: no-op por agora)
        pass

    def ebreak(self, any):
        # Breakpoint: pare ou debug
        self.__x__ = 0
        print("Ebreak: breakpoint atingido")

    def ecall(self, any):
        # Syscall baseada em a7
        syscall_num = self.reg['a7']
        if syscall_num == 64:  # write
            fd = self.reg['a0']
            buf_addr = self.reg['a1'][0]
            count = self.reg['a2']
            # Simule write: pegue de __mem__[buf_addr] por count bytes
            data = ''.join(chr(self.__mem__.get(buf_addr + i, 0)) for i in range(count))
            print(data,end="")  # ou redirecione para stdout simulado
            self.reg['a0'] = count  # retorno = bytes escritos
        elif syscall_num == 63:  # read
            fd = self.reg['a0']
            buf_addr = self.reg['a1'][0]
            count = self.reg['a2']

            if fd == 0:  # stdin simulado
                # Simule input: use input() do Python para pedir ao usuário
                user_input = input()[:count]  # limita ao count
                bytes_read = len(user_input)

                # Escreva na memória a partir de buf_addr
                for i in range(bytes_read):
                    self.__mem__[buf_addr + i] = ord(user_input[i])

                self.reg['a0'] = bytes_read  # retorno = bytes lidos
        
            else:
                self.reg['a0'] = -1  # erro para outros fds
        elif syscall_num == 214:  # brk
            new_brk = self.reg['a0']  # argumento: novo endereço desejado
            if new_brk == 0:
                # brk(0) retorna endereço atual do fim do heap
                self.reg['a0'] = self.heap_end
            else:
                if new_brk > self.heap_end:
                    # Estende heap (simples: só atualiza ponteiro)
                    self.heap_end = new_brk
                    # Opcional: preencher com zeros se quiser
                    # for addr in range(self.heap_end, new_brk): self.__mem__[addr] = 0
                self.reg['a0'] = self.heap_end  # retorna novo fim
        elif syscall_num == 93:  # exit
            self.__x__ = 0
        else:
            print(f"Syscall não implementada: {syscall_num}")
                        
class pyos64:
    __inst_arr_need__=True
    __data_sect_need__=False
    def __init__(self,tread):
        print("thank for :Pygame team! Linux team!\nPyOs it's running a application")
        self.reg=self.__reg__(self)
        self.greg=self.__greg__(self)
        self.sys=self.sys_call(self)
        self.__code__=[]
        self.__stack__=[]
        self.__mem__={}
        self.__ZF__=0
        self.__NF__=0
        self.__CF__=0
        self.__pos__=0
        self._debug_=False
        self.__w_list__=[]
        self.__func__={}
        self.__real__:kernel=tread
        self.__point__={}
        self.__states__={}
        self.__graf__=self.imagem_compose(self)
        self.__recursion__=[]
        self.__env__={}
        self.__ui__=JA.boot(self)
        self.__var__={}
        self.__events__={}
        self.__async_f__=[]
        self.__x__=1
    def __getstate__(self):
        current={
            "reg"           : self.reg        , 
            "greg"          : self.greg       , 
            "sys"           : self.sys        , 
            "__code__"      : self.__code__   , 
            "__stack__"     : self.__stack__  , 
            "__mem__"       : self.__mem__    , 
            "ZF"            : self.__ZF__         , 
            "NF"            : self.__NF__         , 
            "CF"            : self.__CF__         , 
            "__pos__"       : self.__pos__    , 
            "_debug_"       : self._debug_  , 
            "__w_list__"    : self.__w_list__ , 
            "__func__"      : self.__func__   , 
            "__point__"    : self.__point__  , 
            "__states__"    : self.__states__ , 
            # self.__graf__self.imagem_compose(self)
            "__recursion__" : self.__recursion__, 
            "__env__"       : self.__env__    , 
            "__var__"       : self.__var__    , 
            "__events__"    : self.__events__ , 
            "__async_f__"   : self.__async_f__,
        }
        return current
    def __setstate__(self,value):
        for key in value:
            setattr(self,key,value[key])
        self.__ui__=JA.boot(self)
        self.__graf__=self.imagem_compose(self)
    def __repr__(self):
        return f"<pyos64 ISA {version}>\n<with high registers>\n\n::\n\n {self.reg} \n\n::\n\n<with {len(self.__code__)} lines of instruction>"
    class __back__:
        def __init__(self,tread:"pyos64"):
            self.reg=tread.reg
            self.real=tread
    class __greg__:
        def __init__(self,tread:"pyos64"):
            din=dinamica()
            self.graf={
                "x0":0,
                "y0":0,
                "x1":0,
                "y1":0,
                "x2":0,
                "y2":0,
                "x3":0,
                "y3":0,
                "rgb0":0,
                "rgb1":0,
                "rgb2":0,
                "rgb3":0,
                "surf0":surf((10,10)),
                "surf1":surf((100,100)),
                "surf2":surf((3,3)),
                "surf3":surf((1,1)),
                "keyboard":[0],
                "mouse_k":[0,0,0],
                "mouse_pos":[0,0]
            }
            self.real=tread
        def __del__(self):
            JA.pygame.quit()

        def __getstate__(self):
            return self.graf
        def __setstate__(self,values):
            self.graf=values
        def __getitem__(self,__value):
            try:
                # print(f"get {__value} -> {self.values[__value]}")
                return self.graf[__value]
                
            except:
                # print(f"get --> {__value}")
                # print(__value)
                return __value
        def __setitem__(self,__key,__value):
            if __key in self.graf.keys():
                try:
                    # print(f"set {__key} <- {__value}")
                    self.graf[__key]=__value
                except:
                    # print(f"set {__key}<# {__value}")
                    self.real.__mem__[__key]=__value
            else:
                print(f"reg error: {__key}")
                print(f"line {str(self.real.__pos__+1)}")
        def __repr__(self):
            return f"internal registers:\n{self.values}"
        def __str__(self):
            return str(self.values)
    class __reg__:
        def __init__(self,tread:"pyos64"):
            self.values={
                "rax":0,#
                "rgx":0,#
                "a":"0",
                "b":0,
                "c":0,
                "d":0,
                "e":0,#
                "f":0,
                "g":0,
                "h":0,
                "r0":1,
                "r1":10,
                "r2":.1,
                "r3":.0001,
                "r4":None,
                "r5":None,
                "g0":0,
                "g1":0,
                "g2":0,
                "g3":0,
                "rx":"abcdefghijklmnopqrstuvwxyz",
                "ry":r"1234567890*+-=!e~^|&<>",
                "i-sc-size":[800,600],
                "i-flag": pygame.RESIZABLE,
                "i-event":None,
                "i-blank":[0,0,0],
                "ist":0
            }
            self.real=tread

            self.history=[asizeof.asizeof(self)]
        def __getstate__(self):
            return self.values
        def __setstate__(self,values):
            self.values=values
        def __getitem__(self,__value:str):
            try:
                # print(f"get {__value} -> {self.values[__value]}")
                return self.values[__value]
            except:
                # print(f"get --> {__value}")
                # print(__value)
                return __value
        def __setitem__(self,__key,__value):
                try:
                    # print(f"set {__key} <- {__value}")
                    self.values[__key]=__value
                except:
                    print(f"set {__key}<# {__value}")
                # self.history.append(asizeof.asizeof())
        def __repr__(self):
            return f"internal registers:\n{self.values}"
        def __str__(self):
            return str(self.values)
        def copy(self):
            copy=self.real.__reg__(self.real)
            copy.values=self.values.copy()
            return copy
    def mov(self,any):
        self.reg[any[1]]=self.reg[any[0]]
    @property
    def __din_rec__(self):
        return ".".join(self.__recursion__)
    def pss(self,any):
        pass
    def UI(self,any):
        atrr=any[0]

        values=[self.reg[value] for value in any[1:]]
            
        self.__async_f__.append((getattr(self.__ui__,atrr),values,True))
    def load_script(self,any):
        file=self.reg[any[0]]
        self.__script__=JA.scripts(file)
        # print(self.__script__.instru)
        self.__script__.make()
        print(str(self.__script__))
        copy=self.__pos__
        self.__pos__=0
        code=self.__code__.copy()
        self.__code__=self.real.str2code(self.__script__)
        print("the asm is",self.__code__)
        while self.reg["x"]!=0:
            # try:
                op,items=self.__code__[self.__pos__]
                getattr(self,op)(items)
                if op=="halt":
                    print("halted on line",self.__pos__)
                    break
                self.__pos__+=1
            # except Exception as e:
            #     print(self.__pos__)
            #     print("quebro")
            #     break
        self.reg["x"]=1
        self.__pos__=copy
        # print("funcs array",self.func)
        self.__code__=code
    class socket_service:
        def __init__(self,tread:"pyos64",mode):
            self.tread=tread
    def randint(self,any):
        self.reg[any[2]]=randint(self.reg[any[0]],self.reg[any[1]])
    def randbytes(self,any):
        self.reg[any[1]]=randbytes(self.reg[any[0]])
    def eval(self,any):
        # print(any[0].replace("\\n","\n"))
        temp=self.__pos__
        self.__pos__=0
        self.real.run(any[0],False)
        self.__pos__=temp
    def point(self,any):
        self.__point__[any[0]]=self.__pos__
    def loop_p(self,any):
        self.__pos__=self.__point__[any[0]]
    def brick(self,any):
        self.__pos__=self.__stack__.pop()
    def compile_script(self,any):
        with open(any[0],"w")as f:
            f.write(str(self.__script__.codes))
    def set(self,any):
        self.__func__[self.reg[any[1]]]=self.__pos__
        self.__pos__+=any[0]
    def wire(self,any):
        pass #vou implementar coisas aqui
    def watch(self,any):
        self.__w_list__.append(any[0])
    def nwatch(self,any):
        self.__w_list__.remove(any[0])
    def trace(self,any):
        self._debug_ = any[0]
    def AND(self,any):
        self.reg[any[2]]=self.reg[any[0]] & self.reg[any[1]]
    def OR(self,any):
        self.reg[any[2]]=self.reg[any[0]] | self.reg[any[1]]
    def XOR(self,any):
        self.reg[any[2]]=self.reg[any[0]] ^ self.reg[any[1]]
    def NOT(self,any):
        self.reg[any[1]]=~self.reg[any[0]]
    def SHL(self,any):
        self.reg[any[2]]=self.reg[any[0]]<<self.reg[any[1]]
    def SHR(self,any):
        self.reg[any[2]]=self.reg[any[0]]>>self.reg[any[1]]
    def inc(self,any):
        self.reg[any[0]]=self.reg[any[0]]+1
    def xinc(self,any):
        self.reg[any[0]]+=self.reg["r1"]
        self.inc(["r1"])
    def xneg(self,any):
        self.reg[any[0]]-=self.reg["r1"]
        self.inc(["r1"])
    def neg(self,any):
        self.reg[any[0]]-=1
    def movrg(self,any):
        self.greg[any[1]]=self.reg[any[0]]
    def movgr(self,any):
        self.reg[any[1]]=self.greg[any[0]]
        # print("reg x any[0]",self.reg[any[1]],any[0])
    def movr(self,any):
        self.reg[any[1]]=self.reg[any[0]]
    def movx(self,any):
        self.__mem__[any[1]]=self.reg[any[0]]
    def add(self,any):
        self.reg[any[2]]=speed.add(self.reg[any[0]],self.reg[any[1]])
    def sub(self,any):
        self.reg[any[2]]=speed.sub(self.reg[any[0]],self.reg[any[1]])
    def div(self,any):
        self.reg[any[2]]=speed.div(self.reg[any[0]],self.reg[any[1]])
    def mul(self,any):
        self.reg[any[2]]=speed.mul(self.reg[any[0]],self.reg[any[1]])
    def sqr(self,any):
        self.reg[any[2]]=speed.sqr(self.reg[any[0]],self.reg[any[1]])
    def root(self,any):
        self.reg[any[2]]=speed.root(self.reg[any[0]],self.reg[any[1]])
    def call(self, any):
        # push posição atual
        # print("aqui")
        self.__stack__.append(self.__pos__)
        # print(".".join(self.__recursion__+[self.reg[any[0]]]),self.func)
        self.__pos__=self.__func__[any[0]]
    def ret(self, any=None):
        # print("used")
        if any!=[]:
            self.reg["r3"]=self.reg[any[0]]
        self.reg["x"]=0
        # self.__pos__ = self.__stack__.pop()
        # print("            ",self.pos,"depois")
    
    def until(self,any):
        r1,r2,r3=any
        self.reg[r3]=speed.until(self.reg[r1],self.reg[r2])
    def pop(self, any):
        self.reg[any[0]] = self.__stack__.pop()
    def push(self, any):
        self.__stack__.append(self.reg[any[0]])
    def pushm(self,any):
        self.__stack__.append(self.reg[any[0]])
        self.reg[any[0]]=self.reg[any[1]]
    def load(self, any):
        addr,reg = any
        # print(self.__mem__.get(addr,0))
        self.reg[reg] = self.__mem__.get(addr, 0)
    def xload(self,any):
        addr, reg= any
        self.reg[reg]=self.reg[addr,1]
    def store(self, any):
        # print(any)
        addr, reg = any
        self.__mem__[addr] = self.reg[reg]
    def module(self,any):
        with open(any[0],"r")as f:
            temp=f.read()
        xtemp=self.real.make(temp)
        copy=self.__pos__
        self.__pos__=0
        code_copy=self.__code__.copy()
        regs=self.reg.copy()
        self.reg=self.__reg__(self)
        self.__code__=xtemp
        rec=any[0].replace(".asm","")
        self.__recursion__.append(rec)
        while self.reg["x"]:
            op,items=self.real.item_parser(xtemp[self.__pos__])
            # print("self.pos",self.__pos__)
            op(items)
            self.__pos__+=1
        self.__env__[self.__din_rec__]=self.reg.copy()
        self.reg=regs
        self.__code__=code_copy.copy()
        self.reg["x"]=1
        self.__recursion__.pop()
        # self.__code__.pop(self.__pos__)
        # for ncode in xtemp[::-1]:
        #     self.__code__.insert(self.__pos__,ncode)
        self.__pos__=copy
    def list(self,any):
        r=any[0]
        self.reg[r]=[self.reg[value] for value in any[1:]]
        # print(self.reg[r])
    def list_append(self,any):
        r=any[0]
        items=any[1:]
        for item in items:
            self.reg[r].append(self.reg[item])
    def list_appendl(self,any):
        r=any[0]
        self.reg[r].append(any[1:])
    def list_get(self,any):
        r, v, out=any
        self.reg[out]=self.reg[r][v]
    def list_get_bl(self,any):
        r=any[0]
        out=any[-1]
        v=any[1:-1]
        self.reg[out]=[self.reg[value] for value in v]
    
    def list_pop(self,any):
        self.reg[1]=self.reg[any[0]].pop()
    def list_rm(self,any):
        self.reg[any[0]].remove(self.reg[any[0]])
    def dict(self,any):
        self.reg[any[0]]={}
    # @debuga
    def dict_vk(self,any):
        self.reg[any[0]][self.reg[any[1]]]=self.reg[any[2]]
    def dict_kr(self,any):
        self.reg[any[2]]=self.reg[any[0]][self.reg[any[1]]]
    def dict_gk(self,any):
        self.reg[any[1]]=self.reg[any[0]].keys()
    def dict_gv(self,any):
        self.reg[any[1]]=self.reg[any[0]].values()
    def snapshot(self,any):
        self.__states__[any[0]]=self.__getstate__()
    def snapsgb(self,any):
        name,save=any
        self.__states__[name]=self.__getstate__()
        self.__setstate__(self.__states__[save])
    def goback(self,any):
        self.__setstate__(self.__states__[any[0]])
    class imagem_compose:
        def __init__(self,tread:"pyos64"):
            self.real=tread
            pygame.init()
            self.running=1
            def quita(self):
                self.running=0
            self.event_response={pygame.QUIT:quita}
            self.surfs:dict[pygame.Surface]={}
        def __getstate__(self):
            return {}
        @property
        def reg(self):
            return self.real.reg
        def _0(self,any): #update
            pygame.display.update()
        def _1(self,any): #event
            for event in pygame.event.get():
                try:
                    self.event_response.get(event.type,ps)(self)
                except:
                    pass
        def _2(self,any):
            self.window(self.real.reg["i-blank"])
        def _3(self,any):
            self.window.set_at(self.reg[any[0]],self.reg[any[1]])
        def _4(self,any):#get running
            self.real.reg["ist"]=self.running
        def _5(self,any):
            temp=serializador.surf(pygame.display.get_window_size())
            temp.blit(pygame.display.get_surface(),(0,0))
            self.real.reg[any[0]]=temp
        def _6(self,any):
            x,y,name=any
            x,y,name=self.reg[x],self.reg[y],self.reg[name]
            self.surfs[name]=serializador.surf((x,y))
        def _7(self,any): #blit
            name,x,y=[self.reg[v] for v in any]
            self.window.blit(self.surfs[name],(x,y))
        def _8(self,any): #fill
            print([self.reg[value] for value in any])
            self.window.fill([self.reg[value] for value in any])
        def _9(self,any):
            print(self.reg["i-sc-size"])
            self.window=pygame.display.set_mode(self.reg["i-sc-size"],self.reg["i-flag"])
            print("graphic enviroment started")
        def _10(self,any): #surf fill
            r,g,b,name =[self.reg[value] for value in any]
            self.surfs[name].fill((r,g,b))
        def _11(self,any): #surf blit
            source, d_name, d_pos=[self.reg[value] for value in any]
            self.surfs[d_name].blit(source,d_pos)
        def _12(self,any): #input 
            self.real.greg["keyboard"]=pygame.key.get_pressed()
        def _12(self,any): #mouse input
            self.real.greg[""]
    def xcall(self,any):
        getattr(self.__graf__,f"_{self.reg['rgx']}")(any)
    class sys_call:
        def __init__(self,tread:"pyos64"):
            self.real=tread
        def _0(self):
            print(self.real.reg["b"]) 
    def syscall(self,any=None):
        getattr(self.sys,f"_{self.reg['rax']}")()
        [        # try:
        # print(f"_{self.reg['rax']}")
            # print(self.reg["rax"])
            # if self.reg["rax"]==1:
            #     print(self.reg["b"])
            # elif self.reg["rax"]==2:
            #     self.__mem__[self.reg["b"]]=self.reg["c"]
            # elif self.reg["rax"]==3:
            #     self.reg["c"]=self.__mem__.values()
            # elif self.reg["rax"]==10:
            #     pygame.init()
            #     self.window=pygame.display.set_mode((self.reg["b"],self.reg["c"]))
            #     self.blank=(self.reg["d"],self.reg["e"],self.reg["f"])
            # elif self.reg["rax"]==11:
            #     for event in pygame.event.get():
            #         if pygame.QUIT==event.type:
            #             pygame.quit()
            # elif self.reg["rax"]==12:
            #     pygame.display.update()
            # elif self.reg["rax"]==20:
            #     with open(self.reg["b"],"w")as f:
            #         f.write(self.reg["c"])
            # elif self.reg["rax"]==23:
            #     with open(self.reg["b"],"r")as f:
            #         self.reg["c"]=f.read()
            # print(self.mem)
        # except:
        #     print(self.reg)
        #     self.reg["x"]=0
        ]
    
    def CMP(self, any):
        left  = self.reg[any[0]]
        right = self.reg[any[1]]
        value = left - right
        # print(left,right)
        self.__ZF__ = int(value == 0)
        self.__NF__ = int(value < 0)
        self.__CF__ = int(left < right)
    def CMPstr(self,any):
        left  = str(self.reg[any[0]])
        right = str(self.reg[any[1]])
        print(f"right: {left} -- left: {right}",end="\r")
        self.__ZF__ = int(left == right)
        self.__NF__ = int(left in right)
        self.__CF__ = int(right in left)
    def CMPi(self, any):
        left  = self.reg[any[0]]
        right = self.reg[any[1]]

        value = left - right

        ivalue = abs(left)-abs(right)
        self.__i=ivalue
        self.AZF = int(ivalue == 0)
        self.ANF = int(ivalue < 0)
        self.AEF = int(ivalue == value)
        self.AEAF = int(ivalue == abs(value))
    def CMPx(self, any):
        left  = self.reg[any[0]]
        right = self.reg[any[1]]

        value = left - right
        ivalue = abs(left)-abs(right)
        xvalue = ivalue - value

        self.XZF = int(value == 0)
        self.XNF = int(value < 0)
        self.XCF = int(left < right)
    def jz(self, any):      # jump if ZF == 1   (JE / JZ)
        if self.__ZF__: 
            self.__pos__ += any[0]
    def jnz(self, any):     # (JNE / JNZ)
        if not self.__ZF__:
            self.__pos__ += any[0]
    def jn(self, any):      # jump if NF == 1   (JL / JS)
        if self.__NF__:
            self.__pos__ += any[0]
    def jnn(self, any):     # (JNL / JNS)
        if not self.__NF__:
            self.__pos__ += any[0]
    def jc(self, any):      # jump if CF == 1   (JB / JC)
        if self.__CF__:
            self.__pos__ += any[0]
    def jnc(self, any):     # (JNB / JNC)
        if not self.__CF__:
            self.__pos__ += any[0]
    def jaz(self, any):     # jump if abs difference == 0
        if self.AZF:
            self.__pos__ += any[0]
    def jnaz(self, any):   # negativo
        if not self.AZF:
            self.__pos__ += any[0]
    def jan(self, any):     # jump if abs(left) < abs(right)
        if self.ANF:
            self.__pos__ += any[0]
    def jnan(self, any):
        if not self.ANF:
            self.__pos__ += any[0]
    def jae(self, any):     # ivalue == value  (mesmo sinal)
        if self.AEF:
            self.__pos__ += any[0]
    def jnae(self, any):
        if not self.AEF:
            self.__pos__ += any[0]
    def jaea(self, any):    # abs difference == abs(value)
        if self.AEAF:
            self.__pos__ += any[0]
    def jnaea(self, any):
        if not self.AEAF:
            self.__pos__ += any[0]
    def jxz(self, any):     # jump if value == 0 (mesmo que ZF)
        if self.XZF:
            self.__pos__ += any[0]
    def jnxz(self, any):
        if not self.XZF:
            self.__pos__ += any[0]
    def jxn(self, any):     # jump if value < 0  (mesmo que NF)
        if self.XNF:
            self.__pos__ += any[0]
    def jnxn(self, any):
        if not self.XNF:
            self.__pos__ += any[0]
    def jxc(self, any):     # jump if left < right (mesmo que CF)
        if self.XCF:
            self.__pos__ += any[0]
    def jnxc(self, any):
        if not self.XCF:
            self.__pos__ += any[0]
    def jl(self, any):   # signed
        if self.__NF__:
            self.__pos__ += any[0]
    def jg(self, any):
        if (not self.__NF__) and (not self.__ZF__):
            self.__pos__ += any[0]
    def jle(self, any):
        if self.__NF__ or self.__ZF__:
            self.__pos__ += any[0]
    def jge(self, any):
        if not self.__NF__:
            self.__pos__ += any[0]
    def halt(self,any=None):
        self.__x__=0
        if self.__recursion__==[]:
            print("")
    def loop(self,any):
        r,ponteiro=any
        # print(self.reg[r])
        if self.reg[r]!=0:
            self.__pos__=ponteiro
            self.reg[r]-=1
    def xloop(self,any):
        r,pont,fator=any
        if self.reg[0]!=0:
            self.__pos__=pont,
            self.reg[r]-=fator

class solve:
    def __init__(self,ins_pattern:dict,tread:pyos64|risc_v):
        self.iset=ins_pattern
        self.cpu=tread
    def solve(self,params,op):
        solved=[]
        table=self.iset[op]
        for i,param in enumerate(params):
            if isinstance(param,list):
                solved.append(param)
                continue
            try:
                match table[i]:
                    case "in":
                        solved.append(self.cpu.reg[param])
                    case "out":
                        solved.append(param)
                    case "mem":
                        solved.append(self.cpu.__mem__[param])
                    case "label":
                        # print("label getted",self.cpu.__pointers__)
                        solved.append(self.cpu.__point__[param])
            except:
                print(f"'{op}' :: has too many args:: {params}")
        return solved
class pyos64_async:
    def __init__(self,tread):
        self.reg=pyos64.__reg__(self)
        self.__flux__={}
        self.__tread__:kernel=tread
        self.__async_f__=[],
        self.__pos__=0
        self.__cpu__=[]
        self.__code__=[]
        self.__programas__=[]
    def init(self,any):
        x=any[0]
        for i in range(x):
            self.__cpu__.append(pyos64(self.tread))
    def tread(self,any):
        op:str=any[0]
        if op=="start":
            nid:int=any[1]
            size:int=any[2]
            self.__flux__[nid]=self.__code__[self.__pos__+1:self.__pos__+2+size]
            print(self.__flux__[nid])
            self.__pos__+=size
        elif op=="make":
            nid:int=any[1]
            size:int=any[2]
            async def freeze():
                def meta():
                    for op,arg in self.__flux__[nid]:
                        try:
                            getattr(self.__cpu__[nid],op)(arg)
                        except:
                            print("error in tread",nid)
class pyos16: #primeira versão funcional para o kernel antigo
    def __init__(self,tread):
        self.reg={
            "a":0,#
            "b":0,
            "c":0,
            "d":0,
            "e":0,#
            "f":0,
            "g":0,
            "h":0,
            "x":1,#,
            "g0":0,
            "g1":0,
            "g2":0,
            "g3":0,
            "r0":1,
            "r1":10,
            "r2":.1,
            "r3":.0001,
            "rx":"abcdefghijklmnopqrstuvwxyz",
            "ry":r"1234567890*+-=!e~^|&<>"
        }
        self.__code__=[]
        self.__stack__=[]
        self.__mem__={}
        self.ZF=0
        self.NF=0
        self.CF=0
        self.__pos__=0
        self.debug=False
        self.w_list=[]
        self.func={}
        self.real=tread
    def eval(self,any):
        # print(any[0].replace("\\n","\n"))
        temp=self.__pos__
        self.__pos__=0
        self.real.run(any[0].replace("\\n","\n"),False)
        self.__pos__=temp
    def set(self,any):
        # print("set any[0]",any[0])
        self.func[any[1]]=[fcode for fcode in self.__code__[self.__pos__+1:self.__pos__+int(any[0])+1]]
        # print(" 6: ",self.__code__[6:])
        # self.func[any[1]]=self.__pos__
        # print("size",any[0])
        # print("pos",self.__pos__)
        # print(any[1],self.func[any[1]])
        self.__pos__+=any[0]+1
        # print(self.pos)
    def watch(self,any):
        self.w_list.append(any[0])
    def nwatch(self,any):
        self.w_list.remove(any[0])
    def trace(self,any):
        self.debug = any[0]
    def AND(self,any):
        self.reg[any[2]]=self.reg[any[0]] & self.reg[any[1]]
    def OR(self,any):
        self.reg[any[2]]=self.reg[any[0]] | self.reg[any[1]]
    def XOR(self,any):
        self.reg[any[2]]=self.reg[any[0]] ^ self.reg[any[1]]
    def NOT(self,any):
        self.reg[any[1]]=~self.reg[any[0]]
    def SHL(self,any):
        self.reg[any[2]]=self.reg[any[0]]<<self.reg[any[1]]
    def SHR(self,any):
        self.reg[any[2]]=self.reg[any[0]]>>self.reg[any[1]]
    def inc(self,any):
        self.reg[any[0]]+=1
    def xinc(self,any):
        self.reg[any[0]]+=self.reg["r1"]
        self.inc(["r1"])
    def xneg(self,any):
        self.reg[any[0]]-=self.reg["r1"]
        self.inc(["r1"])
    def neg(self,any):
        self.reg[any[0]]-=1
    def mov(self,any):
        self.reg[any[1]]=any[0]
    def movr(self,any):
        self.reg[any[1]]=self.reg[any[0]]
    def movx(self,any):
        self.__mem__[any[1]]=self.reg[any[0]]
    def add(self,any):
        self.reg[any[2]]=self.reg[any[0]]+self.reg[any[1]]
    def sub(self,any):
        self.reg[any[2]]=self.reg[any[0]]-self.reg[any[1]]
    def mul(self,any):
        self.reg[any[2]]=self.reg[any[0]]*self.reg[any[1]]
    def call(self, any):
        # push posição atual
        # print("aqui")
        # self.__stack__.append(self.__pos__)
        copy=self.__pos__
        self.__pos__=0
        code_copy=self.__code__.copy()
        self.__code__=self.func[self.reg[any[0]]]
        while self.reg["x"]!=0:
            try:
                op,items=self.real.item_parser(self.__code__[self.__pos__])
                getattr(self,op)(items)
                if op=="halt":
                    print("erro")
                self.__pos__+=1
            except:
                # print(self.__pos__)
                break
        self.reg["x"]=1
        self.__pos__=copy
        self.__code__=code_copy
        # print("passou")
        # print("usado")
        # pula para função
        # self.__pos__ = self.func[self.reg[any[0]]]
        # print(self.pos)
    def ret(self, any=None):
        # print("used")
        if any!=[]:
            self.reg["r3"]=self.reg[any[0]]
        # self.__pos__ = self.__stack__.pop()
        # print("            ",self.pos,"depois")
    def div(self,any):
        self.reg[any[2]]=any[0]/any[1]
    def pop(self, any):
        self.reg[any[0]] = self.__stack__.pop()
    def push(self, any):
        self.__stack__.append(self.reg[any[0]])
    def load(self, any):
        addr,reg = any
        self.reg[reg] = self.__mem__.get(addr, 0)
    def store(self, any):
        addr, reg = any
        self.__mem__[addr] = self.reg[reg]
    def cmp(self, any):
        left  = self.reg[any[0]]
        right = self.reg[any[1]]

        value = left - right

        self.ZF = int(value == 0)
        self.NF = int(value < 0)
        self.CF = int(left < right)
    def module(self,any):
        with open(any[0],"r")as f:
            temp=f.read()
        xtemp=self.real.make(temp)
        copy=self.__pos__
        self.__pos__=0
        code_copy=self.__code__.copy()
        self.__code__=xtemp
        while self.reg["x"]:
            op,items=self.real.item_parser(xtemp[self.__pos__])
            # print("self.pos",self.__pos__)
            getattr(self,op)(items)
            self.__pos__+=1
        self.__code__=code_copy.copy()
        self.reg["x"]=1
        # self.__code__.pop(self.__pos__)
        # for ncode in xtemp[::-1]:
        #     self.__code__.insert(self.__pos__,ncode)
        self.__pos__=copy
    def syscall(self,any=None):
        # try:
            # print("used")
            # print(self.reg["a"])
            if self.reg["a"]==1:
                print(self.reg["b"])
            elif self.reg["a"]==2:
                self.__mem__[self.reg["b"]]=self.reg["c"]
            elif self.reg["a"]==3:
                self.reg["c"]=self.__mem__.values()
            elif self.reg["a"]==10:
                pygame.init()
                self.window=pygame.display.set_mode((self.reg["b"],self.reg["c"]))
                self.blank=(self.reg["d"],self.reg["e"],self.reg["f"])
            elif self.reg["a"]==11:
                for event in pygame.event.get():
                    if pygame.QUIT==event.type:
                        pygame.quit()
            elif self.reg["a"]==12:
                pygame.display.update()
            elif self.reg["a"]==20:
                with open(self.reg["b"],"w")as f:
                    f.write(self.reg["c"])
            elif self.reg["a"]==23:
                with open(self.reg["b"],"r")as f:
                    self.reg["c"]=f.read()
            # print(self.mem)
        # except:
        #     print(self.reg)
        #     self.reg["x"]=0
    def jmp(self,any):
        # print(any[0])
        self.__pos__+=any[0]
    def halt(self,any=None):
        self.reg["x"]=0
    def loop(self,any):
        if self.reg[r]!=0:
            r,ponteiro=any
            self.__pos__=ponteiro
            self.reg[r]-=1
    def xloop(self,any):
        if self.reg[0]!=0:
            r,pont,fator=any
            self.__pos__=pont,
            self.reg[r]-=fator
# if __name__:
#     print(list(pyos64.__dict__.keys()))
