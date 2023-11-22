from django.urls import path
from models import views

urlpatterns = [
    path("",views.get_data_disney),
    path("check",views.get_data_disney),

]