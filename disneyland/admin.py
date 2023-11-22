from django.contrib import admin
from .models import userInfo, DisneylandReview

# Register your models here.

class userInfoAdmin(admin.ModelAdmin):
    pass

admin.site.register(userInfo, userInfoAdmin)


@admin.register(DisneylandReview)
class Disneyadmin(admin.ModelAdmin):
    pass