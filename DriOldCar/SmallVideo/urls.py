from django.conf.urls import url
from .views import video_list, to_play, UserFormView

urlpatterns = [
    url(r'^$', video_list, name='videoindex'),
    url(r'^(?P<video_id>[0-9]+)/$', to_play, name='toplay'),
    url(r'^register/$', UserFormView.as_view(), name='register'),
    # url(r'^/(?P<app_id>\d{1,10})\.plist$', views.ios_app_plist, name='django_mobile_app_distribution_ios_app_plist'),

]