"""
misc useful function by Nemo
"""
import cv2
import cv2.cv as cv
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import re
import sympy as sp



def lazy_import():
    print """
from numpy import *
import numpy as np
import cv2
import os
#import time
#import sys
import _NEMOpy as npy
import matplotlib as mpl
from matplotlib import pyplot as plt
import re
# import networkx as nx
#from sympy import *
#init_printing()
if "__builtin__" in globals(): 
    if "__IPYTHON__" in vars(__builtin__): 
        %matplotlib inline
"""

#%%

def isRunFromIDE():
    return (('spyderlib.utils.external.path' in sys.modules) or
            ('spyder.utils.spyder' in sys.modules) or
            ('spyder.config.main' in sys.modules))
    
    

#%%
def readtxt(fln,aslist=False):
    "simple read text file"
    with open(fln,'r') as f:
        txt=f.readlines() if aslist else f.read() 
    return txt	


def warning( *objs): 
    print >> sys.stderr, objs


def plot3dWireframe(Z):
    from matplotlib import cm
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    szy,szx=Z.shape
    X = np.arange(szx)
    Y = np.arange(szy)
    X, Y = np.meshgrid(X, Y)
    surf = ax.plot_wireframe(X,Y, Z)
    plt.show()
    return surf

def plot3dSurf(Z):
    from matplotlib import cm
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    szy,szx=Z.shape
    X = np.arange(szx)
    Y = np.arange(szy)
    X, Y = np.meshgrid(X, Y)
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
    plt.show()
    return surf

def firstParamAsDirORcurDir():
    "return argv[1] as dir or use current dir"
    if len(sys.argv)>1:
        arg1=sys.argv[1]
        if os.path.exists(arg1):
            if os.path.isdir(arg1):
                dir1=os.path.abspath(arg1)
    else:
        dir1=os.path.abspath(os.curdir)
    return dir1

def imshow_BGR_byMPL(img,szw=8,szh=7):
    "Show BGR image (i.e. loaded by opencv) usig matplotlib (as RGB)"
    #imgd=np.empty_like(img)
    #imgd[:,:,2],imgd[:,:,1],imgd[:,:,0]=img[:,:,0],img[:,:,1],img[:,:,2]
    #plt.imshow(imgd)
    plt.imshow(cv2.cvtColor(img,cv2.cv.CV_BGR2RGB))
    plt.gcf().set_size_inches(szw,szh)

def imshow_Gr(img,szw=8,szh=7):
    "Show gray image by matplotlib"	
    plt.imshow(img,cmap='gray')
    plt.gcf().set_size_inches(szw,szh) 

def mplssz(szw=8,szh=7):
    "set size for plotted by matplotlib (inch)"	
    plt.gcf().set_size_inches(szw,szh) 

def mplGridSzAndCross(szw=8,szh=7,cross=True,spineCross=False):
    "set size grid and cross axes"      
    plt.gcf().set_size_inches(szw,szh)     
    plt.grid(True)
    plt.box(False)
    if cross:
        plt.axvline(color='k',alpha=0.6)
        plt.axhline(color='k',alpha=0.6)
        
    if spineCross:
        plt.box(True)
        ax=plt.gca()
        ax.spines[u'bottom'].set_position('zero')
        ax.spines[u'left'].set_position('zero')
        ax.spines[u'right'].set_visible(False)
        ax.spines[u'top'].set_visible(False)

def mplAddYaxisWsameX(label='',relpos=10,alpha=0.6):
    f=plt.gcf()
    ax=plt.gca()
    newax = f.add_axes(ax.get_position())    
    newax.yaxis.set_label_position('right')
    newax.yaxis.set_ticks_position('right')
    newax.yaxis.set_label_text(label)
    z=newax.spines['right']
    z.set_alpha(alpha)
    newax.spines['right'].set_position(('outward', relpos))
    # newax.spines['bottom'].set_position(('outward', 20))
    # newax.patch.set_visible(False)
    newax.xaxis.set_visible(False)
    newax.set_xlim(ax.get_xlim())
    

def mplRc_RusViaLaTeX():
    """ russian chars via set usetex and style
    solution from http://s.arboreus.com/2009/04/cyrillic-letters-in-matplotlibpylab.html http://koldunov.net/?p=290#comments
    Usiliyami nekogo Alekseya segodnya my vse nakonec uznali kak v Matplotlib/Pylab delat' podpisi po-russki.
    """
    import matplotlib
    # rc('font',**{'family':'serif'})
    matplotlib.rc('text', usetex=True)
    matplotlib.rc('text.latex',unicode=True)
    matplotlib.rc('text.latex',preamble='\usepackage[utf8]{inputenc}')
    matplotlib.rc('text.latex',preamble='\usepackage[russian]{babel}')

def mplRc_RusViaFonts():#u'font.family': [u'sans-serif'],):
    """ russian chars via set fonts. to change fontFamily- set i.e. mpl.rcParams[u'font.family']= [u'monospace']
    solution from http://pyviy.blogspot.ru/2009/06/matplotlib.html
    """
    import matplotlib
    matplotlib.rcParams[u'font.serif']= [u'Verdana',u'Arial']
    matplotlib.rcParams[u'font.serif']= [u'Verdana',u'Arial']
    matplotlib.rcParams[u'font.sans-serif']= [u'Tahoma',u'Arial']
    matplotlib.rcParams[u'font.cursive']= [u'Courier New',u'Arial']
    matplotlib.rcParams[u'font.fantasy']= [u'Comic Sans MS',u'Arial']
    matplotlib.rcParams[u'font.monospace']= [u'Courier New']

def mplRc_FontSize(sz=10.0):
    "set rcParams[u'font.size']  def=10.0 "
    import matplotlib
    matplotlib.rcParams[u'font.size']= sz








def findlike(ar,subs):
    "find in strarray somthing containing subs. return s"
    for s in ar:
        if s.find(subs)>=0:
            return s







def distxy(a,b): 
    "dist from pt A to pt B where A have coord a=[x,y[,z]]"
    return ((a-b)**2).sum()**.5

	
def absv (a):
    "length for vector a (x,y)"
    return np.absolute(a[0]+a[1]*1j)
	
def anglev (a):
    "angle for vector a (x,y) // remember y coord on most images is inverted!"
    return np.angle(a[0]+a[1]*1j)


def normalizeArSchifted(ar,scaleTo=1):
    "return array normalized from 0 to scaleTo"
    m=ar.min()
    ptp=ar.ptp()
    return (ar-m)*(scaleTo/ptp)

def cvtImg2Uint8(im):
    return np.uint8( normalizeArSchifted(im,256) )








def tickArray(w,minQlabels=10):
    dx=10**int((np.log10(w)))
    k=0
    while int( (w-0) / (dx/2**k))<minQlabels:k+=1
    ar=np.hstack((np.arange(0,w, dx/2**k ),[w]))    
    return ar


def imshow_(img,colormap='gray',szw=8,szh=7,adapt4screensize=(1024,1280),minQlabels=5):
    """unuversal imshow form matplotlib imshow. RGB for BGR and default Grayscale for others 
    
        adapt4screensize=(1024,1280) - image decimated to this+ size to fit screen and not overuse memory. Use None to not decimate
        
        minQlabels - (use only for adapt4screensize<>None) - minQlabels for axis adaptive labels

        remember: matplotlib colormap names is:

        cmaps = [('Sequential',     ['Blues', 'BuGn', 'BuPu',
                                     'GnBu', 'Greens', 'Greys', 'Oranges', 'OrRd',
                                     'PuBu', 'PuBuGn', 'PuRd', 'Purples', 'RdPu',
                                     'Reds', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd']),
                 ('Sequential (2)', ['afmhot', 'autumn', 'bone', 'cool', 'copper',
                                     'gist_heat', 'gray', 'hot', 'pink',
                                     'spring', 'summer', 'winter']),
                 ('Diverging',      ['BrBG', 'bwr', 'coolwarm', 'PiYG', 'PRGn', 'PuOr',
                                     'RdBu', 'RdGy', 'RdYlBu', 'RdYlGn', 'Spectral',
                                     'seismic']),
                 ('Qualitative',    ['Accent', 'Dark2', 'Paired', 'Pastel1',
                                     'Pastel2', 'Set1', 'Set2', 'Set3']),
                 ('Miscellaneous',  ['gist_earth', 'terrain', 'ocean', 'gist_stern',
                                     'brg', 'CMRmap', 'cubehelix',
                                     'gnuplot', 'gnuplot2', 'gist_ncar',
                                     'nipy_spectral', 'jet', 'rainbow',
                                     'gist_rainbow', 'hsv', 'flag', 'prism'])]
    """
    h,w= img.shape[:2]
    if adapt4screensize<>None:
        d=1
        while (h/(d+1)>adapt4screensize[0]) or (w/(d+1)>adapt4screensize[1]):d+=1
        #print '~',d,h/d,w/d
        img=img[::d,::d]
        
    if colormap=='gray':
        if img.ndim==3:
            if img.shape[2]==3:
                plt.imshow(cv2.cvtColor(img,cv2.cv.CV_BGR2RGB))
        else:
            plt.imshow(img,colormap)
    
    if adapt4screensize<>None:
        minQlabels1=minQlabels
        tax=tickArray(w,minQlabels1)
        tay=tickArray(h,minQlabels1)
        plt.xticks(tax/d,[str(x) for x in tax],rotation=33);
        plt.yticks(tay/d,[str(x) for x in tay]);

    plt.gcf().set_size_inches(szw,szh)


def imshow_2(img,colormap='gray',szw=8,szh=7,norm=None, aspect=None, interpolation=None, alpha=None, 
             vmin=None, vmax=None, origin=None, extent=None, shape=None, filternorm=1, filterrad=4.0, 
             imlim=None, resample=None, url=None, hold=None,adapt4screensize=(1024,1280),minQlabels=5):    
    """unuversal imshow form matplotlib imshow. RGB for BGR and default Grayscale for others 

	adapt4screensize=(1024,1280) - image decimated to this+ size to fit screen and not overuse memory. Use None to not decimate

	minQlabels - (use only for adapt4screensize<>None) - minQlabels for axis adaptive labels
        
        see matplotlib.pyplot.imshow for param details
        remember: matplotlib colormap names is:
        cmaps = [('Sequential',     ['Blues', 'BuGn', 'BuPu',
                                     'GnBu', 'Greens', 'Greys', 'Oranges', 'OrRd',
                                     'PuBu', 'PuBuGn', 'PuRd', 'Purples', 'RdPu',
                                     'Reds', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd']),
                 ('Sequential (2)', ['afmhot', 'autumn', 'bone', 'cool', 'copper',
                                     'gist_heat', 'gray', 'hot', 'pink',
                                     'spring', 'summer', 'winter']),
                 ('Diverging',      ['BrBG', 'bwr', 'coolwarm', 'PiYG', 'PRGn', 'PuOr',
                                     'RdBu', 'RdGy', 'RdYlBu', 'RdYlGn', 'Spectral',
                                     'seismic']),
                 ('Qualitative',    ['Accent', 'Dark2', 'Paired', 'Pastel1',
                                     'Pastel2', 'Set1', 'Set2', 'Set3']),
                 ('Miscellaneous',  ['gist_earth', 'terrain', 'ocean', 'gist_stern',
                                     'brg', 'CMRmap', 'cubehelix',
                                     'gnuplot', 'gnuplot2', 'gist_ncar',
                                     'nipy_spectral', 'jet', 'rainbow',
                                     'gist_rainbow', 'hsv', 'flag', 'prism'])]
    """

    h,w= img.shape[:2]
    if adapt4screensize<>None:
        d=1
        while (h/(d+1)>adapt4screensize[0]) or (w/(d+1)>adapt4screensize[1]):d+=1
        #print '~',d,h/d,w/d
        img=img[::d,::d]

    if colormap=='gray':
        if img.ndim==3:
            if img.shape[2]==3:
                plt.imshow(cv2.cvtColor(img,cv2.cv.CV_BGR2RGB))
                return
    plt.imshow(img,colormap,norm=None, aspect=None, interpolation=None, alpha=None, vmin=None, vmax=None, origin=None, extent=None, shape=None, filternorm=1, filterrad=4.0, imlim=None, resample=None, url=None, hold=None)

    if adapt4screensize<>None:
        minQlabels1=minQlabels
        tax=tickArray(w,minQlabels1)
        tay=tickArray(h,minQlabels1)
        plt.xticks(tax/d,[str(x) for x in tax],rotation=33);
        plt.yticks(tay/d,[str(x) for x in tay]);

    plt.gcf().set_size_inches(szw,szh)



def getFilenamesFromDir(d='.',regexpflt=None,regexpfltFlag=re.IGNORECASE):
    if regexpflt==None:
        return [x for x in [f for p,d,f in os.walk(d)][0]]
    else:
        return [x for x in [f for p,d,f in os.walk(d)][0] if re.search(regexpflt,x,regexpfltFlag)]


def quickPlotF(strFunctionOf_x,pltlineopt="-",xmin=-10,xmax=10,pts=50,szw=8, szh=7, cross=False, spineCross=True):
    "just quick plot some 1-variable (x) function defined as string expression and return lambda(x) with this function"
    ff=sp.lambdify('x',strFunctionOf_x)
    xx=np.linspace(xmin,xmax,pts)
    plt.plot(xx, [ ff(z) for z in (xx)] ,pltlineopt)
    mplGridSzAndCross(szw=szw, szh=szh, cross=cross, spineCross=spineCross)
    return ff