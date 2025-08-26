from django.urls import path, include
from .views import RegisterView, LoginView, ProfileView, FollowUserView, UnfollowUserView, FeedView
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
   path('', include(router.urls)),

    # Registration, login, and profile management routes
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    
   # Other URL patterns...
   path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
   path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow_user'),
]