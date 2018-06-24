from django.http import HttpResponseRedirect  
from django.http import HttpResponse

def redirect_mode_sel(request):  
    #表单处理OR逻辑处理  
    return HttpResponseRedirect('/mode_sel')  #跳转到主界面  
#    return HttpResponse("hiii")
