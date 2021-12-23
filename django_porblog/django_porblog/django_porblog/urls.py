"""django_poblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls.conf import include
from blog import views
from django.conf.urls import url
from blog import views

from blog.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.blog_index, name='blog_index'),
    path('blog/', views.blog_index, name='blog_index'),
    path('<int:id>/post_publish/', views.post_publish, name='post_publish'),
    path("<int:id>/", views.blog_detail, name="blog_detail"),   
    url(r'^post/new/$', views.CreatePostView.as_view(), name='CreatePostView'),
    path('<int:id>/post_detail/', views.post_detail, name="post_detail"),
    path('<int:id>/post_edit/', views.post_edit, name="post_edit"),
    path('miembros/', views.nosotros, name='miembros'),
    path('<int:id>/post_remove/', views.post_remove, name="post_remove"),
    path('<int:id>/comment_remove/', views.comment_remove, name="comment_remove"),
    path('<int:id>/comment_aprove/', views.comment_approve, name="comment_approve"),
    path('<int:id>/comment_form/', views.add_comment_to_post, name="add_comment_to_post"),
    path('categorias/<str:category>/', views.blog_category, name='blog_category'),
   
    
    #path('', views.index, name='index'),
    #path('blog/', include('blog.urls'),),
    #path('', include(('blog_auth.urls', 'blog_auth'), namespace='blog_auth')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, show_indexes=True)
