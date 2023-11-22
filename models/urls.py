from django.urls import path
from models import views

urlpatterns = [
    path("",views.import_data_csv),
    path("alldata",views.get_data_disney),
    path("check",views.get_data),

]