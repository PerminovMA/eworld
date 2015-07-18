__author__ = 'PerminovMA@live.ru'

from django.conf.urls import url

urlpatterns = [
    url(r'registration', 'profiles.views.user_registration', name='registration'),
    url(r'authorization', 'profiles.views.user_authorization', name='authorization'),
    url(r'logout', 'django.contrib.auth.views.logout', {'next_page': 'index'}, name='logout'),
]