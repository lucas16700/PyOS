import shlex, asyncio,traceback as tcb,pickle,gzip
from pympler import asizeof
from lib.JA import parser as jpass,pygame
from sereal import generator
from parser import riscv as risco_, pyos64 as pyos_
import builtins
# from plot_debug import imprime
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
pygame.quit()
class compilador:
    module_=False
    def __init__(self,nome:str,arch:str="pyos64"):
        builtins.tread=self
        self.n=nome.encode()
        self.sig=arch.encode()
        self.save=[]
        self.cpu:pyos64|risc_v=self.paleta[arch](self)
        self.nvram=None
        self.history=[]
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
        try:
            op:str=code[0]
        except:
            print(code,"sem nada")
            return "nop",[]
        items=[]
        if op.startswith(";")or op==";":
            return "nop",[]
        if op.startswith("#")or op=="#":
            return "nop",[]
            # print(tread.pos)
            # print(actin[tread.pos])
        #feito para ISA do pyos64 que ja esta funcional
        xcode=[]
        temp=""
        print(code[1:])
        for i in code[1:]:
            
            if i.startswith("#")or i=="#":
                break
            if i.startswith(";")or i==";":
                break
            if not temp==".string" or op!=".string":
                # print(temp,"is not .string",i)
                if "," in i and not (", " in i or " ," in i):
                    [xcode.append(x) for x in i.split(",") if len(x)>0]

                elif i.endswith(",") or i.startswith(","):
                    xcode.append(i.replace(",",""))
                
                else:
                    xcode.append(i)
            else:
                print("e .strings",f"string: {code[1:]}")
                xcode.append(i)
            temp=i
        print("xcode from",xcode)
        temp=""
        for i in xcode:
            i:str
            # print("parametro ",i, "sendo parseado")
            if i == "zero":
                items.append(0)
            elif "(" in i and ")" in i and op!=".string":
                
                bruto=jpass(i).pre()
                print(bruto,"brtuo  ",temp)
                for itemx in bruto:
                    if isinstance(itemx,list):
                        for itemy in itemx:
                            items.append(itemy)
                    else:
                        items.append(itemx)
            

            # elif i.startswith("r"):
            #     ni=i.replace("r","")
            #     items.append(jpass(ni).pre())# converter S-Expression para lista
            else:
                items.append(i)
            temp=i
        if save:
            self.save.append((op,items))
        if op.endswith(":"):
            items=[op]+items
            return "label_0_",items
        elif op.startswith("."):
            items=[op]+items
            return "sect_0_",items
        print(op)
        return op,items
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
                tratado . append(ic)
        return [self.item_parser(shlex.split(line)) for line in tratado]
    def sections_serial(self,secs:list):
        print("partitioning",[x[0] for x in secs].count(self.cpu.NONES_label_space))
        index=0
        nsect=[]
        mode=".data"
        code=[]
        labels={}
        temp=None
        size=0
        offset=0
        for line in secs:
            if line[0]!= self.cpu.NONES_label_space:
                nsect.append(line)
        data_pos=0
        final=[]
        page=4096
        mod={
            ".data":0,
            ".rodata":page,
            ".bss":page*2
            }
        types={

        }
        rcha={
            "@object":".data",
            "@function":".text"
        }
        globl=None
        lens={}
        last_globl=""
        for i,liner in enumerate(nsect):
            op,args=liner
            
            print("mode : ",mode,op,args)
            if op=="label_0_":
                mode=types.get(args[0].removesuffix(":"),mode)
                if mode==".text":
                    nname=args[0].removesuffix(":")
                    final.append(["label_0_",[nname]])
                    labels[nname]=len(final)-1
                elif mode in (".data", ".rodata", ".bss",".sdata", ".srodata", ".sbss"):
                    print(f"mode {mode}, with args {args}")
                    labels[args[0].removesuffix(":")]=data_pos
                    if len(args)>1:
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
                                val_str:str
                                if val_str.startswith("0x"):
                                    self.cpu.__mem__[data_pos] = int(val_str,16) & 0xFF
                                else:
                                    self.cpu.__mem__[data_pos] = int(val_str) & 0xFF
                                data_pos += 1
                        elif args[1] == ".space":
                            size = int(args[2])
                            data_pos += size  # só avança (ou preenche com 0 se quiser)
                        # .align N
                        elif args[1] == ".align":
                            align = 1 << int(args[2])
                            data_pos = (data_pos + align - 1) & ~(align - 1)
                        elif args[1] == ".type":
                            print("types seted",args[2:])
                            types[args[2]]=rcha[args[3]]
                        else:
                            print("nothing happened")
                        # vars[args[0].removesuffix(":")][1]=data_pos-vars[args[0].removesuffix(":")][0]
            elif op=="sect_0_":
                
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
                elif mode in (".data", ".rodata", ".bss",".sdata", ".srodata", ".sbss"):
                    if args[0] == ".word":
                        for val_str in args[1:]:
                            val = int(val_str)
                            for i in range(4):
                                self.cpu.__mem__[data_pos + i] = (val >> (i*8)) & 0xFF
                            data_pos += 4
                    elif args[0] == ".dword":
                        try:
                            val = int(args[1])
                        except:
                            # print(labels)
                            val = eval(args[1],labels)
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
                            if val_str.startswith("0x"):
                                self.cpu.__mem__[data_pos] = (int(val_str,16) & 0xFF)
                            else:
                                self.cpu.__mem__[data_pos] = (int(val_str) & 0xFF)
                            data_pos += 1
                    elif args[0] == ".space":
                        size = int(args[1])
                        data_pos += size  # só avança (ou preenche com 0 se quiser)
                    # .align N
                    elif args[0] == ".globl":
                        last_globl=args[1]
                    elif args[0] == ".align":
                        align = 1 << int(args[1])
                        data_pos = (data_pos + align - 1) & ~(align - 1)
                    elif args[0] == ".type":
                        print("types seted*")
                        types[args[1]]=rcha[args[2]]
                    else:
                        print("nothing happened")
                    # if temp:
                    #     vars[temp][1]=data_pos-vars[temp][1]
            elif mode==".text":
                print(f".text code: {[op,args]}")
                final.append([op,args])
            elif mode in (".data",".rodata",".bss"):
                if "=" in args:
                    args:list
                    evo = " ".join(args[1:])
                    evo=evo.replace(".",str(data_pos))
                    labels[op]=eval(evo,labels)
                    
        if last_globl!="":
            self.cpu.__pos__=labels[last_globl]
            self.cpu.globl=self.cpu.__pos__
        # nsect=[]
        # for line in final:
        #     if line[0]!= self.cpu.NONES_label_space:
        #         nsect.append(line)
        try:
            labels.pop('__builtins__')
        except:
            pass
        print(types)
        print("final result############")
        print(labels,list(enumerate(final)))
        print("end of final code#######")
        return final,labels # retorna secs , porque ainda não sei o que retornar , estou na duvida entre remover data completamente , ja que essa sessão vai ficar no em self.__data__ que é escrita junto com o binario, e na leitura , tudo o que estiver em data, vai ser definido
    async def run(self,code:str|list,save=True,inject:dict=None,parser=False,reading=False):
        # self.cpu:pyos64=compilador.paleta[self.sig](self)
        # print(paciente)
        if not reading:
            print("nao estou lendo")
            tratado=[]
            if isinstance(code,str):
                paciente=code.splitlines()
                for ic in paciente:
                    if ic and ic!="":
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
                self.cpu.__code__,self.cpu.__labels__=self.sections_serial(self.cpu.__code__)
            # print(self.cpu.__code__)
            
            
            # print(self.cpu.__code__)
            self.cpu.__code__=[[getattr(self.cpu,op),arg] for op,arg in self.cpu.__code__]
            if parser:
                return
        else:
            self.cpu.__code__=code
        # print("sected need",self.cpu.__data_sect_need__)
        if self.cpu.__inst_arr_need__:
            self.sv=self.cpu.__solver__(self.cpu.INSTRUCTION_PATTERNS,self.cpu)
        else:
            self.sv=None
        self.history_len=0
        if not self.cpu.__pos__:
            self.cpu.__pos__=0
        # print(self.cpu.__code__)
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
            try:
                # print("linha:",self.cpu.__code__[self.cpu.__pos__])
                # print("linha rodada: ",self.cpu.__pos__)
                op,items=self.cpu.__code__[self.cpu.__pos__]

                # self.history.append([op.__name__,items])
                if not self.sv:
                    op(items)
                else:
                    op(self.sv.solve(items,op.__name__))
                # self.history_len+=1
                # self.history.append([vv for vv in self.cpu.reg.values.values()])
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
            except KeyboardInterrupt:
                print("killed")
                # imprime(iter(self.history))
                with open("logmem.txt","w")as f:
                    f.write(bytes(self.cpu.__mem__.r).hex())
                break
            except:
                print("error ocurred")
                print(self.cpu.__pos__)
                raise
        memoria=bytes(self.cpu.__mem__.r)
        print(f"final memory ({len(self.cpu.__mem__)} Bytes): {memoria[:512]} :: {memoria[-32:]}\nlabels:{self.cpu.__labels__}")
                # print(f"final memory ({len(self.cpu.__mem__)} Bytes): {len(self.cpu.__mem__)-list(self.cpu.__mem__.values()).count(0)}\npointers:{self.cpu.__point__}\nlabels:{self.cpu.__labels__}")
        # print("final regis by line")
        # print(self.history)
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
        code_part=[pargs,
                   fxop,
                   fcode,
                   self.nvram,
                   self.cpu.__mem__,
                   self.sig.decode(),
                   self.cpu.__labels__,
                   self.cpu.globl
                ]
        gen=generator(code_part)
        print("pargs")
        print(pargs)
        with open(file,"wb")as f:
            
            f.write(gen.dump(True))
    def read(self,file):
        gen=generator(None)
        reverses=gen.revert(file)
        # print(reverses[0])
        # print("reversed things")
        pargs,fxop,fcode,nvram,__mem__,self.sig,__labels__,__pos__=reverses
        self.cpu=self.paleta[self.sig](self)
        self.sig=self.sig.encode()
        self.cpu.__pos__=__pos__
        self.cpu.__mem__=__mem__
        self.cpu.__labels__=__labels__
        code=[]
        # print("codigo",fcode)
        # print(nvram)
        for i,index in enumerate(fcode):
            code.append(
                [getattr(self.cpu,fxop[index]),pargs[i]]
            )
        # print(code)
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
    # teste= compilador("codigo")
    if "riscv" in argv:
        teste=compilador("programa","riscv")
        with open(argv[1],"r")as f:
            lido=f.read()
        temp=risco_(lido,teste.cpu)
        # print(valores)
        # asyncio.run(teste.run(lido,parser=True))
        # teste.write(argv[-1])
        temp.init()
        teste.cpu.__mem__=temp.__memory__
        teste.cpu.__labels__=temp.__labels__
        print([(x[0],[x[1][0].__name__,x[1][1]]) for x in enumerate(temp.__code__)])
        asyncio.run(teste.run(temp.__code__,parser=False,reading=True))
    elif "riscv-c" in argv:
        
        teste=compilador("programa","riscv")
        with open(argv[1],"r")as f:
            lido=f.read()
        # valores=lx(lido,True)
        temp=risco_(lido)
        # print(valores)
        # asyncio.run(teste.run(lido,parser=True))
        # teste.write(argv[-1])
        temp.init()
        print(temp.__labels__)
            # print(teste.save)
    elif "pyos" in argv:
        teste=compilador("programa","pyos64")
        with open(argv[1],"r")as f:
            lido=f.read()
        temp=pyos_(lido,teste.cpu)
        # print(valores)
        # asyncio.run(teste.run(lido,parser=True))
        # teste.write(argv[-1])
        print("executou")
        temp.init()
        teste.cpu.__mem__=temp.__memory__
        teste.cpu.__labels__=temp.__labels__
        print([(x[0],[x[1][0].__name__,x[1][1]]) for x in enumerate(temp.__code__)])
        print(temp.__code__)
        print(temp.__high__)
        teste.cpu.__high__=temp.__high__
        teste.cpu.__lasts__=temp.__last_data__
        asyncio.run(teste.run(temp.__code__,parser=False,reading=True))
    elif "pyos-c" in argv:
        
        teste=compilador("programa","pyos64")
        with open(argv[1],"r")as f:
            lido=f.read()
        # valores=lx(lido,True)
        temp=pyos_(lido)
        # print(valores)
        # asyncio.run(teste.run(lido,parser=True))
        # teste.write(argv[-1])
        temp.init()
        print(temp.__labels__)
            # print(teste.save)
    elif "serial" in argv:
        teste=compilador("programa")
        teste.module_=True
        code,nv=teste.read(argv[1])
        asyncio.run(teste.run(code,inject=nv,reading=True))
    elif "rvserial" in argv:
        teste=compilador("programa","riscv")
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