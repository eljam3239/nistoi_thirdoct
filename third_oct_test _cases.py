from thirdoct import third_oct
import h5py
import numpy as np

#this file will be used to generate the test cases.

Python_test_files_dir = 'py_test_dir'

for fs in [8000, 16000, 41000]:
    for N_fft in [128, 256, 512]:
        for numBands in [8, 15]:
            for mn in [150, 440]:
                A, cf = third_oct(fs, N_fft, numBands, mn)
                file_name = 'PYTHON_fs_'+str(fs)+'_Nfft_'+str(N_fft)+'_numBands_'+str(numBands)+'_mn_'+str(mn)
                write_test_file(file_name, A, cf)

def write_test_file(file_name, A, cf):
    file_name = file_name+'.h5'
    with h5py.File(Python_test_files_dir/file_name, 'w') as f:
        f.create_dataset('A', data = A)
        f.create_dataset('cf', data = cf)

    return 0
