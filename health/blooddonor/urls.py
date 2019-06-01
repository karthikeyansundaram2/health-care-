from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.Login.as_view(),name='login'),
    url(r'^register/',views.register,name='register'),
    url(r'^bloodbankregister/',views.bloodbankregister.as_view(),name='bloodbankregister'),
    url(r'^hospitalregister/',views.hospitalregister.as_view(),name='hospitalregister'),
    url(r'^donorregister/',views.donorregister.as_view(),name='donorregister'),
    url(r'^(?P<LoginName>[-\w]+)/(?P<User>[-\w]+)/$', views.bloodbank, name='bloodbank'),
    url(r'^hospitalrequirements/$', views.hospital.as_view(), name='hospital'),
    url(r'^donordetails/$',views.donor.as_view(),name='donor'),
    url(r'^viewhospital/',views.viewhospital,name='viewhospital'),
    url(r'^viewdonor/',views.viewdonor,name='viewdonor'),
    url(r'^logout/',views.Login.as_view(),name='logout'),
]
