from django.urls import path
from . import views

urlpatterns = [
    # 빈경로인 경우 views.index 함수가 실행되도록 해라
    path('', views.index, name='index'),
]
