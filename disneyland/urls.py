from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from disneyland import views
from hello_world.core import views as core_views

urlpatterns = [
    path("",views.register),
    path("home",views.home),
    path("register",views.register),
    path("login",views.login),
    path("places",views.places),
    path("profile",views.profile),
    path("editprofile",views.editprofile)

]
