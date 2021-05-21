import os

# Path to folder directory
# path = "D:/Downloads/Compressed/all_viewdata.tar/all_viewdata/shapenetcore_viewdata/02958343/"
# path = "C:/Users/az/Desktop/02691156/"
path = "D:/repos/AAAI/02691156/02691156"

# prefix = "02691156/"
prefix = ""
datasets = os.listdir(path)

save_file = "C:/Users/az/Desktop/02691156.list"
file = open(save_file, 'w', encoding='utf-8')
for line in datasets:
    file.write(prefix + line + '\n')
file.close()
