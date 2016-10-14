from django.conf.urls import url
from user.views import home, SignUpView

urlpatterns = [
    url(r'^home/$', home, name='user_home'),
    url(r'^signup/$', SignUpView.as_view(), name='user_signup')
]
