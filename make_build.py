from kernel import compilador as gcc,pyos64,asyncio
from fs.zipfs import ZipFS as vfs
from utils_grafic.surfs import pygame,pickle
from json import dumps as jdp ,loads as jld
import gzip,av,numpy as np,traceback
from hashlib import sha256
from sys import argv
# import PySimpleGUI as pg
os_version=1
class graph_encoding:
    def rgb(path:str):
        buf=pygame.image.load(path)
        temp=pygame.surfarray.array3d(buf)
        meta={
            "buff":temp,
            "size":buf.get_size(),
            "type":"rgb",
            "hash":sha256(temp.tobytes()).hexdigest()
            }
        print(sha256(temp.tobytes()).hexdigest())
        return gzip.compress(pickle.dumps(meta))
    def rgbl(path:list[str]):
        buf=[pygame.image.load(paths)for paths in path]
        temp=[pygame.surfarray.array3d(bx) for bx in buf]
        meta={
            "buff":temp,
            "size":[bx.get_size()for bx in buf],
            "type":"rgbl",
            "hash":sha256(temp.tobytes()).hexdigest()
            }        
        print(sha256(temp.tobytes()).hexdigest())
        return gzip.compress(pickle.dumps(meta))
    def png(path:str):
        with open(path,"rb")as f:
            return gzip.compress(pickle.dumps({"buff":f.read(),"size":None,"type":"png"}))
class app:
    def __init__(self,arch:str,name:str,version:int,load=False,sys=False):
        self.arch=arch
        self.main=name+".asm"
        self.rname=name
        self.version=version
        if sys:
            self.files=vfs(f"{name}",write=False)
        else:
            self.files=vfs(f"./temp/{name}.pozip",write=not load)
    def build(self,schema):
        for obj in schema["graphics"]:
            self.files.writebytes("gx."+obj["name"],
                                getattr(graph_encoding,
                                        obj["encoding"])(obj["path"]))
        with open(schema["main"],"r")as f:
            self.files.writetext("main.asm",f.read())
        self.files.writetext("inject.json",jdp(schema["nvram"]))
        for modules in schema["modules"]:
            with open(modules,"r")as f:
                self.files.writetext("libs."+modules,f.read())
        # print(final)
    async def __run__(self):
        runtime=gcc(self.rname)
        run=await runtime.run(self.files.readtext("main.asm"),inject=jld(self.files.readtext("inject.json")))
        print("starting",self.main)
    def run(self):
        asyncio.run(self.__run__())
if len(argv)>0:
    try:
        file=app("pyos64",argv[-1],0,sys=True)
        file.run()
    except:
        print(argv)
        traceback.print_exc()
        
else:

        print(argv)
# meu_app=app("pyos","mojang",10)

# meu_app.add_file("./teste_UI.asm","main.asm")

# print(meu_app.read_file("main.asm"))
# meu_app.files.close()