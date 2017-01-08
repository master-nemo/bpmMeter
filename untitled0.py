# -*- coding: utf-8 -*-
"""
Created on %(date)s


@author: %(username)s
"""
# In[]:
#from _NEMOpy.importCalculator import *

# In[]:
import numpy as np
from numpy import *
#%%
#%%
#%%

#==============================================================================
# def processArgs(verose=False): 
#     aparser = argparse.ArgumentParser(description='descript')
#     aparser.add_argument("-s","--silent",action='store_true',dest="slnt",default=False, help="don't show pic. only save it")
#     aparser.add_argument("--nosavepic",action='store_true',dest="nosavepic",default=False, help="don't save pic. only show if not -s")
#     aparser.add_argument("-f","--sfreq",dest="sfreqsrc", type=int ,default=8000 , help='use sample freq to process (def 8000)')
#     aparser.add_argument("-w","--window_sec",dest="window_sec", type=int, default=60, help='sec to process (starting from 1) def =  60. note: file must have at least window_sec+5 sec length') 
#     
#     if npy.isRunFromIDE():
#         aparser.add_argument('fln', nargs="?",  help='filename')   #debug only use def 4wrk
#     else:
#         aparser.add_argument('fln',             help='filename')
#     
#     #%%%
#     if npy.isRunFromIDE():
#         args = aparser.parse_args(['Testfile2.mp3 '])
#     else:
#         args = aparser.parse_args()
#     if verose: print args
#     
#     return args
# 
# args=processArgs()
# # globals().update(vars(processArgs()))
# # globals().update(vars(aparser.parse_args()))
#==============================================================================
import time
import os
import sys
#%%%
fln="Testfile2.mp3 "
#%%%
timetup = time.gmtime()
time.strftime('%Y%m%dT%H%M%SZ', timetup)


os.path.abspath(fln)+".report."+time.strftime('%Y%m%dT%H%M%SZ', timetup)+".png"

#%%%



#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%

if __name__=='__main__':
    pass


