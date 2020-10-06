from django.conf.urls import url

from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import AppleProvider
from .views import oauth2_finish_login

urlpatterns = default_urlpatterns(AppleProvider)

urlpatterns += [
    url(r'^apple/logincallback/finish/$',		
            oauth2_finish_login, name="apple_finish_callback"),
]
