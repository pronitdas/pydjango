from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static
from django.conf import settings

from .views import SignUpUserView ,DetailsView,GetRecord, UpdateRecord, DeleteRecord
from views import *
#urlpatterns = {
 #   url(r'^MYOS/create/', SignUpUserView.as_view(), name="create"),
  #  url(r'^MYOS/list/', DetailsView.as_view(), name="retrieve"),
   # url(r'^MYOS/fetchRecord/', GetRecord.as_view(), name="post"),
   # url(r'^MYOS/updateRecord/', UpdateRecord.as_view(), name="post"),
   # url(r'^MYOS/deleteRecord/', DeleteRecord.as_view(), name="post"),
#}

urlpatterns = [

    url(r'^MYOS/create/$', create_list, name='create_list'),
    url(r'^MYOS/details/(?P<pk>[0-9]+)$', user_details, name='user_details'),
    url(r'^MYOS/login/$', user_login, name='user_login'),
    url(r'^MYOS/logout/(?P<pk>[0-9]+)$', user_logout, name='user_logout'),
    url(r'^MYOS/updatetoken/(?P<pk>[0-9]+)$', update_deviceToken, name='update_deviceToken'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


urlpatterns = format_suffix_patterns(urlpatterns)

