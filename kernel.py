import shlex, asyncio,traceback as tcb,pickle,gzip
from pympler import asizeof
from lib.JA import parser as jpass
from sereal import generator
# from pickle import dumps , loads
ideia="""mov $1 a
mov "#hello world" b
syscall
mov $10
halt"""

from sys import argv
print(str(argv))
with open("/Users/lucaschaves/projeto_os/log.txt","w")as f:
        f.write(str(argv))

from pyos import pyos16,pyos64
class compilador:
    module_=False
    def __init__(self,nome:str,arch:str="pyos64"):
        self.n=nome.encode()
        self.sig=arch.encode()
        self.save=[]
    # paleta={
    #     b"pyos":{
    #         "mov":pyos.mov,
    #         "syscall":pyos.syscall,
    #         "add":pyos.add,
    #         "sub":pyos.sub,
    #         "mul":pyos.mul,
    #         "div":pyos.div,
    #     }
    # }
    
    paleta={
        b"pyos16":pyos16,
        b"pyos64":pyos64
    }
    optypes={
        "!":b"\x01",    #bytes
        "#":b"\x02",    #str
        "$":b"\x03",    #int
        "@":b"\x04"     #img
    }
    def item_parser(self,code,save=False):
        op=code[0]
        items=[]
            # print(tread.pos)
            # print(actin[tread.pos])
        for i in code[1:]:
            i:str
            if i.startswith("r"):
                ni=i.replace("r","")
                items.append(jpass(ni).pre())# converter S-Expression para lista
            elif i.startswith("$"):
                ni=i.replace("$","")
                print(i)
                try:
                    items.append(int(ni))
                except:
                    items.append(ni)
                # print("used")
            
            elif i.startswith("!"):
                ni=i.replace("!","")
                items.append(bool(ni))
            elif i.startswith("#"):
                ni=i.replace("#","")
                items.append(ni)
            elif i.startswith("@"):
                ni=i.replace("@","")
                items.append(ni)
            else:
                items.append(i)
        if save:
            self.save.append((op,items))
        print(op)
        return getattr(self.cpu,op),items
    def str2code(self,code:str):
        code=str(code)
        paciente=code.splitlines()
        # print(paciente)
        tratado=[]
        for ic in paciente:
            if ic and ic!="":
                if ">" in ic:
                    tratado.append("pss")
                else:
                # print("ic :",ic)
                    tratado . append(ic)
        return [self.item_parser(shlex.split(line)) for line in tratado]
    async def run(self,code:str,save=True,inject:dict=None):
        self.cpu:pyos64=compilador.paleta[self.sig](self)
        paciente=code.splitlines()
        # print(paciente)
        tratado=[]
        for ic in paciente:
            if ic and ic!="":
                if ">" in ic:
                    tratado.append("pss")
                else:
                # print("ic :",ic)
                    tratado . append(ic)
        self.cpu.__code__=[self.item_parser(shlex.split(line),True) for line in tratado]
        if self.module_:
            for key in inject:
                self.cpu.reg[key]=inject[key]
        #         print(key,"injected",inject[key])
        #     print(inject)
        # print("injet",self.module_)
        print(self.cpu.__code__)
        line={}
        while self.cpu.reg["x"]:
                [
            # print(actin)
            # print(actin[1:])
            # items=[]
            # # print(tread.pos)
            # # print(actin[tread.pos])
            # for i in tread.__code__[tread.__pos__][1:]:
            #     if "#" in i:
            #         ni=i.replace("#","")
            #         items.append(ni)
            #     elif "$" in i:
            #         ni=i.replace("$","")
            #         items.append(int(ni))
            #         # print("used")
                
            #     elif "!" in i:
            #         ni=i.replace("!","")
            #         items.append(bool(ni))
            #     else:
            #         items.append(i)
            # if tread.debug:
            #     print(f"** instr: {tread.__code__[tread.__pos__][0]},line {tread.__pos__} **")
            #     print(f"{len(items)} param:")
            #     for pra in items:
            #         print(f"- {pra} {type(pra).__name__.upper()}")
            # if len(items)>=1:
            #     if items[-1] in tread.w_list:
            #         print(f"## watch point triggered @ addr {items[-1]} ##")
            #         print(f"OLD : {tread.reg[items[-1]]}")
            # print(tread.__code__[tread.__pos__])
                ]
                op,items=self.cpu.__code__[self.cpu.__pos__]
                op(items)
                temp=[]
                for i in self.cpu.__async_f__:
                    # print(i)
                    temp.append(asyncio.create_task(i[0](*i[1])))
                    if i[2]:
                        await temp[-1]
                # for i in temp:
                #     try:
                #         await i
                #     except KeyboardInterrupt:
                #         print("keyboard pressed")
                #     except Exception:
                #         print(f"###Error###\nSegmentation Fault!\nLine {str(self.cpu.__pos__+1)}\nOP: {op} > Args/Items {items}")
                #         tcb.print_exc()
                #         if self.cpu.__pos__ in line.keys():
                #             exit()    
                #         line[self.cpu.__pos__]=True
                try:
                    self.cpu.__async_f__=[]
                    # if len(items)>=1:
                    #     if items[-1] in tread.w_list:
                    #         print(f"NEW : {tread.reg[items[-1]]}")
                    # print(tread.pos)
                    self.cpu.__pos__+=1
                except:
                    continue
        
        if save:
            # print(tread.func)
            return self.cpu.__code__,self.cpu.__func__
    def Break(self):
        self
    def make(self,code):
        # Ccode=[]
        # tread=compilador.paleta[self.sig](self)
        paciente=code.splitlines()
        # print(paciente)
        tratado=[]
        for ic in paciente:
            if not ">" in ic and ic!="":
                # print("ic :",ic)
                tratado . append(ic)
        actin=[shlex.split(line) for line in tratado]
        return actin
    def write(self,file):# não funcional, ainda estou pensando como fazer
        xop=set()
        pargs=[]
        fcode=[]
        for op,agrs in self.save:
            xop.add(op)
            pargs.append(agrs)
        gen=generator([list(xop),pargs])
        gen.dump(file)
    def start(self,bin,funcs):
        tread=compilador.paleta[self.sig](self)
        self.funcs=funcs
        while tread.reg["x"]:
            # print(actin)
            # print(actin[1:])
            items=[]
            for i in bin[tread.__pos__][1:]:
                if type(i)==int:
                    items.append(i)
                elif type(i)==bytes:
                    if b"$" in i:
                        ni=i.replace(b"$",b"")
                        items.append(int(ni))
                    elif b"#" in i:
                        ni=i.replace(b"#",b"")
                        items.append(ni.decode())
                    else:
                        items.append(i.decode)
                elif type(i)==str:
                    if "$" in i:
                        ni=i.replace("$","")
                        items.append(int(ni))
                    elif "#" in i:
                        ni=i.replace("#","")
                        items.append(ni)
                    else:
                        items.append(i)
            getattr(tread,bin[tread.__pos__][0])(items)
            tread.__pos__+=1
        self.reg=tread.reg
    def __getstate__(self):
        self.cpu.reg["x"]=True
        values={
            "cpu":self.cpu,
            "name":self.n,
            "sig":self.sig
        }
        return values
    def __setstate__(self,values):
        self.cpu=values["cpu"]
        self.cpu.__real__=self
        self.n=values["name"]
        self.sig=values["sig"]
if __name__ == "__main__":
    teste= compilador("codigo")
    if ".bin" in argv[1]:
        with open(argv[1],"rb")as f:
            app=teste.read(f.read())
            teste.start(*app)
    elif "r" in argv:
        with open(argv[1],"r")as f:
            asyncio.run(teste.run(f.read()))
        # import matplotlib.pyplot  as mtp
        # mtp.plot(range(len(teste.cpu.reg.history)),teste.cpu.reg.history)
        # mtp.show()
    elif "r-" in argv:
        compilador.module_=True
        layout={
    "main":{
        "type":"Box",
        "value":"",
        "style":{
            "size":[200,140],
            "position":[20,50]
        },
        "child":{
            "texto":{
                "type":"TextBox",
                "value":"programa iniciado",
                "style":{
                    "color":[255,255,255],
                    "background":[255,255,255,255],
                },
                'events':{
                    'hover_leave':{
                        "script": (("change_style" ,"background", [100, 100, 100, 255]),
                                   ("change_style" ,"color", [0, 0, 0, 255])),
                        "JIT": True
                    },
                    'hover_enter':{
                        "script": (("change_style" ,"background", [255, 255, 255, 255]),
                                   ("change_style" ,"color", [0, 0, 0, 255])),
                        "JIT": True
                    }
                }
            }
        }
    }
}
        with open(argv[1],"r")as f:
            asyncio.run(teste.run(f.read(),inject={"corpo":layout}))
        teste.write("temp.pickle")
    elif "rmake" in argv:
        try:
            with open(argv[1],"r")as f:
                teste.asyncio.run(teste.run(f.read()))
        except:
            print("failed to open: ",argv[1])
    else:
        print("kernel usage: <file.asm> ['r' run projects|'rmake' run projects from user_space]")
else:
    print("module mode")
    compilador.module_=True
#depois ....
# binario=teste.write(*projeto)
# print(binario)

# app=teste.read(binario)
# with open("programa base.pyapp","wb")as f:
    # f.write(binario)
# app=teste.read(binario)
# teste.start(app)
# # print(binario)
# app=teste.read(binario)

# print("kernel em bytes:",asizeof.asizeof(teste,code=True))
# print("itens da paleta",teste.paleta[b"pyos64"].__dict__)
# print("pyos64 em mb:",asizeof.asizeof(teste.reg))