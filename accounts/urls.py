from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', include('django.contrib.auth.urls')),  # 로그아웃 URL 추가
]

