from os import mkdir
from thirdoct import third_oct
import h5py
import numpy as np
import shutil

#this file will be used to generate the test cases.

Python_test_files_dir = 'py_test_dir'
mkdir(Python_test_files_dir)

def write_test_file(file_name, A, cf):
    file_name = file_name+'.h5'
    with h5py.File(file_name, 'w') as f:
        f.create_dataset('A', data = A)
        f.create_dataset('cf', data = cf)
    source_folder = r"/home/eljam3239/repos/nistoi_thirdoct/"
    dest_folder = r"/home/eljam3239/repos/nistoi_thirdoct/py_test_dir/"
    files_to_move = [file_name]

    for file in files_to_move:
        source = source_folder+file
        destination = dest_folder+file
        shutil.move(source, destination)
    return 0


for fs in [8000, 16000, 41000]:
    for N_fft in [128, 256, 512]:
        for numBands in [8, 15]:
            for mn in [150, 440]:
                A, cf = third_oct(fs, N_fft, numBands, mn)
                file_name = 'fs_'+str(fs)+'_Nfft_'+str(N_fft)+'_numBands_'+str(numBands)+'_mn_'+str(mn)
                write_test_file(file_name, A, cf)


