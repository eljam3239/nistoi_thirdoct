from thirdoct import third_oct
import h5py
import numpy as np

for fs in [8000, 16000, 41000]:
    for N_fft in [128, 256, 512]:
        for numBands in [2, 8, 16]:
            for mn in [150, 440]:
                A, cf = third_oct(fs, N_fft, numBands, mn)
                file_name = 'PYTHON_fs_'+str(fs)+'_Nfft_'+str(N_fft)+'_numBands_'+str(numBands)+'_mn_'+str(mn)+'.h5'
                hf = h5py.File('file_name', 'w')
                hf.create_dataset('A', data = A)
                hf.create_dataset('cf', data = cf)
                hf.close()