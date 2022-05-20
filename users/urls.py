from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
   path('',views.indexViews,name="home"),
   path('about/',views.aboutViews,name="about"),
   path('registro/',views.registroViews,name="registro"),
   path('login/',LoginView.as_view(template_name='login.html'),name="login"),
   path('logout/',LogoutView.as_view(template_name='logout.html'),name="logout"),
]