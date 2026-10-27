
from django.urls import path,include
from .views import CategoryViewSet,ItemViewSet,ConversationViewSet,ConversationmessageViewset,UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'items', ItemViewSet, basename='item')
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'conversationmessages', ConversationmessageViewset, basename='conversationmessage')

urlpatterns = [
    path('api/token/',TokenObtainPairView.as_view(), name="token_obtain_view"),
    path('api/token/refresh/',TokenRefreshView.as_view(), name="token_refresh_view"),
    path('api/', include(router.urls)),
]
