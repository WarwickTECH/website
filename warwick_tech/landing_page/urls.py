from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^login/$', auth_views.login, {'template_name': 'landing_page/login.html'}, name="login"),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name="logout"),
    url(r'^signup/$', views.signup, name="signup")
]
