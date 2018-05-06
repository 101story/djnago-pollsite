from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    # 빈경로인 경우 views.index 함수가 실행되도록 해라
    path('', views.index, name='index'),
    url(r'^areas/(?P<area>.+)/$', views.areas),
    url(r'^polls/(?P<poll_id>\d+)/$', views.polls)
]
