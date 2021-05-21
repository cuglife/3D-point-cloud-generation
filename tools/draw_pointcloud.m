%% 绘制点云


points = cell2mat(pointcloud);
% points = F;

% points = Vd;

x=points(:,1);
y=points(:,2);
z=points(:,3);
% plot3(x,y,z,'.','MarkerSize',3);
% rotate3d

figure(1)
pc_tmp(:,1) = x;     %调整点云的方位的和xyz轴
pc_tmp(:,2) = y;
pc_tmp(:,3) = z;
pcshow(pc_tmp)