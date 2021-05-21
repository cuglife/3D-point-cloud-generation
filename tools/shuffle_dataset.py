import os
import numpy

file_dir  = "D:/repos/AAAI/02691156/02691156"  # Path to folder directory
file_list = "02691156a.list"
save_path = "C:/Users/az/Desktop/"
prefix = "02691156"
rate = 0.2

get_file_in_list = True

if get_file_in_list:
    datasets = []
    with open(file_list) as list_file:
        for line in list_file:
            datasets.append(line.strip())
else:  # get files from folder
    datasets = os.listdir(file_dir)

# shuffle
numpy.random.shuffle(datasets)

index = int(len(datasets) * rate)
train = datasets[index:]
test = datasets[:index]

train_file = save_path + prefix + "_train.list"
file1 = open(train_file, 'w', encoding='utf-8')
for t in train:
    file1.write(prefix + "/" + t + '\n')
file1.close()

test_file = save_path + prefix + "_test.list"
file2 = open(test_file, 'w', encoding='utf-8')
for t in test:
    file2.write(prefix + "/" + t + '\n')
file2.close()
