from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,PostViewSet
router=DefaultRouter()
router.register(r'snippets', PostViewSet)
router.register(r'users', UserViewSet)
urlpatterns=[
path('',include(router.urls))

]