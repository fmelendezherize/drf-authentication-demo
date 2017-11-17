"""
Definition of urls for drf_authentication_demo.
"""

from django.conf.urls import include, url
from rest_framework_jwt.views import obtain_jwt_token

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', drf_authentication_demo.views.home, name='home'),
    # url(r'^drf_authentication_demo/', include('drf_authentication_demo.drf_authentication_demo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^', include('other_module.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/auth/', include('authentication.urls')),
    url(r'^api/v1/auth/', include('authentication.urls')),
]
