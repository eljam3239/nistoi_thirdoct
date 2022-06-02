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
    #print(f)
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
    #fl = math.sqrt(np.dot((2**(k/3)*mn),(2**((k-1)/3)*mn))) --> outputs 2227.4722913822884
    #fl = np.sqrt((2**(k/3)*mn)@(2**((k-1)/3)*mn))
    #fl = np.sqrt(np.multiply(np.power(2, k/3)*mn), np.power(2, ((k-1)/3)*mn))
    fl = np.sqrt(np.multiply(np.power(2, k/3)*mn, np.power(2, (k-1)/3)*mn))
    #print(fl)
    #fr              = sqrt((2.^(k/3)*mn).*2.^((k+1)/3)*mn);
    fr = np.sqrt(np.multiply(np.power(2, k/3)*mn, np.power(2, (k+1)/3)*mn))
    #A               = zeros(numBands, length(f));
    A = np.zeros((numBands, max(f.shape)))
    #print(A)

    for i in range(0, max(cf.shape)):
        a= min((f-fl[i])**2)
        b = np.argmin((f-fl[i])**2, axis =0)
        fl[i] = f[b]
        fl_ii = b

        a= min((f-fr[i])**2)
        b = np.argmin((f-fr[i])**2, axis =0)
        fr[i] = f[b]
        fr_ii = b
        #A(i,fl_ii:(fr_ii-1))	= 1;
        A[i, fl_ii:(fr_ii-1)]=1
        #print(A)
    rnk = np.sum(A,1)
    
    numBands = np.where(np.logical_and((rnk[1:] - rnk[0:-1])>=0, rnk[1:] != 0))[0][-1]+1
    #print(numBands)
    A = A[0:numBands+1, :]
    cf = cf[0:numBands+1]
    
third_oct(fs, N_fft, numBands, mn)