import numpy as np
"""
Computes third octave band matrix inptuts
Inputs: 
    FS: samplerate
    N_fft: FFT size
    numBands: number of bands
    mn: center frequency of first 1/3 octave band
Outputs: 
    A: octave band matrix
    CF: center frequencies
"""
def third_oct(fs, N_fft, numBands, mn):
    #is FS stop or is N_fft+1 stop?
    f = np.linspace(0, fs, N_fft+1)
    #f*1:n is the same as 1:f:n, right?
    f =np.mgrid[1: f:(N_fft/2)+1]


