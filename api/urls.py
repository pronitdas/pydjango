from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SignUpUserView ,DetailsView,GetRecord, UpdateRecord, DeleteRecord

urlpatterns = {
    url(r'^MYOS/create/', SignUpUserView.as_view(), name="create"),
    url(r'^MYOS/list/', DetailsView.as_view(), name="retrieve"),
    url(r'^MYOS/fetchRecord/', GetRecord.as_view(), name="post"),
    url(r'^MYOS/updateRecord/', UpdateRecord.as_view(), name="post"),
    url(r'^MYOS/deleteRecord/', DeleteRecord.as_view(), name="post"),
}

urlpatterns = format_suffix_patterns(urlpatterns)