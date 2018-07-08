from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from .models import gallaryImg
from .forms import gallaryImgForm
from . import func
import os ,re

# Create your views here.
def index(request):
    return render(request, "info.html",{"info":"way_img index"})
def gen_img(request):
    if request.method == 'POST':
        form = gallaryImgForm(request.POST, request.FILES)
        if form.is_valid():
            if 'content' in request.FILES:
                content = request.FILES['content']
                style = request.POST['style']
                s = gallaryImg(owner=request.user, content=content,style=style)
                s.save()
                func.gen_img(s.content.path,s.style)
                return HttpResponseRedirect("list_img")
        else :
                return render(request, "info.html",{"info":"choose content image first"})

    else :
        print(settings.WAY_IMAGE_ROOT)
        style_list = os.listdir(os.path.join(settings.WAY_IMAGE_ROOT,"models"))
        print(style_list)
        return render(request,"way_img/gen_img.html",{"style_list":style_list})
def list_img(request):
    model = gallaryImg.objects.get(owner=request.user) 
    print(model.style)
    content = {"content_url":model.content.url,
                "style_url":settings.MEDIA_URL+"img/%s"%model.style.replace("ckpt-done","jpg"),
                "res_url":model.content.url.replace('content','res')}
    return render(request,"way_img/list_img.html",content)
def list_img_all(request):
    gallery = []
    basedir = settings.MEDIA_URL+"list_img_all"
    for img in sorted(os.listdir(os.path.join(settings.MEDIA_ROOT, "list_img_all"))):
        res = re.search(r'res(.+?)_(.+?).jpg',img)
        if res : 
            index = res.group(1)
            style = res.group(2)
            gallery.append({
                "content":"{0}/content{1}.jpg".format(basedir,index),
                "style":"{0}/{1}.jpg".format(basedir,style),
                "res":"{0}/{1}".format(basedir,img)
                })
    content = {"gallery":gallery}
    return render(request,"way_img/list_img_all.html",content)
