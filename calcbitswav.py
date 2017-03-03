# -*- coding: utf-8 -*-
"""
show FFT of envelope to view BPMs of wav  (used 1st 20sec fragment)

@author: master_Nemo
"""
    
#from _NEMOpy.importCalculator import *
import nemopy_misc as npy #lite version
from matplotlib import pyplot as plt
#from scipy import *    
from scipy.io import wavfile
import scipy
from  scipy import ndimage
import numpy as np
from numpy import *
import argparse 

import tempfile
import ffmpy
import os
import sys
import time
#%%

def processArgs(verose=False): 
    aparser = argparse.ArgumentParser(description='show FFT of waveform envelope to view BPMs of wav  (used 1st 60sec fragment by default)')
    aparser.add_argument("-s","--silent",action='store_true',dest="slnt",default=False, help="don't show pic. only save it")
    aparser.add_argument("--nosavepic",action='store_true',dest="nosavepic",default=False, help="don't save pic. only show if not -s")
    aparser.add_argument("-f","--sfreq",dest="sfreqsrc", type=int ,default=8000 , help='use sample freq to process (def 8000)')
    aparser.add_argument("-w","--window_sec",dest="window_sec", type=int, default=60, help='sec to process (starting from 1) def =  60. note: file must have at least window_sec+5 sec length') 
    
    if npy.isRunFromIDE():
        aparser.add_argument('fln', nargs="?",  help='filename (wav or mp3 or any known by ffmpeg)')   #debug only use def 4wrk
    else:
        aparser.add_argument('fln',             help='filename (wav or mp3 or any known by ffmpeg)')
    
    
    if npy.isRunFromIDE():
        args = aparser.parse_args(['Testfile2.mp3 '])
    else:
        args = aparser.parse_args()
    if verose: print args
    
    return args


#%%%
def convertInfile_And_Read2array(fln,sfreqsrc=8000,window_sec=60):
    try:
        tempFileH,tempFileName=tempfile.mkstemp(".wav")
        print "use mmpeg to convert to wav (to temp file)"
        ffmpy.FFmpeg(global_options='-y',
                     inputs={args.fln:''},
                     outputs={tempFileName:'-ar %d -to %d -f wav' % (sfreqsrc,window_sec+5) }
                     #outputs={tempFileName:'-ar 8000  -to 65 -f wav'}
                     ).run()
        
    #    w1f=wavfile.read(tempFileName);
    #    w1=w1f[1]
        w1=wavfile.read(tempFileName)[1];
        return w1
    finally:
        os.close(tempFileH)
        os.remove(tempFileName)
        print tempFileName,os.path.exists(tempFileName)
       
#%%

def getFragmentByTime(w,sf,
                mintview=1, #sec
                maxtview=61):
    return w[mintview*sf:sf*maxtview]


#%%

#fmax2view=5 #Hz
def ShowFFTFragmentTo(maxHz=5,dxtick=0.2):
    #minHz=0.2
    minHz=10./60
    
    ff=df*arange(Nf)
    
    fmax2view=maxHz #Hz
    nv=1+int(fmax2view/df)
    dxt=dxtick
    
    #xxf=arange(round(ceil(fmax2view*10)/dxt/10   ))*dxt
    #xxf=arange(round(1+round(fmax2view*10)/ (dxt*10)   ))*dxt
    xxf=np.arange(minHz,maxHz,dxt)
    
    print 'show 1st {0} points up to {1:.5} with freq resolution {2:.5} [Hz]'.format(nv, ff[nv], df)
    #print 'show 1st %d points up to %.5f with freq resolution %.5f [Hz]' % (nv, ff[nv], df)
    #nolof=5
    #nolof=8
    nolof=minHz/df
    nolof=int(nolof)
    npy.mplssz(11,7)
    #npy.mplssz(11,7)
    plt.plot(ff[nolof:nv],f1a[nolof:nv],"*-g")
    #npy.mplssz(11,7)
    npy.mplGridSzAndCross(11,7,cross=False)
    plt.box(True)
    plt.title("fft of envelope (1st %.2f Hz) w/o 0Hz   (df=%.5fHz ~%.2f bpm)" %(fmax2view,df,df*60))
    plt.ylabel("abs(fft) ")
    ##plt.xlabel("frequency Hz")
    ##plt.xticks(arange(round(round(fmax2view)/dyt))*dyt)
    
    #plt.xticks(yyf,map(str,yyf*60))
    #plt.xticks(xxf,map(str,xxf*60))
    ##plt.xticks(xxf,xxf*60)
    plt.xticks(xxf,xxf*60)
    plt.xlim((xxf[0],xxf[-1]))
    #plt.xticks(xxf)#,map(str,yyf*60))
    plt.xlabel("bpm")
    #print  xxf,xxf*60
    #print  xxf*60
    #plt.show()

def reportFileName(fln):
    #timetup = time.gmtime()
    return  os.path.abspath(fln)+".report."+time.strftime('%Y%m%dT%H%M%SZ', time.localtime())+".png"

#%%
#%%
#%%
#%%
#%%
#==============================================================================
#==============================================================================
#==============================================================================

if __name__=='__main__':
    args=processArgs()
    w1=convertInfile_And_Read2array(args.fln,args.sfreqsrc,args.window_sec);        
    #%%
    w1l=(np.float_(w1[:,0])+np.float_(w1[:,0]))*0.5     #use nean of 2 ch    #w1l=w1[:,0] #use 1 channel
    #%%
    sf=args.sfreqsrc    #Fs=8000 #Hz ## sample frequency
    Nt=len(w1l)
    #%%
    w1t= getFragmentByTime(w1l,sf, 1, 1+args.window_sec)
    print "%d points of %d so used ~%.2f%% of file"%(len(w1t),Nt,(100.0*len(w1t)/Nt))
    #%%
    print "now calc envelope .... wait please...."
    w1e=abs(np.float_(w1t))
    w1ef=scipy.ndimage.gaussian_filter1d(w1e,(sf/200))*2  # @UndefinedVariable
    #%%
    Nef=len(w1ef)
    #%%
    print "and fft. wait please...."
    f1=np.fft.fft(w1ef)
    f1a=abs(f1)
    #%%
    Nf=len(f1)
    df=1.0*sf/Nf
    print "Nf,df",Nf,df
    #%%
    # ff=df*arange(Nf)    #arguments 
    #%%
    print "srv len=%d " %(len(w1),)
    print "env len=%d " %(len(w1ef),)
    print "fft len=%d and df=%f" %(Nf,df)
    #%%
    
    ## ===plot result===
    
    plt.subplot(311)
    
    maxtview=3
    plt.plot(w1t[:sf*maxtview])
    plt.plot(w1ef[:sf*maxtview],'r')
    plt.title("waveform %.2f sec"%maxtview)
    
    plt.subplot(312)
    ShowFFTFragmentTo(5,(10./60))

    #%%
    plt.subplot(313)
    ShowFFTFragmentTo(2,(5./60))
    #%%
    
    fig=plt.gcf()
    
    s_name=args.fln
    npy.mplRc_RusViaFonts()
    s_name=s_name.decode('1251',"ignore")#.encode('cp1251')
    fig.suptitle(s_name, fontsize=12)
    
    
    npy.mplssz(16,10)
    
    plt.subplots_adjust(left=0.05, right=0.98, top=0.93, bottom=0.05)

    #%%
    mng = plt.get_current_fig_manager()
    mng.set_window_title('report for:'+s_name)
    mng.resize(1024,768)
    #mng.full_screen_toggle()
    
    #%%

    if not args.nosavepic: fig.savefig(reportFileName(args.fln))     #plt.savefig(time.strftime('%Y%m%dT%H%M%SZ', timetup)+".png")
    if not args.slnt:      plt.show()
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    