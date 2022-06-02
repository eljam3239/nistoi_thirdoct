import numpy as np
import math
from scipy import io, integrate, linalg, signal
from scipy.sparse.linalg import eigs
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

fs       = 8000
N_fft    = 256
numBands = 12
mn       = 120



def third_oct(fs, N_fft, numBands, mn):
    f = np.linspace(0, fs, N_fft+1)
    #print(f.shape)
    #f               = f(1:(N_fft/2+1));
    f = f[:N_fft//2+1]
    #print("\n", f, f.shape)
    #k               = 0:(numBands-1); --> generating an array
    k = np.arange(0, numBands)
    #print(k)
    #cf              = 2.^(k/3)*mn;
    cf = 2**(k/3)*mn
    #print(cf)
    #fl              = sqrt((2.^(k/3)*mn).*2.^((k-1)/3)*mn);
    fl = math.sqrt(np.dot((2**(k/3)*mn),(2**((k-1)/3)*mn)))
    #print(fl)
    #fr              = sqrt((2.^(k/3)*mn).*2.^((k+1)/3)*mn);
    fr = math.sqrt(np.dot((2**(k/3)*mn),(2**((k+1)/3)*mn)))
    #A               = zeros(numBands, length(f));
    A = np.zeros((numBands, max(f.shape)))
    print(A)
    """
    k = np.mgrid[0:numBands-1]
    cf = np.power(2, k/3*mn)
    #sqrt of a dot product I beleive
    fl = math.sqrt(np.dot(np.power(2, k/3*mn), np.power(2, (k-1)/3*mn)))
    fr = math.sqrt(np.dot(np.power(2, k/3*mn), np.power(2, (k+1)/3*mn)))

    #this might need to be like m(f.shape) -- we want the size of this largest dimension?
    A = np.zeros(numBands, f.max())

    #length(cf) in python?
    for i in range(1, cf.max):
        a = min(np.power(2, f-fl[i]))
        b = f.index(a)
        fl[i]=f[b]
        fl_ii = b

        a = min(np.power(2, f-fr[i]))
        b = f.index(a)
        fr[i] = f[b]
        fr_ii = b
        #defs wrong
        A[i, fl_ii:(fr_ii-1)] = 1

    rnk = np.sum(A, 2)
    #last?
    numBands = np.where()
    A = np.linspace[1:A:numBands]
    cf = np.linspace[1:cf:numBands]
    """
    return 0

third_oct(fs, N_fft, numBands, mn)