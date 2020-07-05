from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

app_name = "accounts"

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]

# 장고에서 지원하는 loginview와 logoutview를 활용하여 바로 login.html과 logout.html로 연결시켜줌
# 1차 url 연결 : 메인 urls.py에 path('accounts/', include('accounts.urls')) 추가
