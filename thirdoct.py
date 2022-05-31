import numpy as np
import math
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
    k = np.mgrid[0:numBands-1]
    cf = np.power(2, k/3*mn)
    #sqrt of a dot product I beleive
    fl = math.sqrt(np.dot(np.power(2, k/3*mn), np.power(2, (k-1)/3*mn)))
    fr = math.sqrt(np.dot(np.power(2, k/3*mn), np.power(2, (k+1)/3*mn)))

    #this might need to be like m(f.shape) -- we want the size of this largest dimension?
    A = np.zeros(numBands, f.max())

    #length(cf) in python?
    for i in range(1, cf.max):



