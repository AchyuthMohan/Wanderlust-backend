from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import BlacklistTokenView,LoggedInUserView,RegisterView,TrendingView,PlaceViewSet
router=DefaultRouter()
router.register('places',PlaceViewSet, basename='places')
router.register('register',RegisterView,basename='register')
router.register('trending',TrendingView,basename='trending')
urlpatterns = [
    path('',include(router.urls)),
    path('api/token/',TokenObtainPairView.as_view(),name="token_obtain"),
    path('api/token/refresh/',TokenRefreshView.as_view(),name="refresh_token"),
    path('api/token/blacklist/',BlacklistTokenView.as_view(),name="blacklist"),
    path('current-user/', LoggedInUserView.as_view(), name='currentuser'),
]