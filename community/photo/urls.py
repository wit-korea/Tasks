from django.urls import path
from .views import PhotoList, PhotoDelete, PhotoCreate, PhotoUpdate, PhotoDetail, PhotoLike, PhotoFavorite

app_name = 'photo'

urlpatterns = [
    path("create/", PhotoCreate.as_view(), name='create'),
    path("delete/<int:pk>/",PhotoDelete.as_view(), name='delete'),
    path("update/<int:pk>/",PhotoUpdate.as_view(), name ='update'),
    path("detail/<int:pk>/",PhotoUpdate.as_view(), name ='detail'),
    path("", PhotoList.as_view(),name='index'),
    path("like/<int:photo_id>/",PhotoLike.as_view(),name = 'like'),
    path("favorite/<int:photo_id>/",PhotoFavorite.as_view(),name = 'favorite'),

]

# as_view() 함수는 클래스의 인스턴스 생성, 인스턴스의 dispatch() 호출 
# dispatch 는 요청을 검사해서, 어떤 http 메소드로 요청되었는지 알아낸 뒤
# 인스턴스 내에서 해당 이름을 갖는 메소드 요청을 중계

# path -> 해당 url 이 들어오면, 뷰의 로직을 따라서 처리, name 은 해당 url 로 이동하도록

from django.conf.urls.static import static

from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
