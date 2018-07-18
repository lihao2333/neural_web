## 这是什么?
这是一个django网站框架,通过用户上传内容图片和风格图片就可以返回内容风格合成的图片或者一个从原始图片到目标图片渐变的视频
## 需要环境
* tmux
* tmuxinator
* docker 并且把当前用户加到docker组中
## 需要文件
需要的数据和模型建议按照如下方式存放
```
/Dataset
	style_transfer---精选样本
	train2014----用于训练风格模型
/Model
	styles--风格模型
	vgg16
		vgg16.ckpt----用于训练风格模型
	vgg19
		VGG_ILSVRC_19_layers.caffemodel
		VGG_ILSVRC_19_layers_deploy.prototxt
		vgg_normalised.caffemodel
```

项目本身预置的软连接关系如下:

```
$Proj/fast-neural-style-tensorflow/models --> /Model/styles
$Proj/fast-neural-style-tensorflow/train2014 --> /Dataset/train2014
$Proj/neural-style_diy/model--> /Model/vgg19
$Proj/media/img_list_all --> /Dataset/style_transfer
```

## docker镜像
该项目需要的docker镜像托管在dockerhub中,通过`docker pull lihao2333/intel:v4`来下载
或者拥有我们制作的镜像文件`intel:v4.tar`通过执行`docker load<intel:v4.tar`来还原镜像

## 如何使用
#### 安装

* 递归克隆项目

```
git clone --recurse-submodules git@github.com:lihao2333/neural_web.git
cd neural_web
```
* 配置`tmuxinator`
	* for ubuntu:16.04
	```
	apt-get install tmux
	apt-get install tmuxinator
	mkdir ~/.tmuxinator
        ln -sf `pwd`/neural_web.yml ~/.tmuxinator/ 
	```
	* for mac
	```
	brew install tmux
	brew install tmuxinator
	mkdir ~/.config/tmuxinator
        ln -sf `pwd`/neural_web.yml ~/.config/tmuxinator/ 	
	```
	* 最后记得在`~/.bashrc`中添加
	```
	export EDITOR="vim"
	alias mux="tmuxinator"
	```
        * 然后执行
	```
	source ~/.bashrc
	mux list
	```
	* 如果出现`neural_web`则说明安装成功
#### 运行
* 执行`mux start neural_web`,会自动打开一个tmux的session, 同时里面会自动运行docker
* 登录`<your ip address>:8000`既可

#### 最终效果
* 查看视频
![avatar](readme/video_gallery.png)
* 创建图片
![avatar](readme/create_image.png)
* 查看图片
![avatar](readme/image_gallery.png)
* 查看精选图片
![avatar](readme/image_gallery_all.png)
