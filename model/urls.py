from django.urls import path
from .views import post_view,post_detail
urlpatterns=[
path('<int:id>/',post_detail,name='post_detail'),
path('',post_view, name='post_view')

]