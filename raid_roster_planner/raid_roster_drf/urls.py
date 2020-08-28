from django.urls import re_path

from . import views


urlpatterns = [
    re_path(r'^input/$', views.InputView.as_view(), name='input_form'),
    re_path(r'^roster/$', views.RosterView.as_view(), name='roster')
]
