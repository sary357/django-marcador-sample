from django.conf.urls import url
from myapp.views import bookmark_user
from myapp.views import bookmark_list

urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$',bookmark_user,name='myapp_bookmark_user'),
    url(r'^$',bookmark_list,name='myapp_bookmark_list'),
]