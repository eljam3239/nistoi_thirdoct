
import os
import h5py
import numpy as np

from thirdoct import third_oct

def read_test_file(test_file):
    with h5py.File(test_file, "r") as f:
        data = f['/data']
        A  = np.transpose(data['A'][()])
        cf = np.transpose(data['cf'][()])
    return A, cf

#A, cf = read_test_file('PYTHON_fs_8000_Nfft_256_numBands_12_mn_120.h5')

def compare(X, Y):
    return np.amax(np.absolute(np.subtract(X, Y)))
"""
def compare(fileP, fileM):
    A_py, cf_py = read_test_file(fileP)
    A_m, cf_m = read_test_file(fileM)
    A_diff = np.linalg.det(np.subtract(A_py, A_m))
    c_diff = np.linalg.det(np.subtract(cf_py, cf_m))

    return A_diff, c_diff
"""
#det of diff between python and matlab files


py_folder = '/home/eljam3239/repos/nistoi_thirdoct/py_test_dir'
m_folder = '/home/eljam3239/repos/nistoi_thirdoct/test_files'

for fs in [8000, 16000, 41000]:
    for N_fft in [128, 256, 512]:
        for numBands in [8, 15]:
            for mn in [150, 440]:
                file_name = 'fs_' + str(fs) + '_Nfft_' + str(N_fft) + '_numBands_' + str(numBands) + '_mn_' + str(mn)+'.h5'
                A_m, cf_m = read_test_file(os.path.join(m_folder, file_name+'.h5'))
                A_py, cf_py = third_oct(fs, N_fft, numBands, mn)
                
                if compare(A_py, A_m)>1e-10:
                    print('ERROR in computing A: '+file_name)
                elif compare(cf_py, cf_m)>1e-10:
                    print("ERROR in computing cf: "+file_name)
                else:
                    print("Nice job")
                