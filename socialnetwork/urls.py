"""socialnetwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from registrationapp.views import *
from forum.views import show_forum
from socialnetwork.settings import DEBUG, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', show_registration_form),
    path('success_reg/', show_successfull_reg, name = 'success_reg'),
    path('login/', show_login_form, name = 'login'),
    path('welcome/',show_welcome, name = 'welcome'),
    path('logout/', user_logout, name = 'logout'),
    path('forum/', show_forum, name = 'forum')
]
# Формуємо URL адреси у медіа файлі
if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)