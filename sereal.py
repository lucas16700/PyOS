from math import log
import gzip
# from hashlib import sha256
# from random import randbytes
import numpy as np
class __mems__:
        def __init__(self,size):
            self.r=np.zeros(size, dtype=np.uint8)
            self.r
        def __getitem__(self,__key):
            return self.r[__key]
        def __setitem__(self,__key,__value):
            self.r[__key]=__value
        def get(self,key,default=0):
            try:
                return self.r[key]
            except:
                return default
        def __len__(self):
            return len(self.r)
        def values(self):
            return self.r
class inode:
    def __init__(self,tip:int=0,aloc:int=0,offset:int=0):
        self.b0=tip
        self.b1=aloc
        self.b2=offset
        self.sub=0
        self.size=0
    def __len__(self):
        return len(generator([self]).dump())-1
class layout:
    def __init__(self,dict_layout:dict):
        self.value=dict_layout["value"]
        self.style=dict_layout["style"]
        self.type=dict_layout["type"]
        self.events=dict_layout["events"]
        self.child={key:layout(dict_layout["childs"][key])for key in dict_layout["childs"]}
zipado=False
def aux(file):
    if zipado:
        with gzip.open(file,"rb")as f:
            while True:
                bt=f.read(1)
                if not bt:
                    break
                yield bt
    else:
        with open(file,"rb")as f:
            while True:
                bt=f.read(1)
                if not bt:
                    break
                yield bt
class generator:
    max_int=8
    def __init__(self,parans=[]):
        self.paran=parans
        # self.gen_table[gen](self)
    def dump(self,file:str=None,debug=False):
        self.start=self.__0__(self.paran)
        if isinstance(file,str):
            with open(file,"wb")as f:
                f.write(gzip.compress(self.start))
        # print(self.start.count(b"\x00")/len(self.start)*100)
        return self.start
        # print(gzip.compress(self.start))
    def revert(self,file):
        fx=aux(file)
        size=int.from_bytes(b"".join([next(fx) for nada in range(self.max_int)]))
        # print(size)
        vals=[]
        for index in range(size):
            tipo=int.from_bytes(next(fx))
            size2=int.from_bytes(b"".join([next(fx) for nada in range(self.max_int)]))
            rawdata=b"".join([next(fx) for nada in range(size2)])
            vals.append(self.__1__(tipo,rawdata))
        return vals
    def reverts(self,data):
        fx=iter(data)
        size=int.from_bytes(bytes([next(fx) for nada in range(self.max_int)]))
        # print(size)
        vals=[]
        for index in range(size):
            tipo=int.from_bytes(bytes([next(fx)]))
            size2=int.from_bytes(bytes([next(fx) for nada in range(self.max_int)]))
            rawdata=bytes([next(fx) for nada in range(size2)])
            vals.append(self.__1__(tipo,rawdata))
        return vals
    
    def __0__(self,paran): #python types: str , int, list, dict
        ff=len(paran).to_bytes(self.max_int)
        for para in paran:
            # print(paran,para)
            temp=[]
            if isinstance(para,str):
                temp.append(00)
                size=len(para)
                temp.append((int.from_bytes(para.encode())).to_bytes(size,signed=True))
            elif isinstance(para,bool):
                temp.append(1)
                temp.append(para.to_bytes())
            elif isinstance(para,int):
                temp.append(2)
                temp.append(para.to_bytes(self.max_int))
            elif isinstance(para,list):
                temp.append(3)
                temp.append(self.__0__(para))
            elif isinstance(para,dict):
                temp.append(4)
                keys=para.keys()
                val=[para[x] for x in keys]
                # print(val)
                temp.append(self.__0__([list(keys),val]))
            elif isinstance(para,tuple):
                temp.append(5)
                temp.append(self.__0__(para))
            elif isinstance(para,bytes):
                temp.append(6)
                temp.append(para)
            elif isinstance(para,inode):
                temp.append(255)
                temp.append(self.__0__([para.b0,para.b1,para.b2,para.sub]))
            elif isinstance(para,layout):
                temp.append(254)
                temp.append(self.__0__([para.child,para.events,para.style,para.type,para.value]))
            elif isinstance(para,type(None)):
                temp.append(7)
                temp.append(bytes(1))
            elif isinstance(para,__mems__):
                temp.append(253)
                temp.append(bytes(para.r))
            else:
                print(f"not implemented :: {type(para)} ::\n{paran}!\nYet...")
                # raise TypeError(type(para))
            temp.insert(1,len(temp[1]).to_bytes(self.max_int))
            tp=bytes([temp[0]])
            temp[0]=tp
            ff+=b"".join(temp)
        return ff
    def __1__(self,tipo,bits:bytes):
        if tipo==0:
            return (int.from_bytes(bits,signed=True)).to_bytes(len(bits),signed=True).decode()
        if tipo==255:
            vals=[]
            fx=iter(bits)
            # size=int.from_bytes(b"".join([bytes([next(fx)]) for nada in range(self.max_int)]))
            for index in range(4):
                tipo=next(fx)
                size2=int.from_bytes(b"".join([bytes([next(fx)]) for nada in range(self.max_int)]))
                rawdata=bytes([next(fx) for nada in range(size2)])
                vals.append(self.__1__(tipo,rawdata))
            return inode(*vals)
        if tipo==254:
            vals=[]
            fx=iter(bits)
            # size=int.from_bytes(b"".join([bytes([next(fx)]) for nada in range(self.max_int)]))
            for index in range(5):
                tipo=next(fx)
                size2=int.from_bytes(b"".join([bytes([next(fx)]) for nada in range(self.max_int)]))
                rawdata=bytes([next(fx) for nada in range(size2)])
                vals.append(self.__1__(tipo,rawdata))
            return layout(*vals)
        if tipo==253:
            temp=__mems__(len(bits))
            for i,mem in enumerate(bits):
                temp[i]=int(mem)
            return temp
        if tipo==6:
            return bits
        if tipo==1:
            return bool.from_bytes(bits)
        if tipo==2:
            return int.from_bytes(bits)
        if tipo==3:
            vals=[]
            fx=iter(bits)
            size=int.from_bytes(b"".join([bytes([next(fx)]) for nada in range(self.max_int)]))
            for index in range(size):
                tipo=next(fx)
                size2=int.from_bytes(b"".join([bytes([next(fx)]) for nada in range(self.max_int)]))
                rawdata=bytes([next(fx) for nada in range(size2)])
                vals.append(self.__1__(tipo,rawdata))
            return vals
        if tipo==7:
            return None
        if tipo==4:
            vals=[]
            fx=iter(bits)
            size=int.from_bytes(b"".join([bytes([next(fx)]) for nada in range(self.max_int)]))
            for index in range(size):
                tipo=next(fx)
                size2=int.from_bytes(b"".join([bytes([next(fx)]) for nada in range(self.max_int)]))
                rawdata=bytes([next(fx) for nada in range(size2)])
                vals.append(self.__1__(tipo,rawdata))
            dt={}
            keys,val=vals
            for i,key in enumerate(keys):
                dt[key]=val[i]
            return dt
        if tipo==5:
            vals=[]
            fx=iter(bits)
            size=int.from_bytes(b"".join([bytes([next(fx)]) for nada in range(self.max_int)]))
            for index in range(size):
                tipo=next(fx)
                size2=int.from_bytes(b"".join([bytes([next(fx)]) for nada in range(self.max_int)]))
                rawdata=bytes([next(fx) for nada in range(size2)])
                vals.append(self.__1__(tipo,rawdata))
            return tuple(vals)
    def __2__(self): #rgb lrgb
        pass
    gen_table={
        b"\00":__0__,
        b"\01":__1__,
        b"\02":__2__
    }

if __name__=="__main__":
    a=[{
    'corpo': {
        'value': '',
        'style': {
            'size': [400, 200], 
            'border radius': 50, 
            'background': [255, 0, 0, 100], 
            'position': [300, 300]},
        'type': 'Box',
        'events':{
            'hover_leave':{
                "script": (("change_style" ,"background", [255, 0, 0, 100]),()),
                "JIT": True
            },
            'hover_enter':{
                "script": (("change_style" ,"background", [255, 0, 0, 255]),()),
                "JIT": True
            }
            }
        ,'child': {
            'butao1': {
                'events':{
                    'hover_leave':{
                        "script": (("change_style" ,"background", [0, 0, 255, 100]),()),
                        "JIT": True
                    },
                    'hover_enter':{
                        "script": (("change_style" ,"background", [0, 0, 255, 200]),()),
                        "JIT": True
                    },
                    'click_in':{
                        "script": (("start_app" ,"programa.asm", True),()),
                        "JIT": True
                    }
                    },
                'style': 
                {'border radius': 15, 
                'size': [100, 30], 
                'color': [0, 0, 0], 
                'background': [255, 255, 255]}, 
                'type': 'Button', 
                'value': 'pressione'
                },
            'blocos': {
                'events':{
                    'hover_leave':{
                        "script": (("change_style" ,"background", [0, 255, 0, 100]),()),
                        "JIT": True
                    },
                    'hover_enter':{
                        "script": (("change_style" ,"background", [0, 255, 0, 255]),()),
                        "JIT": True
                    }
                    },
                'style': 
                {'size': [300, 130], 
                'border radius': 50, 
                'background': [2, 50, 40], 
                'position': [0, 0]},
                'type': 'Box',
                'value': '',
                'child': {
                    'butao1': {'events':{
                    'hover_leave':{
                        "script": (("change_style" ,"background", [0, 0, 255, 100]),()),
                        "JIT": True
                    },
                    'hover_enter':{
                        "script": (("change_style" ,"background", [0, 0, 255, 200]),()),
                        "JIT": True
                    }
                    },
                        'style': 
                        {'border radius': 15, 
                        'size': [70, 60], 
                        'color': [0, 0, 0], 
                        'background': [255, 255, 255]}, 'type': 'Button', 
                        'value': 'pressione'}
                }
            }
        }
    }
}]
    g=generator(a)
    g.dump("temp.serial")
    cmp=g.revert("temp.serial")
    print(cmp==a)