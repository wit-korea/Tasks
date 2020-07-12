  
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RelationView, RelationCreateView, RelationDeleteView, UserInfoGetView
from . import views

app_name = "accounts"

urlpatterns = [
    path('relationuserinfo/',UserInfoGetView.as_view(), name='relationuserinfo'),
    path('relationdelete/',RelationDeleteView.as_view(), name='relationdelete'),
    path('relationcreate/',RelationCreateView.as_view(), name='relationcreate'),
    path('relation/',RelationView.as_view(template_name = 'accounts/relation.html'), name='relation'),
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name = 'accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'accounts/logout.html'), name='logout' ),
]