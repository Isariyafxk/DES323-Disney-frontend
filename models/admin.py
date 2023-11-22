from django.contrib import admin
from .models import *

@admin.register(DisneylandReview)
class DisneylandReview(admin.ModelAdmin):
    pass 