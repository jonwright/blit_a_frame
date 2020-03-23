
from timeit import default_timer as timer
import numpy as np, sys



from PIL import Image, ImageTk
import tkinter 
w,h = 1024, 768
N = 30
rgba = np.random.randint(0,255,size=(N,h,w,4), dtype=np.uint8)
nframes=0
start = None

def runTk():
    global N, nframes, start
    root = tkinter.Tk(sync=0)
    frm = ImageTk.PhotoImage( Image.fromarray(rgba[0], "RGBX")) 
    l = tkinter.Label(root, width=w, height=h , image = frm )
    l.frm = frm
    l.pack()

    def changepic():
        global N, nframes, start
        if start is None:
            start = timer()
        t0 = timer()
        nframes += 1
        i = Image.fromarray( rgba[nframes%N], "RGBX" ) 
        t1 = timer()
        l.frm.paste(i)
        t2 = timer()
        l.update_idletasks()
        t3 = timer()
        print("N %d fps %.3f %.3f %.3f %.3f"%(nframes,
         nframes/(t2-start),
         (t1-t0)*1e3,(t2-t1)*1e3,(t3-t2)*1e3))
        if nframes>100:
            sys.exit()
        else:
            l.after(1, changepic)
    
    l.after(1, changepic)
    start =timer()
    l.mainloop()

runTk()
