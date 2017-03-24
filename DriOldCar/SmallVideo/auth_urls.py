from django.conf.urls import url
from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^$', auth_views.login,{'template_name': 'SmallVideo/login.html'},name='auth_login'),
]