from django.urls import path
from django.conf.urls import url
from blog import views

app_name='apps'

urlpatterns = [
    path("blog/", views.blog_index, name="blog_index"),
    #path("<int:id>/", views.blog_detail, name="blog_detail"),
    #url(r'^post/new/$', views.CreatePostView.as_view(), name='CreatePostView'),
    path('contacto', views.contact, name='contact')
]