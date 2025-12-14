import shlex
from pympler import asizeof
from sys import argv
from pickle import dumps , loads
ideia="""mov $1 a
mov "#hello world" b
syscall
mov $10
halt"""
print(str(argv))
with open("/Users/lucaschaves/projeto_os/log.txt","w")as f:
        f.write(str(argv))

from pyos import pyos16,pyos64
class compilador:
    def __init__(self,nome:str,arch:str="pyos64"):
        self.n=nome.encode()
        self.sig=arch.encode()
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
    opcode=[
        "mov",
        "movr",
        "movx",
        "syscall",
        "jmp",
        "add",
        "sub",
        "mul",
        "div",
        "halt",
        "cmp",
        "eval",
        "set",
        "watch",
        "nwatch",
        "trace",
        "AND",
        "OR",
        "NOT",
        "SHL",
        "SHR",
        "inc",
        "xinc",
        "xneg",
        "neg",
        "call",
        "ret",
        "pop",
        "push",
        "load",
        "store",
        "loop",
        "xloop",
        "module"
    ]
    opreg=[
        "a",
        "b",
        "c",
        "d",
        "x",
        "r0",
        "r1",
        "r2",
        "r3",
        "rx",
        "ry",
        "rz"
    ]
    optypes={
        "!":b"\x01",    #bytes
        "#":b"\x02",    #str
        "$":b"\x03",    #int
        "@":b"\x04"     #img
    }
    def item_parser(self,code):
        op=code[0]
        items=[]
            # print(tread.pos)
            # print(actin[tread.pos])
        for i in code[1:]:
            if "#" in i:
                ni=i.replace("#","")
                items.append(ni)
            elif "$" in i:
                ni=i.replace("$","")
                items.append(int(ni))
                # print("used")
            
            elif "!" in i:
                ni=i.replace("!","")
                items.append(bool(ni))
            else:
                items.append(i)
        return op,items
    def run(self,code:str,save=True):
        Ccode=[]
        tread=compilador.paleta[self.sig](self)
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
        tread.__code__=[self.item_parser(shlex.split(line)) for line in tratado]
        
        while tread.reg["x"]:
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
            op,items=tread.__code__[tread.__pos__]
            getattr(tread,op)(items)
            # if len(items)>=1:
            #     if items[-1] in tread.w_list:
            #         print(f"NEW : {tread.reg[items[-1]]}")
            # print(tread.pos)
            tread.__pos__+=1
        # print(tread.reg)
        self.reg=tread.cpu_state=tread
        if save:
            # print(tread.func)
            return tread.__code__,tread.func
    def write(self,save,func):
        app=b""
        code=[]
        data=[]
        data_index=0
        # print(func)
        for line in save:
            # print(line)
            subcode=[self.opcode.index(line[0]).to_bytes()]
            # print(line,len(line),len(line).to_bytes())
            
            subcode.append(int(len(line)-1).to_bytes())
            for arg in line[1:]:
                if "#"  in arg or "@"  in arg or "!"  in arg:
                    subcode.append(b"\x02")
                    subcode.append(int(data_index).to_bytes())
                    data.append(arg)
                    data_index+=1
                elif "$" in arg:
                    if int(arg.replace("$",""))<255 and int(arg.replace("$",""))>-1:
                        subcode.append(b"\x01")
                        # print(arg)
                        subcode.append(int(arg.replace("$","")).to_bytes(signed=True))
                    else:
                        subcode.append(b"\x02")
                        subcode.append(int(data_index).to_bytes())
                        data.append(arg)
                else:
                    subcode.append(b"\x03")
                    subcode.append(self.opreg.index(arg).to_bytes())
            code.append(subcode)
        fcode=b""
        for scode in code:
            fcode+=b"".join(scode)
        funcs={}
        for key in func:
            funcs[key]=[]
            for real in func[key]:
                # print(line)
                subcode=[self.opcode.index(real[0]).to_bytes()]
                # print(real,len(real),len(real).to_bytes())
                
                subcode.append(int(len(real)-1).to_bytes())
                for arg in real[1:]:
                    if "#"  in arg or "@"  in arg or "!"  in arg:
                        subcode.append(b"\x02")
                        subcode.append(int(data_index).to_bytes())
                        data.append(arg)
                        data_index+=1
                    elif "$" in arg:
                        if int(arg.replace("$",""))<255 and int(arg.replace("$",""))>-1:
                            subcode.append(b"\x01")
                            # print(arg)
                            subcode.append(int(arg.replace("$","")).to_bytes(signed=True))
                        else:
                            subcode.append(b"\x02")
                            subcode.append(int(data_index).to_bytes())
                            data.append(arg)
                    else:
                        subcode.append(b"\x03")
                        subcode.append(self.opreg.index(arg).to_bytes())
                funcs[key].append(subcode)
        final_func=len(funcs).to_bytes()
        for key in funcs:
            tfunc=len(key).to_bytes(2)
            tfunc+=key.encode()
            # print("funcs key=",key,funcs[key])
            tjoin=[]
            for line in funcs[key]:
                tjoin.append(b"".join(line))
            fjoin=b"".join(tjoin)
            # print("func",fjoin)
            fsize=len(fjoin).to_bytes(2)
            final_func+=tfunc+fsize+fjoin


        fdata=b""
        for DATA in data:
            fdata+=self.optypes[DATA[0]]
            DATA.replace(DATA[0],"")
            fdata+=len(DATA).to_bytes()
            fdata+=DATA.encode()
        meta=len(self.sig).to_bytes()+self.sig+len(self.n).to_bytes()+self.n
        offsetcode=len(meta)+24
        offsetdata=len(fcode)+offsetcode
        offsetfunc=len(fdata)+offsetdata
        meta+=offsetcode.to_bytes(8)+offsetdata.to_bytes(8)+offsetfunc.to_bytes(8)
        app=meta+fcode+fdata+final_func
        # print(app)
        return app
        # with open("temp.pyapp","wb")as f:
        #     f.write(app)
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
    def read(self,bin):
        arch_len=int(bin[0])+1
        arch=bin[1:arch_len]
        name_len=int(bin[arch_len])+1
        name=bin[arch_len+1:arch_len+name_len]
        codeoffset=int.from_bytes(bin[arch_len+name_len:arch_len+name_len+8])
        off=arch_len+name_len+8
        dataoffset=int.from_bytes(bin[off:off+8])
        funcoffset=int.from_bytes(bin[off+8:off+16])
        # print(codeoffset,dataoffset)
        code=bin[codeoffset:dataoffset]
        data=bin[dataoffset:funcoffset]
        funco=bin[funcoffset:]
        # print(code,"\n",data)
        fcode=[]
        bvar_index=0
        bin_var=[]
        data_off=0
        while True:
            try:
                Super_t=self.optypes.items()
                for n in Super_t:
                    if data[data_off].to_bytes() in n:
                        data_key=n[0]
                        break
                data_off+=1
                # print(data_key)
                size=data[data_off]
                # print("data:",data[data_off+1:size+data_off+1])
                bin_var.append(data[data_off+1:size+data_off+1])
                data_off+=size+1
            except:
                # print(bin_var)
                break
        code_off=0
        b_index=0
        while True:
            try:
                instruc=[self.opcode[code[code_off]]]
                code_off+=1
                # print("len:",code[code_off])
                for i in range(code[code_off]):
                    code_off+=1
                    # print("caracter",code[code_off])
                    if code[code_off]==1:
                        code_off+=1
                        instruc.append(code[code_off])
                    elif code[code_off]==3:
                        code_off+=1
                        instruc.append(self.opreg[code[code_off]])
                    elif code[code_off]==2:
                        code_off+=1
                        instruc.append(bin_var[b_index])
                        b_index+=1
                code_off+=1
                # print("instruc",instruc)
                fcode.append(instruc)
            except:
                # print("final code:",fcode)
                break
        funcs={}
        funco_off=1
        # print("len function",funco[0])
        for i in range(funco[0]):
            funco_off+=1
            name_l=funco[funco_off]
            funco_off+=1
            # print("name len",name_l)
            key_name=funco[funco_off:name_l+funco_off]
            funcs[key_name]=[]
            funco_off+=name_l
            xsize=int.from_bytes(funco[funco_off:funco_off+2])
            funco_off+=2
            func=funco[funco_off:xsize+funco_off]
            # print("func ",func)
            funco_off+=xsize
            func_off=0
            while True:
                try:
                    instruc=[self.opcode[func[func_off]]]
                    func_off+=1
                    # print("len:",code[code_off])
                    for i in range(func[func_off]):
                        func_off+=1
                        # print("caracter",code[code_off])
                        if func[func_off]==1:
                            func_off+=1
                            instruc.append(func[func_off])
                        elif func[func_off]==3:
                            func_off+=1
                            instruc.append(self.opreg[func[func_off]])
                        elif func[func_off]==2:
                            func_off+=1
                            instruc.append(bin_var[b_index])
                            b_index+=1
                    func_off+=1
                    # print("instruc",instruc)
                    funcs[key_name].append(instruc)
                except:
                    # print("final code:",fcode)
                    break
        # print("final_func",funcs)
        return fcode,funcs
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
teste= compilador("codigo")
if ".bin" in argv[1]:
    with open(argv[1],"rb")as f:
        app=teste.read(f.read())
        teste.start(*app)
else:
    with open(argv[1],"r")as f:
        app=teste.run(f.read())
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