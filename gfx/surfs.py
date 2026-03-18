import pygame,numba,numpy as np,pickle
class surf(pygame.Surface):
    def __init__(self,size:tuple|list,flags:int=0,masks=None):
        super().__init__(size,flags,masks)
    def __getstate__(self)->np.ndarray:
        return pygame.surfarray.array3d(self)
    def __setstate__(self,value):
        temp=pygame.surfarray.make_surface(value)
        super().__init__(temp.get_size(),temp.get_flags())
        self.blit(temp,(0,0))

class shaders:
    def pixel(surface:surf)->np.ndarray:
        return surface.__getstate__()
    @numba.njit(parallel=True)
    def invert(buf:np.ndarray):
        h, w, _ = buf.shape
        for y in numba.prange(h):
            for x in range(w):
                buf[y,x,0] = 255 - buf[y,x,0]
                buf[y,x,1] = 255 - buf[y,x,1]
                buf[y,x,2] = 255 - buf[y,x,2]
    @numba.njit(parallel=True)
    def brightness(buf:np.ndarray, gain:float|int):
        h,w,_ = buf.shape
        for y in numba.prange(h):
            for x in range(w):
                for c in range(3):
                    v = buf[y,x,c] * gain
                    buf[y,x,c] = 255 if v > 255 else v
    @numba.njit(parallel=True)
    def pulse(buf:np.ndarray, t):
        h,w,_ = buf.shape
        g = (np.sin(t) + 1) * 0.5
        for y in numba.prange(h):
            for x in range(w):
                buf[y,x,0] *= g
                buf[y,x,1] *= g
                buf[y,x,2] *= g
    @numba.njit(parallel=True)
    def gradient(buf:np.ndarray):
        h,w,_ = buf.shape
        for y in numba.prange(h):
            for x in range(w):
                buf[y,x,0] = x * 255 // w
                buf[y,x,1] = y * 255 // h
                buf[y,x,2] = 128
    @numba.njit(parallel=True)
    def blur(src:np.ndarray, dst:np.ndarray):
        h,w,_ = src.shape
        for y in numba.prange(1, h-1):
            for x in range(1, w-1):
                for c in range(3):
                    s = (
                        src[y,x,c] +
                        src[y-1,x,c] + src[y+1,x,c] +
                        src[y,x-1,c] + src[y,x+1,c]
                    )
                    dst[y,x,c] = s // 5
    @numba.njit(parallel=True)
    def wave(src:np.ndarray, dst:np.ndarray, t):
        h,w,_ = src.shape
        for y in numba.prange(h):
            for x in range(w):
                ox = int(10 * np.sin(y*0.05 + t))
                sx = x + ox
                if 0 <= sx and sx < w:
                    dst[y,x] = src[y,sx]
if __name__=="__main__":
    teste=surf((100,100))
    param=surf((100,100))
    teste.fill((1,1,1))
    param.fill((1,0,0))
    teste.fill((255,255,255),pygame.Rect(10,10,10,10))
    pygame.init()
    temp2=shaders.pixel(param)
    temp=shaders.pixel(teste)
    tela=pygame.display.set_mode((100,100))
    clock=pygame.time.Clock()
    for i in range(3600):
        clock.tick(30)
        for event in pygame.event.get():
            pass
        tela.fill(0)
        teste.__setstate__(temp)
        tela.blit(teste,(0,0))
        shaders.wave(temp2,temp,0.1)
        pygame.display.flip()
    pygame.quit()
        