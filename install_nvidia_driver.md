# Readme



## 安装Nvidia驱动



### 删除旧版本



卸载驱动 如果以前没有安装过驱动则跳过这一步



以我安装的nvidia-390为例

 

如果你安装的其它版本，请自行更改尾缀数字到相应版本

 

`sudo apt-get remove --purge nvidia-331-updates`

 

如果安装的是官网下载的驱动



则重新运行run文件来卸载



`sh ./nvidia.run --uninstall`



### 新版本安装



***首先（很重要一点！）禁用自带驱动nouveau，不然安装驱动和CUDA都无法成功***

```python
#首先检查自己的nouveau驱动是否正在加载

$lsmod | grep nouveau#终端运行这个命令，如果有输出则代表nouveau正在加载，则需要执行以下命令，否则跳过这段内容

sudo vim /etc/modprobe.d/blacklist-nouveau.conf #建立一个黑名单 

#在文件内添加如下两行内容

blacklist nouveau
options nouveau modeset=0

#添加完成之后保存退出，并执行以下命令

sudo update-initramfs –u
#这个时候如果执行 lsmod | grep nouveau 命令可能还会有输出，不要紧张，这是正常现象，按照官网说法，当我们重启电脑之后自带驱动才会被禁止
```





#### 方法一（命令行操作）

```python
sudo add-apt-repository ppa:graphics-drivers/ppa 
#回车后继续 
sudo apt-get update 
sudo apt-get install nvidia-390#根据自己的显卡修改尾缀数字，具体请参考官网(http://www.nvidia.com/Download/index.aspx?lang=cn)
sudo apt-get install mesa-common-dev 
sudo apt-get install freeglut3-dev 
#之后重启系统让GTX1060显卡驱动生效 
```



#### 方法二（官网下载）

在[官网](http://www.nvidia.com/Download/index.aspx?lang=cn)中寻找合适自己显卡的驱动，下载下来（最好放在/home目录下，防止中文乱码造成的安装繁琐）



切换到tty1控制台：Ctrl+Alt+F1 



关闭`X-Window`:`sudo service lightdm stop`



执行如下命令开始安装:`sudo ./NVIDIA.run` 



安装完成后重新启动`X-Window: sudo service lightdm start`



然后`Ctrl+Alt+F7`进入图形界面



####方法三（设置中操作）



打开Linux的setting->Software & Updates->Additional Drivers可以在里面查看到自己显卡的驱动，选择合适的驱动保存，系统会自动安装驱动。



####如何检测是否安装成功

命令行执行以下任意一个命令

```
nvidia-smi #输出正确的显卡信息则安装成功   
nvidia-settings  #可以打开Nvidia显卡设置图形界面则安装成功
```





## 安装CUDA



CUDA安装是有官网的[安装手册](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)作为指导的，里面给出了详细的操作步骤，如果遇到了文中没有提到的问题，可以在手册中寻找答案



1. 验证自己的电脑是否有支持CUDA的GPU

   ````python
   lspci | grep -i nvidia #命令行下查看自己的Nvidia显卡信息
   lspci | grep -i vga #也可以用这个命令查看自己电脑上所拥有的显卡信息
   ````

   得知自己Nvidia显卡信息之后可以去[官网](https://developer.nvidia.com/cuda-gpus)查看自己的GPU是否支持CUDA

2. 验证自己的Linux版本是否支持 CUDA(Ubuntu 16.04没问题)

   ```python
   uname -m && cat /etc/*release
   ```

3. 验证系统是否安装了gcc

   ```python
   gcc –version #查看是否安装了gcc
   
   #如果没有安装则执行以下命令
   sudo apt-get  install  build-essential
   ```

4. 验证系统是否安装了kernel header和 package development

   ```python
   uname –r #查看正在运行的系统内核版本
   
   sudo apt-get install linux-headers-$(uname -r) #可以安装对应kernel版本的kernel header和package development
   ```

   

上述内容都没有问题之后可以[下载](https://developer.nvidia.com/cuda-zone)CUDA的安装文件，这里我们使用的是runfile文件进行安装





![屏幕快照 2018-07-20 14.39.36](/Users/chenyao/Desktop/屏幕快照 2018-07-20 14.39.36.png)



5. 下载完成之后可以进行MD5检验，如果需号不和，需要重新下载

   `md5sum cuda_9.2.148_396.37_linux.run`

6. 禁用nouveau

7. 进入文本模式（**Ctrl+Alt+F1**），关闭图形化界面（**sudo service lightdm stop**）

8. 切换到CUDA安装文件路径（eg. `$cd /home`）

   执行`$ sudo sh cuda_7.5.18_linux.run`

   按照提示输入相应字符，例如accept，yes

9. 如果自己的电脑是双显卡，则在被询问是否安装OpenGL时选择no，否则极有可能安装完CUDA之后，重启图形化界面后遇到登录界面循环问题：输入密码后又跳回密码输入界面。这是因为你的电脑是双显，而且用来显示的那块GPU不是NVIDIA，则OpenGL Libraries就不应该安装，否则你正在使用的那块GPU（非NVIDIA的GPU）的OpenGL Libraries会被覆盖，然后GUI就无法工作了。

   安装成功后，会在最后显示installed，否则会显示failed。

   ***如果你的电脑是双显卡，在重启之后发现无法进入图形界面，可以尝试讲显示输出换成另一个显卡***

   在命令最后提示你需要声明两个环境变量，***记住这两个变量***

10. 返回图形化界面（Alt + ctrl +F7），如果能够成功登录，则表示不会遇到循环登录的问题，基本说明CUDA的安装成功了。

    如果你遇到了重复登陆情况，不用急着重装系统，官方教程上有提及，原因上一步的注中有提及，在安装openGL时你可能不注意选择了yes，请卸载cuda,然后重装。

    ```python
    #在登陆界面状态下，按Ctrl + Alt + f1,进入TUI 执行
    
    $ sudo /usr/local/cuda-9.2/bin/uninstall_cuda_9.2.pl #请根据自己下载的文件修改
    
    $sudo /usr/bin/nvidia-uninstall 
    
    #然后重启  
    $sudo reboot 
    
    #重新安装.run   再次安装时请一定留意，在提示是否安装OpenGL时，你的是双显卡应该选则n
    ```

    

11. 重启电脑，检查Device Node Verification

    执行`$ ls /dev/nvidia*`

    如果出现了三个文件，类似于`/dev/nvidia0 /dev/nvidiactl  /dev/nvidia-uvm`（第三个文件尾缀可能不同）则证明安装成功，如果只显示了一两个文件（显示不全，可以去[官网](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#runfile-installation)查看具体解决办法。

12. 设置环境变量

    终端执行`$sudo vi /etc/profile`

    在文件末尾添加最初安装完成后要求保存记录的两行环境变量

    ```python
    #请根据自己的环境变量进行修改
    
    export PATH=/usr/local/cuda-9.0/bin${PATH:+:${PATH}}
    export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
    ```

    重启电脑，查看环境变量是否设置成功

    ```python
    $ cat /proc/driver/nvidia/version #验证驱动版本
    
    $ nvcc -V #验证CUDA Toolkit
    
    #如果显示 The program 'nvcc' is currently not installed. You can install it by typing:sudo apt-get install nvidia-cuda-toolkit 则说明环境变量没有配置成功，请重新配置
    ```

13. 编译CUDA提供的例子

    

    终端进入NVIDIA_CUDA-9.2_Samples目录

    

    `$make`

    

    编译成功会显示 Finished building CUDA samples

    

    如果出错就按照错误提示进行修改

    

    编译之后的文件在 NVIDIA_CUDA-9.2_Samples/bin 目录中

    

    进入 NVIDIA_CUDA-9.0_Samples/bin/x86_64/linux/release 目录，终端执行`$ ./deviceQuery` 看到 Result = PASS 证明安装成功

    

    最后再检查一下系统和CUDA-Capable device的连接情况 

    终端输入`$ ./bandwidthTest` 看到Result = PASS，则代表成功 
