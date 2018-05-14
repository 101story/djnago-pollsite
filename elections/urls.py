from django.urls import path
from django.conf.urls import url

from . import views

app_name='elections'
urlpatterns = [
    # 빈경로인 경우 views.index 함수가 실행되도록 해라
    path('', views.index, name='home'),
    url(r'^areas/(?P<area>[가-힣]+)/$', views.areas),
    url(r'^areas/(?P<area>[가-힣]+)/results$', views.results),
    url(r'^polls/(?P<poll_id>\d+)/$', views.polls),
    path('candidate/<int:pk>/', views.candidate, name='candidate'),
    path('candidate/new/', views.newcandidate, name='newcandidate'),
    path('candidate/<int:pk>/edit/', views.editcandidate, name='editcandidate')
]
