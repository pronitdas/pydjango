from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static
from django.conf import settings
from views import (
    signup_user,
    user_details, 
    user_login, 
    user_logout, 
    update_deviceToken, 
    create_session,  
    user_profile, 
    user_editprofile, 
    favroites_trainer,
    apply_promocode
    ) 

#urlpatterns = {
 #   url(r'^MYOS/create/', SignUpUserView.as_view(), name="create"),
  #  url(r'^MYOS/list/', DetailsView.as_view(), name="retrieve"),
   # url(r'^MYOS/fetchRecord/', GetRecord.as_view(), name="post"),
   # url(r'^MYOS/updateRecord/', UpdateRecord.as_view(), name="post"),
   # url(r'^MYOS/deleteRecord/', DeleteRecord.as_view(), name="post"),
#}

urlpatterns = [

    url(r'^MYOS/user/usersignup/$', signup_user, name='signup_user'),
    url(r'^MYOS/user/userprofile/$', user_profile, name='user_profile'),
    url(r'^MYOS/user/usereditprofile/$', user_editprofile, name='user_editprofile'),
    url(r'^MYOS/user/login/$', user_login, name='user_login'),
    url(r'^MYOS/user/logout/$', user_logout, name='user_logout'),
    url(r'^MYOS/user/updatetoken/$', update_deviceToken, name='update_deviceToken'),
    url(r'^MYOS/user/createsession/$', create_session, name='create_session'),
    url(r'^MYOS/user/favroitestrainer/$', favroites_trainer, name='favroites_trainer'),
    url(r'^MYOS/user/applypromocode/$', apply_promocode, name='apply_promocode')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


urlpatterns = format_suffix_patterns(urlpatterns)

