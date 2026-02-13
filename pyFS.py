from sereal import generator,inode
class Disk:
    def __init__(self,file):
        try:
            self.vfs=open(file,"r+b")
        except:
            self.vfs=open(file,"w+b")
        self.toffset=0
        self.offset=0
    def __getitem__(self,item:slice|int):
        if isinstance(item, slice):
            self.vfs.seek(item.start or 0)
            return self.vfs.read((item.stop or 0) - (item.start or 0))
        
        self.vfs.seek(item)
        byte = self.vfs.read(1)
        if not byte:
            print("posição fora do alcance do arquivo")
        return byte[0]   # retorna o valor inteiro (0-255)
    def __setitem__(self,pos:int,value:list[int|dict|str]):
        fixed=generator(value)
        out=fixed.dump()
        self.vfs.seek(pos)
        self.vfs.write(out)
        self.offset=len(out)
        self.toffset=pos+self.offset
    def write0(self):
        self.vfs.truncate(0)
        self.vfs.seek(0)
    def table(self,value:bytes):
        self.toffset=len(value)
        self.vfs.seek(0)
        self.vfs.write(value)
    def __del__(self):
        try:
            self.vfs.close()
        except:
            pass
# tipos 
# 0 arquivo sys
# 1 pasta sys
# 2 dicionario
# 3 linker

class pyfs:
    disk=[]
    inodes=[]
    def __init__(self,disk0:Disk):
        self.disk.append(disk0)
        self.default_d=0
        
    def write_table(self,size:int):
        [self.inodes.append(inode(0,0,0)) for x in range(size)]
        self.inodes[0].b0=1
        self.inodes[0].b1=1
        self.inodes[0]=len(self.inodes[0])
        self.disk[0][1]=self.inodes
    # def read(self,iid:list[str,int]):
        
if __name__=="__main__":
    dx=Disk("disco.pyfs")
    fsx=pyfs(dx)    
    fsx.write_table(128)
