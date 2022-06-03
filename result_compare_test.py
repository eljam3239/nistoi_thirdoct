import os
import h5py
import numpy as np

def read_test_file(test_file):
    with h5py.File(test_file, "r") as f:
        data = f['/data']
        A  = np.transpose(data['A'][()])
        cf = np.transpose(data['cf'][()])
    return A, cf

#A, cf = read_test_file('PYTHON_fs_8000_Nfft_256_numBands_12_mn_120.h5')

#det of diff between python and matlab files
def compare(fileP, fileM):
    A_py, cf_py = read_test_file(fileP)
    A_m, cf_m = read_test_file(fileM)
    A_diff = np.linalg.det(np.subtract(A_py, A_m))
    c_diff = np.linalg.det(np.subtract(cf_py, cf_m))

    return A_diff, c_diff

py_folder = '/home/eljam3239/repos/nistoi_thirdoct/py_test_dir'
m_folder = '/home/eljam3239/repos/nistoi_thirdoct/test_files'

for file in 