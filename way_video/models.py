from django.db import models
from django.contrib.auth.models import User
from time import gmtime, strftime
import re
# Create your models here.
def content_file_name(instance, filename):
    return "way-video/{0}/{1}/{2}".format(instance.owner.username,strftime("%Y-%m-%d-%H-%M-%S",gmtime()),re.sub(".*\.","content.",filename))
def style_file_name(instance, filename):
    return "way-video/{0}/{1}/{2}".format(instance.owner.username,strftime("%Y-%m-%d-%H-%M-%S",gmtime()),re.sub(".*\.","style.",filename))
class gallaryVideo(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="video_owner",primary_key=True)
    content = models.ImageField(upload_to=content_file_name, blank=True, null=True)
    style = models.ImageField(upload_to=style_file_name, blank=True, null=True)
#    res = models.ImageField(upload_to='way_img/',blank=True, null=True)
    def __unicode__(self):
        return'%s %s'%(self.owner,self.content)

