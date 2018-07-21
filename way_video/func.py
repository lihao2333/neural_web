import re
import os,time
def gen_img(content,style):
    cmd="python3 fast-neural-style-tensorflow/eval.py\
            --image_file {0} \
            --model_file fast-neural-style-tensorflow/models/{1}".format(content,style)
    os.system(cmd)
#def gen_video(content,style):
#    print("ddddddddddddddddddd")
#    print(content, style)
#    cmd="cd neural-style_diy;th main.lua\
#            -content_image {0} \
#            -style_image {1}".format(content,style)
#    print(cmd)
#    os.system(cmd)
#def gen_video2(dirname):
#    cmd="cd {0};pwd;ffmpeg -y -r 10 -i res_%04d.jpg  output.mp4; ".format(dirname)
#    os.system(cmd)
def gen_video(content,style):
    output = "{0}/res.{1}".format(os.path.dirname(content),content.split(".")[1])
    print(content, style,output)
    cmd="cd neural-style;th neural_style.lua\
            -content_image {0} \
            -style_image {1}\
            -output_image {2}\
            -print_iter 1\
            -save_iter 1\
            -image_size 512\
            -optimizer 'lbfgs'\
            -num_iterations 1000\
            -original_colors 0\
            -content_weight 8e0\
            -style_weight 5e1\
            -init 'image'\
".format(content,style,output)
    print(cmd)
    os.system(cmd)
def gen_video2(dirname):
    print("hi")
    print(dirname)
    print("hi")
    cmd="\
cd {0};pwd;ffmpeg -y -r 50 -i res_%d.jpeg  output.mp4||cd {0};pwd;ffmpeg -y -r 50 -i res_%d.jpg  output.mp4; ".format(dirname)
    os.system(cmd)
if __name__ == "__main__":
    gen_img(1,1)
