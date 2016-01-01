"""rsquarelabs_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    #admin
    url(r'^admin/', admin.site.urls),

    #oauth
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    #api auth
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #api docs
    url(r'^docs/', include('rest_framework_swagger.urls')),

    #restful
    url(r'^restful/', include('restful.users.urls')),

    #website
    url(r'^', include('website.urls')),

]