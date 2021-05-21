[https://github.com/chenhsuanlin/3D-point-cloud-generation](https://github.com/chenhsuanlin/3D-point-cloud-generation) 程序执行指北
## 渲染数据


### Rendering depth image


#### Blender 运行环境准备


Blender 自带有 Python 环境，所以需要在 Blender 的Python 环境中安装需要的第三方包


- 安装方式：
   - 使用 Blender 的 Python 解释器  执行如下代码获取解释器版本与路径：
```python
blender  --python-console		# 运行 Blender Python 解释器

import sys
print(sys.path)
# output 可以得知 Python 解释器的版本与路径
# ['/usr/share/blender/scripts/addons', '/usr/share/blender/scripts/startup', '/usr/share/blender/scripts/modules', '/env/python', '/usr/lib/python36.zip', '/usr/lib/python3.6', '/usr/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6/dist-packages', '/usr/lib/python3/dist-packages', '/usr/share/blender/scripts/freestyle/modules', '/usr/share/blender/scripts/addons/modules', '/root/.config/blender/2.79/scripts/addons/modules']
```

   - 安装 pip & 使用 pip 安装需要的包
```python
# 安装 pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py   # 下载安装脚本
python3.6 get-pip.py    								  # 运行安装脚本
python3.6 -m pip install numpy scipy		# package 安装
```


#### 运行代码


```bash
# ./run.sh 02691156 8
# blender blank.blend -b -noaudio -P render.py -- [存放路径]  [文件夹名] [文件列表] 128 8
blender blank.blend -b -noaudio -P render_fixed.py -- ../  02691156 02691156.list 128 8
blender blank.blend -b -noaudio -P render.py -- ../  02691156 02691156.list 128
```


参数说明：


- -b(--background) 后台运行，用于无界面渲染
- -noaudio 禁用声音系统 部分无声卡的服务器运行会出现错误
- -P(--python) 运行指定的脚本文件



### Convert to .mat


#### 运行环境准备


```bash
# openexr C++ 库 安装
sudo apt install libopenexr-dev
# py2 环境创建
conda create -n py2gtx python=2.7
conda activate py2gtx
pip install numpy scipy
easy_install -U openexr  	# openexr Python 包 安装
```


#### 运行代码


```bash
python2 convertEXR.py 02691156 02691156.list 128 8
# python2 convertEXR.py [数据集文件夹名] [文件列表] 128 8
```


### Creating densified point


```bash
conda activate py36gtx
python3 densify.py ../ 02691156 02691156.list
# python3 densify.py [存放路径]  [文件夹名] [文件列表]
```


### Convert .jpg to .npy


可通过咱写的 tools 代码中的 jpg2npy.py 进行转换，亦可自行编写或修改


```bash
# 运行格式 
# python .\jpg2npy.py [数据集路径] [转换文件存放路径]
python .\jpg2npy.py  D:/repos/AAAI/02691156/  D:/repos/AAAI/npy/

# 适用于路径格式为：
# ├── 02691156
# │	  ├───xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# │   │   │  └─imgs
# │   │   │    └─xxx.jpg ...
```


### 数据划分


可通过咱写的 tools 代码中的 shuffle_dataset.py 进行数据划分，亦可根据实际情况修改或自行编写


### 修改：


`options.py` 中 原数据集类别修改为现数据集类别


## 程序运行


### Conda 环境配置


```python
conda create -n py36gtx python=3.6
conda activate py36gtx
pip3 install jupyter notebook
jupyter notebook
```


### 运行


具体可参考：`3D_point_cloud_generation.ipynb` ，不再赘述
