import re
import os,time
def gen_img(content,style):
    cmd="python3 fast-neural-style-tensorflow/eval.py\
            --image_file {0} \
            --model_file fast-neural-style-tensorflow/models/{1}".format(content,style)
    os.system(cmd)
def gen_video(content,style):
    print("ddddddddddddddddddd")
    print(content, style)
    cmd="cd neural-style_diy;th main.lua\
            -content_image {0} \
            -style_image {1}".format(content,style)
    print(cmd)
    os.system(cmd)
def gen_video2(dirname):
    cmd="cd {0};pwd;ffmpeg -y -r 10 -i res_%04d.png  output.mp4; ".format(dirname)
    os.system(cmd)
if __name__ == "__main__":
    gen_img(1,1)
