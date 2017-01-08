## bpmMeter ##

show FFT of waveform envelope to view BPM of wav  (used 1st 60sec fragment by default)

### require ###

ffmpeg.exe in PATH

python 2.7

python modules:
numpy,scipy,matplotlib,ffmpy, and some other common used...


### How to use: ###
```
calcbitswav.py [-h] [-s] [--nosavepic] [-f SFREQSRC] [-w WINDOW_SEC] fln

positional arguments:
  fln                   filename (wav or mp3 or any known by ffmpeg)

optional arguments:
  -h, --help            show this help message and exit
  -s, --silent          don't show pic. only save it
  --nosavepic           don't save pic. only show if not -s
  -f SFREQSRC, --sfreq SFREQSRC
                        use sample freq to process (def 8000)
  -w WINDOW_SEC, --window_sec WINDOW_SEC
                        sec to process (starting from 1) def = 60. note: file
                        must have at least window_sec+5 sec length
```
*then look bpm in 1st peaks of fft plot *

### _____________ ###
(c) master_Nemo 2016 All right reserved