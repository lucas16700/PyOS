# from kernel import compilador
from random import randbytes,randint
# from json import dumps, loads
from lib import JA
from functools import lru_cache
# from lib.wprotoc import server,client
from time import time
from pickle import dumps as upld,loads as dowld
import pygame
from numba import jit,njit
import serializador,asyncio
from pympler import asizeof
from gfx.surfs import surf
import asyncio
import numpy as np
from sereal import __mems__
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
debussy=True
debussy=False
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
        'lb':     ['out', 'in', "in"],     # mem = offset(rs1)
        'lbu':    ['out', 'in', 'in'],
        'lh':     ['out', 'in', 'in'],
        'lhu':     ['out', 'in', 'in'],
        'lw':     ['out', 'in', 'in'],
        'ld':     ['out', 'in', 'in'],

        # R-type (rd, rs1, rs2)
        'add':    ['out', 'in', 'in'],
        'sub':    ['out', 'in', 'in'],
        'mul':    ['out', 'in', 'in'],
        'div':    ['out', 'in', 'in'],
        'and':    ['out', 'in', 'in'],
        'or':     ['out', 'in', 'in'],
        'xor':    ['out', 'in', 'in'],
        'andi':    ['out', 'in', 'in'],
        'andiw':    ['out', 'in', 'in'],
        'sll':    ['out', 'in', 'in'],
        'srl':    ['out', 'in', 'in'],
        'sra':    ['out', 'in', 'in'],
        'slt':    ['out', 'in', 'in'],
        'divu': ['out', 'in', 'in'],
        'remu': ['out', 'in', 'in'],

        # S-type (rs2, imm(rs1)) — note: sem out!
        'sb':     ['in', 'in', "in"],      # rs2 é fonte (in), mem é destino
        'sh':     ['in', 'in', 'in'],
        'sw':     ['in', 'in', 'in'],
        'sd':     ['in', 'in', 'in'],

        # Branches (rs1, rs2, in/offset)
        'beq':    ['in', 'in', 'in'],
        'beqz':    ['in', 'in'],
        'bne':    ['in', 'in', 'in'],
        'bnez':    ['in', 'in'],
        'blt':    ['in', 'in', 'in'],
        'bltz':    ['in', 'in'],
        'bge':    ['in', 'in', 'in'],
        'bgt':    ['in', 'in', 'in'],

        # Jumps
        'jal':    ['out', 'in'],   # rd, in
        'j':    ['in'],   #  in
        'jr':    ['in'],   #  in
        'jalr':   ['out', 'mem', 'mem'],     # rd, offset(rs1)

        # U-type
        'lui':    ['out', 'in'],      # rd, imm
        'auipc':  ['out', 'in'],

        # Pseudos
        'li':     ['out', 'in'],
        'la':     ['out', 'in'],
        'mv':     ['out', 'in'],
        'ret':    [],                 # sem args
        'nop':    [],

        # Syscall
        "ecall":  []
    }
    __data_sect_need__=True
    __inst_arr_need__=True
    import lexer_risc as lx_00
    def __init__(self,tread):
        self.tread=tread
        self.reg=self.__reg__(self)
        self.reg[2] = 128 * 1024
        self.__code__=[]
        self.__stack__=[]
        self.memory_size = 128 * 1024  # 128 KiB — confortável para começar
        self.__mem__ = __mems__(self.memory_size)  # ou bytearray(self.memory_size)

        self.heap_start = 0x4000     # endereço virtual inicial do heap (exemplo)
        self.heap_end   = self.heap_start + 4096  # começa com 1 página alocada

        # Opcional: área separada para mmap (se quiser diferenciar do heap)
        self.mmap_regions = {}  # futuro: dict de {addr: {'len': X, 'prot': Y}}
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
        # self.__ui__=JA.boot(self)
        self.__clock__=0
        self.__var__={}
        self.__events__={}
        self.__async_f__=[]
        self.__x__=1
        self.__labels__={}
        self.opened_files={}
        self.globl=0
        self.__sections__={
            "globl":"_start",
            "currenct":"",
            "section":".text",
        }
        self.opened_files[0] = open(0, 'rb', buffering=0)   # stdin
        self.opened_files[1] = open(1, 'wb', buffering=0)   # stdout
        self.opened_files[2] = open(2, 'wb', buffering=0)   # stderr
    class __reg__:
        def __init__(self,tread:"risc_v"):
            self.values={
                a:0 for a in range(32)
            }
            self.real=tread
            self.stack=2
            self.history=[asizeof.asizeof(self)]
        def __getstate__(self):
            return self.values
        def __setstate__(self,values):
            self.values=values
        def __getitem__(self,__value:str):
            # print(__value,"getted")
            return self.values[__value]
        def __setitem__(self,__key,__value):
            if not __key in self.values.keys():
                raise 
            self.values[__key]=__value
                
                    
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
        # print("li args",any)
        rd, imm = any[0], int(any[1])
        self.reg[rd] = imm
    def mv(self,any):
        self.reg[any[0]]=any[1]
    def la(self, any):
        rd, label = any[0], any[1]
        # print(f"la : rd.{rd} =label.{label}")
        # Assume label resolvido para endereço (ex.: de .data)
        self.reg[rd] = label  # ou endereço virtual
        # print(f"rd in memory {self.reg[rd]}")
    def lb(self, any):
        """
        lb rd, offset(rs1)
        any = [rd, offset, rs1]   # ex.: ['t0', 0, 'a1']
        """
        # print(f"in lb {any}")
        rd = any[0]          # registrador destino
        offset = any[1] # pode ser string ou int, converta
        rs1 = any[2]       # registrador base
        # print(f"rs1 lido {rs1}")
        # Calcula endereço
        addr = rs1 + offset

        # Lê 1 byte da memória
        byte_val = int(self.__mem__.get(addr, 0))  # garante 0-255

        # # Extensão de sinal (signed byte → int64)
        # if byte_val & 0x80:  # bit de sinal ligado (128-255)
        #     byte_val -= 256   # transforma em -128 a -1
        # print(f"lb : leu {byte_val} de {addr}:{rs1}+{offset}")
        self.reg[rd] = byte_val
    def lbu(self, any):
        """
        lbu rd, offset(rs1)
        any = ['rd', endereço_final]   # ou ['rd', offset, 'rs1'] se ainda não resolveu
        """
        rd = any[0]
        
        # Se o parser ainda não resolveu o endereço, ajuste aqui:
        if len(any) == 3:  # formato cru: ['rd', offset, 'rs1']
            offset = int(any[1])
            rs1 = any[2]
            addr = rs1 + offset
        else:  # já resolvido (recomendado)
            addr = int(any[1])

        # Lê 1 byte e garante 0–255 (unsigned)
        byte_val = self.__mem__.get(addr, 0) & 0xFF
        
        self.reg[rd] = byte_val
        # print(f"lbu: leu {byte_val} (0x{byte_val:x}) de 0x{addr:x} para {rd}")
    def lh(self, any):
        """
        lh rd, offset(rs1)
        any = ['rd', endereço_final]
        """
        rd = any[0]
        
        if len(any) == 3:
            offset = int(any[1])
            rs1 = any[2]
            addr = rs1 + offset
        else:
            addr = int(any[1])

        # Lê 2 bytes (little-endian)
        byte1 = self.__mem__.get(addr, 0) & 0xFF
        byte2 = self.__mem__.get(addr + 1, 0) & 0xFF
        half_val = int((byte2 << 8) | byte1)

        # Extensão de sinal (16-bit → 64-bit signed)
        if half_val & 0x8000:        # bit 15 ligado?
            half_val -= 0x10000      # transforma em número negativo

        self.reg[rd] = half_val
        # print(f"lh: leu {half_val} (0x{half_val:x}) de 0x{addr:x} para {rd}")
    def lhu(self, any):
        """
        lhu rd, offset(rs1)
        any = ['rd', endereço_final]
        """
        rd = any[0]
        
        if len(any) == 3:
            offset = int(any[1])
            rs1 = any[2]
            addr = rs1 + offset
        else:
            addr = int(any[1])

        # Lê 2 bytes (little-endian)
        byte1 = self.__mem__.get(addr, 0) & 0xFF
        byte2 = self.__mem__.get(addr + 1, 0) & 0xFF
        half_val = (byte2 << 8) | byte1

        # Sem extensão de sinal → valor fica entre 0 e 65535
        self.reg[rd] = half_val
        # print(f"lhu: leu {half_val} (0x{half_val:x}) de 0x{addr:x} para {rd}")
    def andi(self,any):
        rd, rs1, rs2=any
        self.reg[rd]= rs1 & rs2

    def andiw(self,any):
        rd, rs1, rs2=any
        self.reg[rd]= (rs1 & rs2) & 0xFFFFFFFF

    def sb(self, any):
        """
        sb rs2, offset(rs1)
        any = [rs2, offset, rs1]   # ex.: ['t0', 0, 'a1']
        """
        # print(any)
        rs2 = any[0]          # registrador que contém o byte a escrever
        offset = int(any[1])
        rs1 = any[2]          # registrador base
        # print("rs1 dentro dee sb")
        # Calcula endereço
        base_addr = rs1
        addr = base_addr + offset

        # Pega só o byte menos significativo (0–255)
        byte_val = rs2 & 0xFF

        # Escreve na memória
        # print(f"sb : escreveu {byte_val} em {addr}")
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
    def addiw(self,any):
        rd, rs1, imm = any[0], int(any[1]), int(any[2])
        self.reg[rd] = (rs1 + imm) & 0xFFFFFFFF
    def addi(self, any):
        # print(f"addi {any}")
        rd, rs1, imm = any[0], int(any[1]), int(any[2])
        self.reg[rd] = (rs1 + imm)# & 0xFFFFFFFF
    def sext_w(self, any):
        rd, rs1 = any[0], int(any[1])
        # print(f"rd: {rd} = rs1: {rs1}+rs2: {rs2}")
        valor32 = rs1 & 0xFFFFFFFF
        if valor32 & 0x80000000:         # se o bit 31 está ligado (número negativo em 32 bits)
            self.reg[rd] = valor32 | 0xFFFFFFFF00000000
        else:
            self.reg[rd] = valor32
    def add(self, any):
        rd, rs1, rs2 = any[0], int(any[1]), int(any[2])
        # print(f"rd: {rd} = rs1: {rs1}+rs2: {rs2}")
        self.reg[rd] = rs1 + rs2
    def addw(self, any):
        rd, rs1, rs2 = any[0], int(any[1]), int(any[2])
        soma32 = (rs1 + rs2) & 0xFFFFFFFF          # soma só os 32 bits baixos
        if soma32 & 0x80000000:                    # se o resultado em 32 bits é negativo
            self.reg[rd] = soma32 | 0xFFFFFFFF00000000
        else:
            self.reg[rd] = soma32
    def mul(self, any):
        rd, rs1, rs2 = any[0], any[1], any[2]
        self.reg[rd] = int(rs1 * rs2)
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
        self.reg[rd] = rs1 - rs2

    # def mul(self, any):
    #     rd, rs1, rs2 = any[0], any[1], any[2]
    #     self.reg[rd] = rs1 * rs2  # Assumindo M extension

    def div(self, any):
        rd, rs1, rs2 = any[0], any[1], any[2]
        if rs2 == 0:
            # Trap ou erro (implemente exception)
            print("Divisão por zero!")
            return
        self.reg[rd] = rs1 // rs2  # signed div
    def divu(self, any):
        """
        divu rd, rs1, rs2
        any = [('reg_out', 't0'), ('reg_in', 'a0'), ('reg_in', 'a1')]
        """
        # print("divu chamado com:", any)

        # Extrai os argumentos já classificados
        rd,rs1,rs2 = any     # deve ser 'reg_out'
        
        # Pega valores reais
        dividend = rs1 & 0xFFFFFFFFFFFFFFFF  # unsigned 64-bit
        divisor = rs2 & 0xFFFFFFFFFFFFFFFF   # unsigned 64-bit
        # print("rd",rd)
        if divisor == 0:
            # Comportamento comum em emuladores: retorna -1 ou máximo unsigned
            self.reg[rd] = 0xFFFFFFFFFFFFFFFF  # -1 em signed, máximo em unsigned
            # print("divu: divisão por zero! Retornando máximo unsigned")
        else:
            self.reg[rd] = dividend // divisor  # divisão inteira unsigned
        # print("fina")
        # print(f"divu: {dividend} / {divisor} = {self.reg[rd]}")
    def remu(self, any):
        """
        remu rd, rs1, rs2
        any = [('reg_out', 't0'), ('reg_in', 'a0'), ('reg_in', 'a1')]
        """
        # print("remu chamado com:", any)

        rd,rs1,rs2 = any

        
        dividend = rs1 & 0xFFFFFFFFFFFFFFFF
        divisor = rs2 & 0xFFFFFFFFFFFFFFFF

        if divisor == 0:
            self.reg[rd] = dividend  # ou 0xFFFFFFFFFFFFFFFF, escolha um padrão
            # print("remu: divisão por zero! Retornando dividendo")
        else:
            self.reg[rd] = dividend % divisor

        # print(f"remu: {dividend} % {divisor} = {self.reg[rd]}")
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
        if rs1 == rs2:
            self.__pos__ = label

    def j(self,any):
        label = any[0]
        self.__pos__=label

    def jr(self,any):
        label = any[0]
        self.__pos__=label

    def beqz(self, any):
        rs1, label = any[0], any[1]
        if rs1 == 0:
            self.__pos__ = label

    def bne(self, any):
        rs1, rs2, label = any[0], any[1], any[2]
        if rs1 != rs2:
            self.__pos__ = label

    def bnez(self, any):
        rs1, label = any[0], any[1]
        if rs1 != 0:
            self.__pos__ = label

    def blt(self, any):
        rs1, rs2, label = any[0], any[1], any[2]
        if rs1 < rs2:  # signed
            self.__pos__ = label

    def bltz(self, any):
        rs1, label = any[0], any[1]
        if rs1 < 0:  # signed
            self.__pos__ = label

    def bge(self, any):
        rs1, rs2, label = any[0], any[1], any[2]
        if rs1 >= rs2:
            self.__pos__ = label
    def bgt(self, any):
        rs1, rs2, label = any[0], any[1], any[2]
        if rs1 > rs2:
            self.__pos__ = label

    def bltu(self, any):
        rs1, rs2, label = any[0], any[1], any[2]
        if abs(rs1) < abs(rs2):  # unsigned
            self.__pos__ = label

    def bgeu(self, any):
        rs1, rs2, label = any[0], any[1], any[2]
        if abs(rs1) >= abs(rs2):
            self.__pos__ = label

    def jal(self, any):
        rd, label = any[0], any[1]
        self.reg[rd] = self.__pos__  # salva PC+1
        self.__pos__ = label

    def jalr(self, any):
        rd, rs1, imm = any[0], any[1], int(any[2])
        self.reg[rd] = self.__pos__
        self.__pos__ = (rs1 + imm) & ~1  # alinha para par

    def ret(self, any):
        # Pseudoinstrução: jalr x0, ra, 0
        self.__pos__ = self.reg[1]

    def ld(self, any):
        rd, offset, rs1 = any[0], int(any[1]), any[2]
        addr = rs1 + offset
        self.reg[rd] = self.__mem__.get(addr, 0)  # 64-bit load

    def sd(self, any):
        rs2, offset, rs1 = any[0], int(any[1]), any[2]
        addr = rs1 + offset
        # print(f"rs1 {rs1} + offset {offset}")
        self.__mem__[addr] = rs2 & 0xFFFFFFFFFFFFFFFF  # 64-bit store

    # Similar para lw/sw (32-bit), lh/sh (16-bit), lb/sb (8-bit)
    def lw(self, any):
        rd, offset, rs1 = any[0], int(any[1]), any[2]
        addr = rs1 + offset
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
        syscall_num = self.reg[11]
        if syscall_num == 64:  # write
            fd = self.reg[10]
            buf_addr = self.reg[11]
            count = self.reg[12]
            # Simule write: pegue de __mem__[buf_addr] por count bytes
            
            bit=[self.__mem__.get(buf_addr + i, 0)for i in range(count)]
            # print(bytes(bit))
            self.opened_files[fd].write(bytes(bit))

            # data = ''.join(chr() )
            # print("printado")
            self.reg[10] = count  # retorno = bytes escritos
        elif syscall_num == 63:  # read
            fd = self.reg[10]
            buf_addr = self.reg[11]
            count = self.reg[12]

            if fd in self.opened_files:  # stdin simulado
                # Simule input: use input() do Python para pedir ao usuário
                user_input = self.opened_files[fd].read(count)  # limita ao count
                bytes_read = len(user_input)

                # Escreva na memória a partir de buf_addr
                for i in range(bytes_read):
                    self.__mem__[buf_addr + i] = user_input[i]

                self.reg[10] = bytes_read  # retorno = bytes lidos
            # elif fd in self.opened_files:
            #     for i, byte in enumerate(data):
            #         byte= self.__mem__[buf + i]
            else:
                self.reg[10] = -1  # erro para outros fds
        elif syscall_num == 214:  # brk
            
            new_brk = self.reg[10]  # argumento: novo endereço desejado
            if new_brk == 0:
                # brk(0) retorna endereço atual do fim do heap
                self.reg[10] = self.heap_end
                # print("heap geted ",self.heap_end)
            else:
                if new_brk > self.heap_end:
                    # print("novo heap",new_brk)
                    for i in range(new_brk-self.heap_end):
                        # print(i)
                        self.__mem__[len(self.__mem__)]=0
                    # Estende heap (simples: só atualiza ponteiro)
                    # self.heap_end = new_brk
                    # Opcional: preencher com zeros se quiser
                    # for addr in range(self.heap_end, new_brk): self.__mem__[addr] = 0
                self.reg[10] = self.heap_end  # retorna novo fim
        elif syscall_num == 215:  # munmap
            addr   = self.reg[10]
            length = self.reg[11]

            if length <= 0 or addr % 4096 != 0:
                self.reg[10] = -22  # EINVAL
                return

            end = addr + length
            if addr < self.heap_start or end > self.heap_end:
                self.reg[10] = -12  # ENOMEM
                return

            # Simples: só "desaloca" (remove do heap_end ou marca como inválido)
            if end == self.heap_end:
                self.heap_end = addr  # encolhe heap
            else:
                # Para regiões no meio: marca como não mapeado (futuro: dict de regiões)
                print(f"munmap parcial: 0x{addr:x}–0x{end:x} (não encolhe heap_end)")

            self.reg[10] = 0  # sucesso
            print(f"munmap: liberado 0x{addr:x}–0x{end:x}")
        elif syscall_num == 221:  # mmap
            addr_hint = self.reg[10]     # endereço sugerido (geralmente 0)
            length    = self.reg[11]     # tamanho em bytes
            prot      = self.reg[12]     # PROT_READ=1, PROT_WRITE=2, PROT_EXEC=4
            flags     = self.reg[13]     # MAP_SHARED=1, MAP_PRIVATE=2, MAP_ANONYMOUS=32
            fd        = self.reg[14]     # file descriptor (-1 para anônimo)
            offset    = self.reg[15]     # offset no arquivo

            # Simples: ignora addr_hint e fd por enquanto (MAP_ANONYMOUS)
            if flags & 32:  # MAP_ANONYMOUS
                # Aloca memória nova (anônima)
                if length <= 0:
                    self.reg[10] = -1  # erro
                    return
                
                alloc_addr = self.heap_end
                # Opcional: zere a área
                for i in range(length):
                    self.__mem__[alloc_addr + i] = 0
                
                # Usa próximo endereço livre (ex.: após heap_end)
                self.heap_end += length  # estende heap (ou use área separada)

                

                self.reg[10] = alloc_addr  # retorna endereço alocado
                print(f"mmap: alocados {length} bytes anônimos em 0x{alloc_addr:x}")
            else:
                # mmap com arquivo — mais complexo, ignore por agora
                self.reg[10] = -1
                print("mmap com arquivo não implementado")
        elif syscall_num == 226:  # mprotect
            addr   = self.reg[10]   # endereço inicial
            length = self.reg[11]   # tamanho
            prot   = self.reg[12]   # novas permissões

            if length <= 0 or addr % 4096 != 0:
                self.reg[10] = -22  # EINVAL (argumento inválido)
                print("mapeamento invalido")
                return

            # Simples: só verifica se a região está dentro do mapeado
            end = addr + length
            if addr < self.heap_start or end > self.heap_end:
                self.reg[10] = -12  # ENOMEM (fora do mapeado)
                print("fora do mapeamento")
                return

            # Aqui você pode ter um dict de permissões por página
            # Exemplo simples: só registra o prot (futuro page fault simulado)
            print(f"mprotect: 0x{addr:x}–0x{end:x} → prot {prot} (READ={prot&1}, WRITE={prot&2}, EXEC={prot&4})")
            self.reg[10] = 0  # sucesso
        elif syscall_num == 93:  # exit
            self.__x__ = 0
        else:
            print(f"Syscall não implementada: {syscall_num}")
class solve:
    def __init__(self,ins_pattern:dict,tread:risc_v):
        self.iset=ins_pattern
        self.cpu=tread
    def solve(self,params:list,op:str):
        if debussy: # variavel definida dentro do escopo como swith de debug ,para outras partes do codigo tambem
            print("solving", f"{op} {params}",end="\n\n")
        
        solved=[]
        table=self.iset[op]
        ix=0
        sub=params.copy()
        for index,ih in enumerate(params):
            if isinstance(ih,list):
                while "%hi" in ih:
                    if isinstance(ih[1],int):
                        val=int(self.cpu.reg[ih[1]])
                    elif isinstance(ih[1],str):
                        val=int(self.cpu.__data__[ih[1]])
                        # try:
                        #     val=int(self.cpu.reg[params[idx+1]])
                        # except:
                        #     val=int(self.cpu.__data__[params[idx+1]])
                    sub[index]=val >> 12
                    # params.pop(idx+1)
                    # print(f"hi {params[idx]}")
                while "%lo" in ih:
                    idx=params.index("%lo")
                    try:
                        val=int(params[idx+1])
                    except:
                        if isinstance(ih[1],int):
                            val=int(self.cpu.reg[ih[1]])
                        elif isinstance(ih[1],str):
                            val=int(self.cpu.__data__[ih[1]])
                    sub[index]=val & 0xFFF
                    # params.pop(idx+1)
                    # print(f"lo {params[idx]}")
        params=sub
        for i,param in enumerate(params):
            # if isinstance(param,list):
            #     for ix,subp in enumerate(param):
            #         # try:
            #             match table[i+ix]:
            #                 case "in":
            #                     try:
            #                         int(subp)
            #                         solved.append(int(subp))
            #                         # print(subp,int(subp))
            #                         # print("solving with numbers")
            #                         continue
            #                     except:
            #                         solved.append(self.cpu.reg[subp])
            #                 case "out":
            #                     solved.append(subp)
            #                 case "mem":
            #                     if ix:
            #                         solved.append(self.cpu.reg[subp])
            #                     else:
            #                         solved.append(subp)
            #                 case "label":
            #                     # print("label getted",self.cpu.__pointers__)
            #                     solved.append(self.cpu.__point__[subp])
            #         # except:
            #         #     print(f"'{op}' :: has too many args:: {params}")
            #     # print("continuado")
            #     continue
            
            match table[i+ix]:
                    case "in":
                        if isinstance(param,int):
                            solved.append(self.cpu.reg[param])
                        elif isinstance(param,str):
                            solved.append(self.cpu.__labels__[param])
                    case "out":
                        solved.append(param)
                    case "mem":
                        solved.append(self.cpu.__mem__[param])
                    # case "label":
                    #     # print("label getted",param)
                    #     if isinstance(param,str):
                    #         solved.append(self.cpu.__labels__[param])
                    #     elif isinstance(param,int):
                    #         solved.append(self.cpu.__labels__[self.cpu.reg[param]])
                    
            # except:
            #     print(f"'{op}' :: has too many args:: {params}")
        # if op=="lb":
        #     print(f"lb with {solved} :: {params}")
        return solved                      
class pyos64:
    INSTRUCTION_PATTERNS = {
        #basicas
        "mov": ["out","in","in"],
        "pss": [],
        
        #geradores

        "randint": ["out", "in", "in"],
        "randbytes": ["out", "in", "in"],
        
        #prepara saltos

        "point": ["in"],
        "pycall": ["in" for a in range(16)],
        #sys
        "halt":[]
    }
    __inst_arr_need__=True
    __data_sect_need__=True
    def __init__(self,tread):
        print("thank for :Pygame team! Linux team!\nPyOs it's running a application")
        self.reg=self.__reg__(self)
        self.__code__=[]
        self.__mem__= __mems__(2048)
        self.__pos__=0
        self.__func__={}
        self.__real__:kernel=tread
        self.__labels__={}
        self.__states__={}
        self.__high__={}
        # self.__ui__=JA.boot(self)
        self.__events__={}
        self.__async_f__=[]
        self.__x__=1
        self.opened_files={}

        self.opened_files[0] = open(0, 'rb', buffering=0)   # stdin
        self.opened_files[1] = open(1, 'wb', buffering=0)   # stdout
        self.opened_files[2] = open(2, 'wb', buffering=0)   # stderr
    
    def __repr__(self):
        return f"pyos64 ISA {version}"
    def __str__(self):
        return f"<pyos64 ISA {version}>\n<with high registers>\n\n::\n\n {self.reg} \n\n::\n\n<with {len(self.__code__)} lines of instruction>"

    class __reg__:
        def __init__(self,tread:"pyos64"):
            self.values={x:0 for x in range(64)}
            self.real=tread
        def __getstate__(self):
            return self.values
        def __setstate__(self,values):
            self.values=values
        def __getstate__(self):
            return self.values
        def __setstate__(self,values):
            self.values=values
        def __getitem__(self,__value:str):
            # print(__value,"getted")
            return self.values[__value]
        def __setitem__(self,__key,__value):
            self.values[__key]=np.uint64(__value & 0xFFFFFFFFFFFFFFFF)
        def __repr__(self):
            return f"internal registers:\n{self.values}"
        def __str__(self):
            return str(self.values)
        def copy(self):
            copy=self.real.__reg__(self.real)
            copy.values=self.values.copy()
            return copy
    def mov(self,any):
        self.reg[any[0]]=any[1]
        # print(any,"movido foi isso")
    def movh(self,any):
        rd,rs1, rs2 =any
        self.__high__[rs1]=rs2
    def pss(self,any):
        pass
    # def load_script(self,any):
    #     file=self.reg[any[0]]
    #     self.__script__=JA.scripts(file)
    #     # print(self.__script__.instru)
    #     self.__script__.make()
    #     print(str(self.__script__))
    #     copy=self.__pos__
    #     self.__pos__=0
    #     code=self.__code__.copy()
    #     self.__code__=self.real.str2code(self.__script__)
    #     print("the asm is",self.__code__)
    #     while self.reg["x"]!=0:
    #         # try:
    #             op,items=self.__code__[self.__pos__]
    #             getattr(self,op)(items)
    #             if op=="halt":
    #                 print("halted on line",self.__pos__)
    #                 break
    #             self.__pos__+=1
    #         # except Exception as e:
    #         #     print(self.__pos__)
    #         #     print("quebro")
    #         #     break
    #     self.reg["x"]=1
    #     self.__pos__=copy
    #     # print("funcs array",self.func)
    #     self.__code__=code
    def randint(self,any):
        rd,rs1,rs2 = any
        self.reg[rd]=randint(rs1,rs2)
    def randbytes(self,any):
        rd,rs1 = any
        self.reg[rd]=randbytes(rs1)
    # def eval(self,any):
    #     # print(any[0].replace("\\n","\n"))
    #     temp=self.__pos__
    #     self.__pos__=0
    #     self.real.run(any[0],False)
    #     self.__pos__=temp
    def pycall(self,any):
        value,*params=any
        if int(value)==1:
            file=params[0]
            start=params[1]
            size=params[2]
            bit=[self.__mem__.get(start + i, 0)for i in range(size)]
            self.opened_files[file].write(bytes(bit))
        else:
            print("num chamo certo",any)

    def point(self,any):
        label = any[0]
        self.__labels__[label]=self.__pos__
    def loop_p(self,any):
        label=any[0]
        self.__pos__=label
    def set(self,any):
        rd,rs1 = any
        self.__labels__[rd]=self.__pos__
        self.__pos__+=rs1
    def wire(self,any):
        pass #vou implementar coisas aqui
    def AND(self,any):
        rd,rs1,rs2= any
        self.reg[rd]=rs1 & rs2
    def OR(self,any):
        rd,rs1,rs2= any
        self.reg[rd]=rs1 | rs2
    def XOR(self,any):
        rd,rs1,rs2= any
        self.reg[rd]=rs1 ^ rs2
    def NOT(self,any):
        rd,rs1= any
        self.reg[rd]=~rs1
    def SHL(self,any):
        rd,rs1,rs2= any
        self.reg[rd]=rs1<<rs2
    def SHR(self,any):
        rd,rs1,rs2= any
        self.reg[rd]=rs1>>rs2
    def inc(self,any):
        rd,rs1= any
        self.reg[rd]=rs1+1
    def xinc(self,any):
        rd1,rd2,rs = any
        self.reg[rd1]+=rs
        self.reg[rd2]+=1
    def xneg(self,any):
        rd1,rd2,rs = any
        self.reg[rd1]-=rs
        self.reg[rd2]+=1
    def neg(self,any):
        rd,rs1= any
        self.reg[rd]=rs1-1
        # print("reg x any[0]",self.reg[any[1]],any[0])
    def add(self,any):
        rd,rs1,rs2= any
        self.reg[rd]=speed.add(rs1,rs2)
    def sub(self,any):
        rd,rs1,rs2= any
        self.reg[rd]=speed.sub(rs1,rs2)
    def div(self,any):
        rd,rs1,rs2= any
        self.reg[rd]=speed.div(rs1,rs2)
    def mul(self,any):
        rd,rs1,rs2= any
        self.reg[rd]=speed.mul(rs1,rs2)
    def sqr(self,any):
        rd,rs1,rs2= any
        self.reg[rd]=speed.sqr(rs1,rs2)
    def root(self,any):
        rd,rs1,rs2= any
        self.reg[rd]=speed.root(rs1,rs2)
    def call(self, any):
        # push posição atual
        # print("aqui")
        label=any
        self.reg[62]+=1
        self.reg[63-self.reg[62]]=self.__pos__
        self.__pos__=label
    def ret(self, any=None):
        # print("used")
        self.__pos__=self.reg[63-self.reg[62]]
        self.reg[62]-=1
        # self.__pos__ = self.__stack__.pop()
        # print("            ",self.pos,"depois")
    
    def until(self,any):
        r1,r2,r3=any
        self.reg[r3]=speed.until(self.reg[r1],self.reg[r2])
    def load(self, any):
        addr,reg = any
        # print(self.__mem__.get(addr,0))
        self.reg[reg] = self.__mem__[addr]
    def xload(self,any):
        addr, reg= any
        self.reg[reg]=~self.__mem__[addr]
    def store(self, any):
        # print(any)
        addr, reg = any
        self.__mem__[addr] = reg
    
    def jc(self,any):
        cond,label = any
        if cond:
            self.__pos__=label
    def jcdl(self,any):
        cond, label1, label2 =any
        if cond:
            self.__pos__=label1
        else:
            self.__pos__=label2
    def cgo(self,any):
        rd, cond, label = any
        self.reg[rd] = self.__pos__
        if cond:
            self.__pos__=label
    def go(self,any):
        rd, label= any
        self.reg[rd]=self.__pos__
        self.__pos__ = label

    def halt(self,any=None):
        self.__x__=0
    def loop(self,any):
        r,ponteiro=any
        # print(self.reg[r])
        if self.reg[r]!=0:
            self.__pos__=ponteiro
            self.reg[r]-=1
class solve_py:
    def __init__(self,ins_pattern:dict,tread:pyos64):
        self.iset=ins_pattern
        self.cpu=tread
    def solve(self,params:list,op:str):
        if debussy: # variavel definida dentro do escopo como swith de debug ,para outras partes do codigo tambem
            print("solving", f"{op} {params}",end="\n\n")
        
        solved=[]
        table=self.iset[op]
        ix=0
        # for index,ih in enumerate(params):
        #     if isinstance(ih,list):
        #         while "%hi" in ih:
        #             if isinstance(ih[1],int):
        #                 val=int(self.cpu.reg[ih[1]])
        #             elif isinstance(ih[1],str):
        #                 val=int(self.cpu.__data__[ih[1]])
        #                 # try:
        #                 #     val=int(self.cpu.reg[params[idx+1]])
        #                 # except:
        #                 #     val=int(self.cpu.__data__[params[idx+1]])
        #             sub[index]=val >> 12
        #             # params.pop(idx+1)
        #             # print(f"hi {params[idx]}")
        #         while "%lo" in ih:
        #             idx=params.index("%lo")
        #             try:
        #                 val=int(params[idx+1])
        #             except:
        #                 if isinstance(ih[1],int):
        #                     val=int(self.cpu.reg[ih[1]])
        #                 elif isinstance(ih[1],str):
        #                     val=int(self.cpu.__data__[ih[1]])
        #             sub[index]=val & 0xFFF
        #             # params.pop(idx+1)
        #             # print(f"lo {params[idx]}")
        for i,param in enumerate(params):
            # if isinstance(param,list):
            #     for ix,subp in enumerate(param):
            #         # try:
            #             match table[i+ix]:
            #                 case "in":
            #                     try:
            #                         int(subp)
            #                         solved.append(int(subp))
            #                         # print(subp,int(subp))
            #                         # print("solving with numbers")
            #                         continue
            #                     except:
            #                         solved.append(self.cpu.reg[subp])
            #                 case "out":
            #                     solved.append(subp)
            #                 case "mem":
            #                     if ix:
            #                         solved.append(self.cpu.reg[subp])
            #                     else:
            #                         solved.append(subp)
            #                 case "label":
            #                     # print("label getted",self.cpu.__pointers__)
            #                     solved.append(self.cpu.__point__[subp])
            #         # except:
            #         #     print(f"'{op}' :: has too many args:: {params}")
            #     # print("continuado")
            #     continue
            # print(param)
            match table[i+ix]:
                    
                    case "in":
                        if isinstance(param,list):
                            # print("in : ",param[0]==1,param)
                            if param[0]:
                                # print(f"register {param[1]}")
                                solved.append(self.cpu.reg[param[1]])
                            else:
                                solved.append(param[1])
                        elif isinstance(param,str):
                            # print("label chamado", self.cpu.__labels__,param)
                            solved.append(self.cpu.__labels__[param])
                    case "out":
                        if isinstance(param,list):
                            # print("in : ",param[0]==1,param)
                            solved.append(param[1])
                        else:
                            solved.append(param)
                    case "mem":
                        solved.append(self.cpu.__mem__[param])
                    # case "label":
                    #     # print("label getted",param)
                    #     if isinstance(param,str):
                    #         solved.append(self.cpu.__labels__[param])
                    #     elif isinstance(param,int):
                    #         solved.append(self.cpu.__labels__[self.cpu.reg[param]])
                    
            # except:
            #     print(f"'{op}' :: has too many args:: {params}")
        # if op=="lb":
        #     print(f"lb with {solved} :: {params}")
        return solved
risc_v.__solver__=solve
pyos64.__solver__=solve_py
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
