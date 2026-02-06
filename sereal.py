from math import log 
import gzip
def aux(file):
    with open(file,"rb")as f:
        while True:
            bt=f.read(1)
            if not bt:
                break
            yield bt
class generator:
    def __init__(self,parans=[]):
        self.paran=parans
        # self.gen_table[gen](self)
    def dump(self,file):
        self.start=self.__0__(self.paran)
        with open(file,"wb")as f:
            f.write(self.start)
        # print(gzip.compress(self.start))
    def revert(self,file):
        fx=aux(file)
        size=int.from_bytes(b"".join([next(fx) for nada in range(4)]))
        # print(size)
        vals=[]
        for index in range(size):
            tipo=int.from_bytes(next(fx))
            size2=int.from_bytes(b"".join([next(fx) for nada in range(4)]))
            rawdata=b"".join([next(fx) for nada in range(size2)])
            vals.append(self.__1__(tipo,rawdata))
        return vals
    def __0__(self,paran): #python types: str , int, list, dict
        ff=len(paran).to_bytes(4)
        for para in paran:
            # print(paran,para)
            temp=[]
            if isinstance(para,str):
                temp.append(00)
                temp.append(para.encode())
            elif isinstance(para,bool):
                temp.append(1)
                temp.append(para.to_bytes())
            elif isinstance(para,int):
                temp.append(2)
                if para >256:
                    temp.append(para.to_bytes(int(log(para,256)+1)))
                else:
                    temp.append(para.to_bytes())
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
            else:
                print(f"not implemented :: {type(para)} ::\n{paran}!\nYet...")
                # raise TypeError(type(para))
            temp.insert(1,len(temp[1]).to_bytes(4))
            tp=bytes([temp[0]])
            temp[0]=tp
            ff+=b"".join(temp)
        return ff
    def __1__(self,tipo,bits:bytes):
        if tipo==0:
            return bits.decode()
        if tipo==1:
            return bool.from_bytes(bits)
        if tipo==2:
            return int.from_bytes(bits)
        if tipo==3:
            vals=[]
            fx=iter(bits)
            size=int.from_bytes(b"".join([bytes([next(fx)]) for nada in range(4)]))
            for index in range(size):
                tipo=next(fx)
                size2=int.from_bytes(b"".join([bytes([next(fx)]) for nada in range(4)]))
                rawdata=bytes([next(fx) for nada in range(size2)])
                vals.append(self.__1__(tipo,rawdata))
            return vals
        if tipo==4:
            vals=[]
            fx=iter(bits)
            size=int.from_bytes(b"".join([bytes([next(fx)]) for nada in range(4)]))
            for index in range(size):
                tipo=next(fx)
                size2=int.from_bytes(b"".join([bytes([next(fx)]) for nada in range(4)]))
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
            size=int.from_bytes(b"".join([bytes([next(fx)]) for nada in range(4)]))
            for index in range(size):
                tipo=next(fx)
                size2=int.from_bytes(b"".join([bytes([next(fx)]) for nada in range(4)]))
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