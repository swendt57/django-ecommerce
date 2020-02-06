from django.conf.urls import url, include
from accounts.views import logout, login, register, user_profile, change_password

urlpatterns = [
    url(r'^$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', user_profile, name='profile'),
    url(r'^change_password/$', change_password, name='change_password'),  # this one can be used if the user is authenticated

    url('^', include('django.contrib.auth.urls')),  # used for password resetting if the user forgets their password
]

# The auth.urls included are:
# password_reset
# password_reset/done
# reset/<uid>/<token>
# reset/done
