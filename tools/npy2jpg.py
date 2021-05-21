import numpy as np
from PIL import Image
import os

# .npy files trans to jpg

file_list = "02691156_test.list"
# file_dir = "C:/Users/az/Desktop/02691156_inputRGB/"
file_dir = "D:/repos/AAAI/02691156/02691156_inputRGB/"
dest_dir = "C:/Users/az/Desktop/img/"

get_file_in_list = True

if get_file_in_list:
    files = []
    with open(file_list) as list_file:
        for line in list_file:
            # files.append(line.strip() + ".npy")
            files.append(line.strip().split("/")[1] + ".npy")
else:  # get files from folder
    files = os.listdir(file_dir)

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

for f in files:
    img_path = dest_dir + f[:-4] + "/"
    if not os.path.isdir(img_path):
        os.mkdir(img_path)
    file = file_dir + f
    arrays = np.load(file)
    for i in range(arrays.shape[0]):
        arr = arrays[i, :, :, :]
        img = Image.fromarray(arr, 'RGB')
        img_name = str(i + 1) + ".jpg"
        img.save(img_path + img_name)
