
from timeit import default_timer as timer
import numpy as np


import sys
from PyQt5 import QtWidgets, QtGui, QtCore

w,h = 1024, 768
N = 30
rgba = np.random.randint(0,255,size=(N,h,w,4), dtype=np.uint8)
#for i in range(N):
#    rgba[i] = rgba[i]//16 + i*2
nframes=0
start = None


def run():
    global N, nframes, start
    a = QtWidgets.QApplication(sys.argv)
    l = QtWidgets.QLabel()
    l.resize(w,h)
    l.setPixmap( QtGui.QPixmap.fromImage( 
        QtGui.QImage(rgba[0],w,h,QtGui.QImage.Format_ARGB32)))
    l.show()
    def changepic():
        global N, nframes, start
        if start is None:
            start = timer()
        t0 = timer()
        nframes += 1
        i = QtGui.QImage(rgba[nframes%N],w,h,QtGui.QImage.Format_RGB32)
        t1 = timer()
        p = QtGui.QPixmap.fromImage( i )
        t2 = timer()
        l.setPixmap( p )
        t3 = timer()
        print("N %d fps %.3f %.3f %.3f %.3f"%(nframes,
         nframes/(t2-start),
         (t1-t0)*1e3,(t2-t1)*1e3,(t3-t2)*1e3))
        if nframes<100:
            QtCore.QTimer.singleShot( 1000/24, changepic )
        else:
            sys.exit()
    changepic()
    sys.exit( a.exec_() )

run()
