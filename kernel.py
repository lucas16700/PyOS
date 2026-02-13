import shlex, asyncio,traceback as tcb,pickle,gzip
from pympler import asizeof
from lib.JA import parser as jpass
from sereal import generator
import builtins
from rich import print as rich_print
builtins.print = rich_print
builtins.builtins=builtins
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

from pyos import pyos16,pyos64,risc_v,solve as sv
class compilador:
    module_=False
    def __init__(self,nome:str,arch:str="pyos64"):
        builtins.tread=self
        self.n=nome.encode()
        self.sig=arch.encode()
        self.save=[]
        self.cpu:pyos64|risc_v=self.paleta[arch](self)
        self.nvram=None
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
        "pyos16":pyos16,
        "pyos64":pyos64,
        "riscv":risc_v
    }
    optypes={
        "!":b"\x01",    #bytes
        "#":b"\x02",    #str
        "$":b"\x03",    #int
        "@":b"\x04"     #img
    }
    def item_parser(self,code,save=False):
        op:str=code[0]
        items=[]
        if op.startswith(";")or op==";":
            return getattr(self.cpu,"nop"),[]
            # print(tread.pos)
            # print(actin[tread.pos])
        #feito para ISA do pyos64 que ja esta funcional 
        for i in code[1:]:
            i:str
            if i.startswith(";")or i==";":
                break
            if i.endswith(","):
                i=i.removesuffix(",")
            
            if i.startswith(","):
                i=i.removeprefix(",")
            elif "(" in i and i.endswith(")"):
                print(i)
                bruto=jpass(i).pre()
                offset=bruto[0]
                rs1 = bruto[1][0]
                items.append([offset,rs1])

            elif i.startswith("r"):
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
        if op.startswith("."):
            items=[op]+items
            return getattr(self.cpu,"sect_0_"),items
        elif op.endswith(":"):
            items=[op]+items
            return getattr(self.cpu,"label_0_"),items
        print(op)
        if op.startswith(";") or op==";":
            return getattr(self.cpu,"NONES_label_space"),[]
        return getattr(self.cpu,op),items
    def str2code(self,code:str):
        code=str(code)
        paciente=code.splitlines()
        # print(paciente)
        tratado=[]
        for ic in paciente:
            if ic.startswith(";"):
                tratado.append("pss")
            ic= ic.split(";")[0]
            if ic and ic!="":
                if ">" in ic:
                    tratado.append("pss")
                else:
                # print("ic :",ic)
                    tratado . append(ic)
        return [self.item_parser(shlex.split(line)) for line in tratado]
    def sections_serial(self,secs:list):
        print("partitioning",[x[0] for x in secs].count(self.cpu.NONES_label_space))
        index=0
        nsect=[]
        mode=".text"
        code=[]
        labels={}
        vars={}
        temp=None
        size=0
        offset=0
        for line in secs:
            if line[0]!= self.cpu.NONES_label_space:
                nsect.append(line)
        data_pos=0
        final=[]
        for i,liner in enumerate(nsect):
            op,args=liner
            print("mode : ",mode)
            if op==self.cpu.label_0_:
                if mode==".text":
                    labels[args[0].removesuffix(":")]=i
                elif mode in (".data", ".rodata", ".bss"):
                    print(f"mode {mode}, with args {args}")
                    vars[args[0].removesuffix(":")]=[data_pos,0]
                    if len(args)==1:

                        temp=args[0].removesuffix(":")
                        size=0
                        offset=data_pos
                    elif len(args)>1:
                        if args[1] == ".word":
                            for val_str in args[2:]:
                                val = int(val_str)
                                for i in range(4):
                                    self.cpu.__mem__[data_pos + i] = (val >> (i*8)) & 0xFF
                                data_pos += 4
                        elif args[1] == ".dword":
                            val = int(args[2])
                            for i in range(8):
                                self.cpu.__mem__[data_pos + i] = (val >> (i*8)) & 0xFF
                            data_pos += 8
                        elif args[1] == ".string":
                            texto = args[2].strip('"').replace('\\n', '\n')
                            for char in texto:
                                self.cpu.__mem__[data_pos] = ord(char)
                                data_pos += 1
                            self.cpu.__mem__[data_pos] = 0  # null terminator
                            data_pos += 1
                        elif args[1] == ".byte":
                            for val_str in args[2:]:
                                self.cpu.__mem__[data_pos] = int(val_str) & 0xFF
                                data_pos += 1
                        elif args[1] == ".space":
                            size = int(args[2])
                            data_pos += size  # só avança (ou preenche com 0 se quiser)
                        # .align N
                        elif args[1] == ".align":
                            align = 1 << int(args[2])
                            data_pos = (data_pos + align - 1) & ~(align - 1)
                        vars[args[0].removesuffix(":")][1]=data_pos-vars[args[0].removesuffix(":")][0]
            elif op==self.cpu.sect_0_:
                if args[0]==".section":
                    mode=args[1]
                    print(args)
                elif mode==".text":
                    print(args)
                    if args[0]==".globl":
                        self.cpu.__sections__["globl"]=args[1]
                    else:
                        mode=args[0]
                    print("fmode ",mode)
                elif mode in (".data", ".rodata", ".bss"):
                    if args[0] == ".word":
                        for val_str in args[1:]:
                            val = int(val_str)
                            for i in range(4):
                                self.cpu.__mem__[data_pos + i] = (val >> (i*8)) & 0xFF
                            data_pos += 4
                    elif args[0] == ".dword":
                        val = int(args[1])
                        for i in range(8):
                            self.cpu.__mem__[data_pos + i] = (val >> (i*8)) & 0xFF
                        data_pos += 8
                    elif args[0] == ".string":
                        print(args[1:])
                        texto = args[1].strip('"').replace('\\n', '\n')
                        for char in texto:
                            self.cpu.__mem__[data_pos] = ord(char)
                            data_pos += 1
                        self.cpu.__mem__[data_pos] = 0  # null terminator
                        data_pos += 1
                    elif args[0] == ".byte":
                        for val_str in args[1:]:
                            self.cpu.__mem__[data_pos] = (int(val_str) & 0xFF).to_bytes(1)
                            data_pos += 1
                    elif args[0] == ".space":
                        size = int(args[1])
                        data_pos += size  # só avança (ou preenche com 0 se quiser)
                    # .align N
                    elif args[0] == ".align":
                        align = 1 << int(args[1])
                        data_pos = (data_pos + align - 1) & ~(align - 1)
                    if temp:
                        vars[temp][1]=data_pos-vars[temp][1]
            if mode==".text":
                final.append([op,args])
        # nsect=[]
        # for line in final:
        #     if line[0]!= self.cpu.NONES_label_space:
        #         nsect.append(line)
        print("final result############")
        print(self.cpu.__mem__,vars,nsect)
        print("end of final code#######")
        return final,labels,vars # retorna secs , porque ainda não sei o que retornar , estou na duvida entre remover data completamente , ja que essa sessão vai ficar no em self.__data__ que é escrita junto com o binario, e na leitura , tudo o que estiver em data, vai ser definido
    async def run(self,code:str|list,save=True,inject:dict=None,parser=False):
        # self.cpu:pyos64=compilador.paleta[self.sig](self)
        # print(paciente)
        tratado=[]
        if isinstance(code,str):
            paciente=code.splitlines()
            for ic in paciente:
                if ic and ic!="":
                    if ">" in ic:
                        tratado.append("pss")
                    else:
                    # print("ic :",ic)
                        tratado . append(ic)
            self.cpu.__code__=[self.item_parser(shlex.split(line),True) for line in tratado]
            
        else:
            self.cpu.__code__=code
        #         print(key,"injected",inject[key])
        #     print(inject)
        # print("injet",self.module_)
        if self.module_ and inject:
            self.nvram=inject.copy( )
            for key in inject:
                    self.cpu.reg[key]=inject[key]
        if self.cpu.__data_sect_need__:
            self.cpu.__code__,self.cpu.__labels__,self.cpu.__point__=self.sections_serial(self.cpu.__code__)
        # print(self.cpu.__code__)
        if parser:
            return
        print("sected need",self.cpu.__data_sect_need__)
        if self.cpu.__inst_arr_need__:
            self.sv=sv(self.cpu.INSTRUCTION_PATTERNS,self.cpu)
        else:
            self.sv=None
        while self.cpu.__x__:
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
                if not self.sv:
                    op(items)
                else:
                    op(self.sv.solve(items,op.__name__))
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
        # print("printing op name")
        for op,agrs in self.cpu.__code__:
            xop.add(op.__name__)
            # print(op.__name__)
            pargs.append(agrs)
            # print(":arg ",agrs)
        fxop=list(xop)
        # print(fxop)
        for op,ac in self.cpu.__code__:
            fcode.append(fxop.index(op.__name__))
        code_part=[pargs,fxop,fcode,self.nvram,self.cpu.__mem__,self.sig.decode(),self.cpu.__point__,self.cpu.__labels__]
        gen=generator(code_part)
        # print(code_part)
        with gzip.open(file,"wb")as f:
            f.write(gen.dump(True))
    def read(self,file):
        gen=generator(None)
        pargs,fxop,fcode,nvram,self.cpu.__mem__,self.sig,self.cpu.__point__,self.cpu.__labels__=gen.revert(file)
        self.cpu=self.paleta[self.sig](self)
        self.sig=self.sig.encode()
        code=[]
        print(nvram)
        for i,index in enumerate(fcode):
            code.append(
                [getattr(self.cpu,fxop[index]),pargs[i]]
            )
        return [code,nvram]
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
    # def __del__(self):
    #     try:
    #         print(self.cpu)
    #     except:
    #         print("cpu killed")
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
            asyncio.run(teste.run(f.read(),inject={"corpo":layout},parser=True))
        teste.write(argv[-1])
    elif "riscv" in argv:
        teste=compilador("programa","riscv")
        with open(argv[1],"r")as f:
            asyncio.run(teste.run(f.read(),parser=False))
        teste.write(argv[-1])
            # print(teste.save)
    elif "serial" in argv:
        teste.module_=True
        code,nv=teste.read(argv[1])
        asyncio.run(teste.run(code,inject=nv))
    elif "rvserial" in argv:
        teste.module_=True
        code,nv=teste.read(argv[1])
        asyncio.run(teste.run(code,inject=nv))
    else:
        print("kernel usage: <file.asm> ['r' run projects|'r-' run projects and write to temp.serial]")
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