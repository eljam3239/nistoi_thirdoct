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


fs, N_fft, numBands, mn = 8000, 256, 12, 120

file_name = 'PYTHON_fs_'+str(fs)+'_Nfft_'+str(N_fft)+'_numBands_'+str(numBands)+'_mn_'+str(mn)+'.h5'
#print(file_name)
hf = h5py.File(file_name, 'w')
hf.create_dataset('A', data = A)
hf.create_dataset('cf', data = cf)
hf.close()