import os
import h5py
import numpy as np

def read_test_file(test_file):
    with h5py.File(test_file, "r") as f:
        data = f['/data']
        A  = np.transpose(data['A'][()])
        cf = np.transpose(data['cf'][()])
    return A, cf

A, cf = read_test_file('fs_8000_Nfft_256_numBands_12_mn_120.h5')

print(A)
print(cf)