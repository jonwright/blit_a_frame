
from timeit import default_timer as timer
import numpy as np



import pygame, os

w,h = 1024, 768
N = 30
rgba = np.random.randint(0,255,size=(N,h,w,4), dtype=np.uint8)
#for i in range(N):
#    rgba[i] = rgba[i]//16 + i*2
nframes=0
start = 0

def run():
    global N, nframes, start
    os.putenv("SDL_VIDEODRIVER",'directx' )
    pygame.display.init()
    screen = pygame.display.set_mode( (w,h), pygame.DOUBLEBUF )
    img = pygame.image.frombuffer( rgba[0],(w,h) , "RGBX" )
    screen.blit( img, (0,0) )
    pygame.display.update()    

    def changepic():
        global N, nframes, start
        t0 = timer()
        nframes += 1
        img = pygame.image.frombuffer( rgba[nframes%N],(w,h),  "RGBX")
        t1 = timer()
        screen.blit( img, (0,0) )
        t2 = timer()
        pygame.display.flip()    
        t3 = timer()
        print("N %d fps %.3f %.3f %.3f %.3f"%(nframes,
         nframes/(t2-start),
         (t1-t0)*1e3,(t2-t1)*1e3,(t3-t2)*1e3))
        
    while 1:
        for evt in pygame.event.get():

            if evt.type == pygame.QUIT:
                return
        
        changepic( )

run()
