from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('photo.urls')),
    # 가장 기본 주소가 들어오면 photo의 url로 연결
]
