from django.db import models

# Create your models here.

class myServerMap(models.Model):
    hostName = models.CharField(max_length = 30)
    IPAddress = models.GenericIPAddressField()
    hostUrl = models.URLField()
    hostPort = models.IntegerField()
    createTime = models.DateTimeField(auto_now_add = True)
    
    class Meta:  #按时间下降排序
        ordering = ['-createTime']