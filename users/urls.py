from django.urls import path
from .views import UserCreateView, CustomUserDetail, UserListView

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('<int:pk>/', CustomUserDetail.as_view(), name='user-detail'),
]
