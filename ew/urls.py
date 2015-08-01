"""ew URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from profiles import urls as profiles_urls
from eworld import urls as eworld_urls
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='eworld/index.html'), name='index'),
    url(r'^eworld/', include(eworld_urls, namespace='eworld')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile/', include(profiles_urls, namespace='profile')),
    url(r'^angular_urls_config$', TemplateView.as_view(template_name='eworld/js/urls_config.js'),
        name='angular_urls_config'),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Only for development (not production).
