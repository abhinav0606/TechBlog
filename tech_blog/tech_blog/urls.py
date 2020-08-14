"""tech_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.lgn_rgstr,name='Login'),
    path('excell/',view.excell,name='Excell'),
    path('TechBlog/',view.home,name="Home"),
    path('logout/',view.log,name='Logout'),
    path('about/',view.about,name="Developers"),
    path('adm/',view.admin,name="admin"),
    path('accepts/<str:username>',view.accepts,name="accepts"),
    path('rejects/<str:username>',view.rejects,name="rejects"),
    path('blog/',view.blogg,name="blog"),
    path('write/',view.writ_the_blog,name="write"),
    path('blog/<str:title>',view.full_blog,name="Full_Blog")
]
