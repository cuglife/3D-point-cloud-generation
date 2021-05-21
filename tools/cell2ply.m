%% 获取文件
clc;clear;
% file_folder=fullfile('D:/repos/CV/3D-point-cloud-generation/orig-ft_it100000/');
% file_folder=fullfile('C:/Users/az/Desktop/orig-ft_it100000_airplane/');
file_folder=fullfile('D:/Downloads/orig-ft_it100000/');
files={dir(fullfile(file_folder,'*.mat')).name};
%% 读取数据 保存为点云

for i = 1:length(files)
    file_name = files{i};
    file = strcat(file_folder,file_name);
    split_file_name=strsplit(file_name,'.');
    ply_path=strcat("C:/Users/az/Desktop/ply/",split_file_name{1});
    if exist(ply_path)==0   %该文件夹不存在，则直接创建
        mkdir(ply_path);
    end
    
    
    load(file);
    for j = 1:length(pointcloud)
       points = pointcloud{j};
       ptCloud=pointCloud(points);
       ply_file_name = strcat("C:/Users/az/Desktop/ply/",split_file_name{1},"/",num2str(j),".ply");
       pcwrite(ptCloud,ply_file_name);
    end
end



