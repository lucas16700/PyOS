import pygame,pickle

class surf(pygame.Surface):
    def __init__(self,*kargs):
        super().__init__(*kargs)
    def __getstate__(self):
        temp=pygame.surfarray.array2d(self)
        return temp
    def __setstate__(self,value):
        temp=pygame.surfarray.make_surface(value)
        size=temp.get_size()
        super().__init__(size)
        self.blit(temp,(0,0))
class testes:
    def __init__(self,nome):
        self.nome=nome
    
# pygame.Surface()
# parede=surf((10,100))


# teste=pickle.dumps(parede)
# print(pickle.loads(teste))
# a=testes("lulala")
# print(a)