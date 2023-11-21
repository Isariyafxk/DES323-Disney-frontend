from django.urls import path
from models import views

urlpatterns = [
    path("",views.import_data_csv),

]