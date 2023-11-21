from django.contrib import admin
from .models import userInfo

# Register your models here.

class userInfoAdmin(admin.ModelAdmin):
    pass

admin.site.register(userInfo, userInfoAdmin)
