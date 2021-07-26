from django.urls import path
from .views import List,List_detail
urlpatterns=[
path('<int:pk>/',List_detail().as_view(),name='post_detail'),
path('',List.as_view(), name='post_view')

]