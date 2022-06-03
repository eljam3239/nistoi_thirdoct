import os
import h5py
import shutil

junk_dir = 'junk'
#mkdir(junk_dir)

file_name = 'test.h5'
#src_path = r""
with h5py.File(file_name, 'w') as f:
    f.create_dataset('A', data = 5)

source_folder = r"/home/eljam3239/repos/nistoi_thirdoct/"
dest_folder = r"/home/eljam3239/repos/nistoi_thirdoct/junk/"
file_to_move = [file_name]

for file in file_to_move:
    source = source_folder+file
    destination = dest_folder+file
    shutil.move(source, destination)
    

"""
f_path = r"/home/eljam3239/repos/nistoi_thirdoct/"
dest_folder = r"/home/eljam3239/repos/nistoi_thirdoct/junk/"

for file_name in os.listdir(f_path):
    source = f_path+file_name
    destination = dest_folder+file_name
    if os.path.isfile(source)
"""
