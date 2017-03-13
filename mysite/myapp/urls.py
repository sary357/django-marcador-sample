from django.conf.urls import url
from myapp.views import bookmark_user
from myapp.views import bookmark_list
from myapp.views import bookmark_create
from myapp.views import bookmark_edit


urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$',bookmark_user,name='myapp_bookmark_user'),
    url(r'^create/$', bookmark_create, name='myapp_bookmark_create'),
    url(r'^edit/(?P<pk>\d+)/$', bookmark_edit, name='myapp_bookmark_edit'),
    url(r'^$',bookmark_list,name='myapp_bookmark_list'),

]