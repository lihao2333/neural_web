from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from .models import gallaryVideo
from .forms import gallaryVideoForm
from . import func
import os,re

# Create your views here.
def index(request):
    return HttpResponse("way_img ixndex")
def gen_video(request):
    if request.method == 'POST':
        form = gallaryVideoForm(request.POST, request.FILES)
        if form.is_valid():
            if 'content' in request.FILES\
                    and 'style' in request.FILES:
                content = request.FILES['content']
                style = request.FILES['style']
                s = gallaryVideo(owner=request.user, content=content,style=style)
                s.save()
                func.gen_video(s.content.path,s.style.path)
                return HttpResponseRedirect("list_video")
        else :
                return render(request, "info.html",{"info":"choose content image first"})

    else :
        return render(request,"way_video/gen_video.html",{})

def list_video(request):
    model = gallaryVideo.objects.get(owner=request.user) 
    dirname = os.path.dirname(model.content.path)
    current = os.popen(
    '''
    cd {0};ls res_*|sort -r|head -1
    '''.format(dirname)
            ).readline()
    total_num=49
    content = {"content_url":model.content.url,
               "style_url":model.style.url,
               "video_url":os.path.dirname(model.content.url)+"/output.mp4",
                "total_num":total_num,
                }
    try :
        current_num= int(re.match(r"res_(.*)\..*",current).group(1))
        content["current_num"]  = current_num
        content["res_url"] =model.content.url.replace("content","res_%04d"%(current_num))
        func.gen_video2(dirname)
    except :
        content["current_num"] =0
        content["res_url"] =model.content.url

    return render(request, "way_video/list_video.html",content)
