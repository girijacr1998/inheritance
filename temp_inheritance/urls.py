from django.conf.urls import url
from temp_inheritance import views

app_name='temp_inheritance'
urlpatterns=[
    url(r'^relative/$',views.base,name='base'),
    url(r'^others/$',views.others,name='others'),
]