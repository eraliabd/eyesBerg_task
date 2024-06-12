from django.urls import path
from .views import (
    LogoListCreateView,
    LogoDetailView,
    ConferenceSectionListCreateView,
    ConferenceSectionDetailView
)

urlpatterns = [
    path('logo/', LogoListCreateView.as_view(), name='logo-list-create'),
    path('logo/<int:pk>/', LogoDetailView.as_view(), name='logo-detail'),

    path('conference/', ConferenceSectionListCreateView.as_view(), name='conference-list-create'),
    path('conference/<int:pk>/', ConferenceSectionDetailView.as_view(), name='conference-detail'),
]
