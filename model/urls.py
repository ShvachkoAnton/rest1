from django.urls import path,include
from .views import List,List_detail,UserList,UserDetail,api_root,PostHighlight
urlpatterns=[path('',api_root),
path('snippets/<int:pk>/',List_detail().as_view(),name='post-detail'),
path('snippets/',List.as_view(), name='snippet-list'),
path('users/', UserList.as_view(), name='user-list'),
path('users/<int:pk>/',UserDetail.as_view(), name='user-detail'),

path('snippets/<int:pk>/highlight/', PostHighlight.as_view(), name='snippet-highlight'),


]
