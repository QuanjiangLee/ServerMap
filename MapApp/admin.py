from django.contrib import admin
from MapApp.models import myServerMap
from MapApp.models import userInf

# Register your models here.
admin.site.register(myServerMap)
admin.site.register(userInf)