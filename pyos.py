# from kernel import compilador
from rich import print
from random import randbytes,randint
# from json import dumps, loads
from lib import JA
from time import time
from pickle import dumps as upld,loads as dowld
import pygame
from numba import jit,njit
import serializador
if __name__ =="mojang":
    from kernel import compilador as kernel
print("pyos booted")
def ps(*arg,**karg):
    pass
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
class pyos64:
    def __init__(self,tread):
        print("thank for :Pygame team! Linux team!\nPyOs it's running a application")
        self.reg=self.__reg__(self)
        self.greg=self.__greg__(self)
        self.sys=self.sys_call(self)
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
        self.real:kernel=tread
        self.__point__={}
        self.__states__={}
        self.__graf__=self.imagem_compose(self)
        self.__recursion__=[]
        self.__env__={}
        self.__ui__=JA.boot(self)
        self.__var__={}
        self.__events__={}
    def __getstate__(self):
        current={
            "reg":self.reg,
            "mem":self.__mem__,
            "states":self.__states__,
            "var":self.__var__,
            "recursion":self.__recursion__,
            "graf":self.__graf__,
            "ui":self.__ui__,
            "events":self.__events__,
            "code":self.__code__,
            "stack":self.__stack__,
            "ZNCF":[self.ZF,self.NF,self.CF],
            "pos":self.__pos__,
            "funcs":self.func,
            "point":self.__point__,
            "valid":time()
        }
        return current
    def __setstate__(self,value):
        valid=value["valid"]
        if time()+10>valid:
            self.reg                  =value["reg"]   
            self.__code__             =value["code"]  
            self.__stack__            =value["stack"] 
            self.ZF,self.NF,self.CF   =value["ZNCF"]  
            self.__pos__              =value["pos"]   
            self.func                 =value["funcs"] 
            self.__point__            =value["point"]   
        else:
            self.reg                  =value["reg"]   
            self.__code__             =value["code"]  
            self.__stack__            =value["stack"] 
            self.ZF,self.NF,self.CF   =value["ZNCF"]  
            self.__pos__              =value["pos"]   
            self.func                 =value["funcs"] 
            self.__point__            =value["point"]   
            print("ta velho")
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
                "surf0":pygame.Surface((10,10)),
                "surf1":pygame.Surface((100,100)),
                "surf2":pygame.Surface((3,3)),
                "surf3":pygame.Surface((1,1)),
                "keyboard":[0],
                "mouse_k":[0,0,0],
                "mouse_pos":[0,0]
            }
            self.real=tread
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
            din=dinamica()
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
                "x":1,#
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
        def __repr__(self):
            return f"internal registers:\n{self.values}"
        def __str__(self):
            return str(self.values)
        def copy(self):
            copy=self.real.__reg__(self.real)
            copy.values=self.values.copy()
            return copy
    @property
    def __din_rec__(self):
        return ".".join(self.__recursion__)
    def pss(self,any):
        pass
    def UI(self,any):
        atrr=any[0]
        values=[self.reg[value] for value in any[1:]]
        getattr(self.__ui__,atrr)(*values)
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
        self.func[".".join(self.__recursion__+[any[1]])]=[fcode for fcode in self.__code__[self.__pos__+1:self.__pos__+int(any[0])+1]]
        self.__var__[".".join(self.__recursion__+[any[1]])]=[any[2:]]
        print("func defined, name",any[1],"var",any[2:])
        self.__pos__+=any[0]
    def UI_event(self,any):
        print("ui event seted",any)
        if any[0]=="set":
            self.__events__[any[2]]=any[1]
            self.__ui__.load_script(self.__events__)
    def widget(self,any):
        pass
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
        self.reg[any[0]]=self.reg[any[0]]+1
    def xinc(self,any):
        self.reg[any[0]]+=self.reg["r1"]
        self.inc(["r1"])
    def xneg(self,any):
        self.reg[any[0]]-=self.reg["r1"]
        self.inc(["r1"])
    def neg(self,any):
        self.reg[any[0]]-=1
    def mov(self,any):
        self.reg[any[1]]=self.reg[any[0]]
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
        # self.__stack__.append(self.__pos__)
        # print(".".join(self.__recursion__+[self.reg[any[0]]]),self.func)
        copy=self.__pos__
        self.__pos__=0
        code_copy=self.__code__.copy()
        regs=self.reg.copy()

        self.__recursion__.append(self.reg[any[0]])
        self.__code__=self.func[self.reg[any[0]]]
        while self.reg["x"]!=0:
            try:
                op,items=self.real.item_parser(self.__code__[self.__pos__])
                getattr(self,op)(items)
                if op=="halt":
                    print("erro")
                self.__pos__+=1
            except Exception as e:
                # print(self.__pos__)
                print("quebro")
                break
        self.__recursion__.pop()
        self.reg=regs
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
            getattr(self,op)(items)
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
        def _1(self):
            with open(self.real.reg["b"],"r")as f:
                self.real.reg["c"]=f.read()
        def _2(self):
            temp=[]
            with open(self.real.reg["b"],"r")as f:
                while True:
                    try:
                        temp.append(f.read(self.real.reg["d"]))
                    except:
                        break
            self.real.reg["c"]="".join(temp)
        def _3(self):
            with open(self.real.reg["a"],"w")as f:
                f.write(self.real["b"])
        def _4(self):
            with open(self.real.reg["a"],"wb")as f:
                f.write(self.real["b"])
        def _5(self):
            with open(self.real.reg["a"],"rb")as f:
                self.real["b"]=f.read()
        def _6(self):
            ftext=str(self.real.reg["b"])
            print(self.real.__mem__)
            ftext=ftext.format(*[item[1] for item in self.real.__mem__.items()])
            self.real.reg["c"]=ftext
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
        # print(f"right: {left}\nleft: {right}")
        value = left - right
        # print(left,right)
        self.ZF = int(value == 0)
        self.NF = int(value < 0)
        self.CF = int(left < right)
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
        if self.ZF: 
            self.__pos__ += any[0]
    def jnz(self, any):     # (JNE / JNZ)
        if not self.ZF:
            self.__pos__ += any[0]
    def jn(self, any):      # jump if NF == 1   (JL / JS)
        if self.NF:
            self.__pos__ += any[0]
    def jnn(self, any):     # (JNL / JNS)
        if not self.NF:
            self.__pos__ += any[0]
    def jc(self, any):      # jump if CF == 1   (JB / JC)
        if self.CF:
            self.__pos__ += any[0]
    def jnc(self, any):     # (JNB / JNC)
        if not self.CF:
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
        if self.NF:
            self.__pos__ += any[0]
    def jg(self, any):
        if (not self.NF) and (not self.ZF):
            self.__pos__ += any[0]
    def jle(self, any):
        if self.NF or self.ZF:
            self.__pos__ += any[0]
    def jge(self, any):
        if not self.NF:
            self.__pos__ += any[0]
    def halt(self,any=None):
        self.reg["x"]=0
        if self.__recursion__==[]:
            print(str(self.reg),str(self.func))
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

class pyos16: #primeira versão
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

# print(pyos64.__dict__.keys())