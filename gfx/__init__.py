import pygame,numpy as np

class memory:
    def __init__(self,size):
        self.textures=np.zeros(size,dtype=np.uint8)
        self.vram=np.zeros(size,dtype=np.uint8)
        self.shapes={
            0:[800,600]
        }
        self.tick=0
        self.size=[size,1,1]
        self.mmap={
            0:{
                0:[0,size],
                1:0 #contagem de get
            }
        }
    def init(self):
        pygame.init()
        self.vram[0]=255
        
    def __getitem__(self, key):
        if isinstance(key,str):
            tipo,chave,aux= [int(x) for x in key.split(":")]
            if tipo==1:
                return self.shapes[chave][aux]
            elif tipo==0:
                return self.mmap[chave][aux]
            elif tipo==2:
                return self.size[chave]
        elif isinstance(key,list):
            tipo,chave,aux= key
            if tipo==1:
                return self.shapes[chave][aux]
            elif tipo==0:
                return self.mmap[chave][aux]
            elif tipo==2:
                return self.size[chave]
    def __setitem__(self, key, value):
        if isinstance(key,str):
            tipo,chave,aux= [int(x) for x in key.split(":")]
            if tipo==1:
                self.shapes[chave][aux]=value
            elif tipo==0:
                self.mmap[chave][aux]=value
        elif isinstance(key,list):
            tipo,chave,aux= key
            if tipo==1:
                self.shapes[chave][aux]=value
            elif tipo==0:
                self.mmap[chave][aux]=value
class gfx:
    def __init__(self,size:list[int],flags=None):
        pygame.init()
        self.window=pygame.display.set_mode(size,flags,1)
        self.frames={0:pygame.Surface(size)}
        self.frames_p={0:[0,0]}
        self.order=[0]
        self.update_rect=pygame.Rect([0,0],size)
    def flip(self):
        pygame.display.flip()
    def update(self):
        pygame.display.update(self.update_rect)
    def events(self):
        for event in pygame.event.get():
            yield event
    def blit(self,surface,pos):
        self.window.blit(surface,pos)
    def stack_frame(self,surface,pos):
        nid=len(self.frames)
        self.frames[nid]=surface
        self.order.append(nid)
        self.frames_p[nid]=pos
    def stack_change(self,nid,pos):
        self.order.remove(nid)
        self.order.insert(pos,nid)
    def stack_blit(self):
        for i in self.order:
            self.window.blit(self.frames[i],self.frames_p[i])