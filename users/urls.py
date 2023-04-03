from atexit import register
from unicodedata import name
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users.forms import CustomLoginForm
from . import views

urlpatterns= [
    path('register/', views.register, name = 'register'),
    path('accounts/login/', auth_views.LoginView.as_view( authentication_form=CustomLoginForm,template_name='account/login.html'),name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(),name='logout.html'),
    path('category_search/',views.search_by_category,name='category_search'),
    re_path(r'^profile_page/(?P<username>[a-zA-Z0-9]+)$', views.show_profile, name='show_profile'),
    path('profile/', views.edit_profile, name='profile'),

]