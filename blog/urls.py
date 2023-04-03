from atexit import register
from unicodedata import name
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns= [
    path('', views.home, name = 'home'),
    path('post/<int:id>/', views.detail,name='detail'),
    path('newpost/', views.Addpost, name='newpost'),
    path('load/',views.load_more,name='load_more'),
    path('search_results/', views.search, name='search'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('post/<int:post_id>/comment/<int:parent_id>/', views.comment_replies, name='comment-replies'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)