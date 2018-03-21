from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static
from django.conf import settings

from trainer import (
    signup_trainer,
    trainer_login,
    user_logout
)

#urlpatterns = {
 #   url(r'^MYOS/create/', SignUpUserView.as_view(), name="create"),
  #  url(r'^MYOS/list/', DetailsView.as_view(), name="retrieve"),
   # url(r'^MYOS/fetchRecord/', GetRecord.as_view(), name="post"),
   # url(r'^MYOS/updateRecord/', UpdateRecord.as_view(), name="post"),
   # url(r'^MYOS/deleteRecord/', DeleteRecord.as_view(), name="post"),
#}

urlpatterns = [

    url(r'^MYOS/trainer/signup/$', signup_trainer, name='signup_trainer'),
    url(r'^MYOS/trainer/logout/$', user_logout, name='user_logout'),
    url(r'^MYOS/trainer/login/$', trainer_login, name='trainer_login'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


urlpatterns = format_suffix_patterns(urlpatterns)

