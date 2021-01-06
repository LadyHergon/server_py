from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostUpdateView, 
    PostDeleteView,
    UserPostListView,
    PhoneCreateView
    )
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/phone/', PhoneCreateView.as_view(), name='phone-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)