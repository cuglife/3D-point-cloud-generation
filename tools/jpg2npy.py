import os, sys
import numpy as np
from PIL import Image

'''
Converts all images in a directory to '.npy' format.
Use np.save and np.load to save and load the images.
Use it for training your neural networks in ML/DL projects. 
'''

# Path to image directory
file_dir = sys.argv[1]
dest_dir = sys.argv[2]
datasets = os.listdir(file_dir)

for data in datasets:
    files = os.listdir(file_dir + data + "/imgs/")
    dataset = []
    for file in files:
        file_path = file_dir + data + "/imgs/" + file
        if os.path.isfile(file_path):
            im = Image.open(file_path).convert("RGB")
            im = np.array(im)
            dataset.append(im)
    img_set = np.array(dataset)
    save_file_name = dest_dir + data + ".npy"
    np.save(save_file_name, img_set)
