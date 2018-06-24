from django.db import models
from django.contrib.auth.models import User
from time import gmtime, strftime
import re
# Create your models here.
def content_file_name(instance, filename):
    return "way-img/{0}/{1}/{2}".format(instance.owner.username,strftime("%Y-%m-%d-%H-%M-%S",gmtime()),re.sub(".*\.","content.",filename))
class gallaryImg(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="owner",primary_key=True)
    content = models.ImageField(upload_to=content_file_name, blank=True, null=True)
    style = models.CharField(max_length=20)
#    res = models.ImageField(upload_to='way_img/',blank=True, null=True)
    def __unicode__(self):
        return'%s %s'%(self.owner,self.content)

