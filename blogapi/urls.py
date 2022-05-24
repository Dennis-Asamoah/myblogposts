from django.urls import path, include
from . import views 
from rest_framework.documentation import include_docs_urls
#from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('posts/',views.list_posts, name = 'posts'),
    path('posts/<int:id>', views.detailed_view, name = 'detailed_view'),
    path('postss/',views.ListPost.as_view(), name = 'postss'),
    path('postss/<int:pk>',views.DetailedView.as_view(), name = 'detailedview'),
    path('register/', views.register_user, name='register'),
    path('blacklist/', views.blacklist, name='blacklist'),
    path('foreign/', views.foreign, name='foreign'),
    path('foreignd/', views.Foreign.as_view(), name='foreign'),
    path('filter/', views.Filter.as_view(), name='filter'),
    path('doc/', include_docs_urls(title='mypostapidoc')),
    path('register_user/', views.RegisterUser.as_view(), name='registeruser'),
    path('users/', views.Authors.as_view(), name='authors'),
    path('users/<int:pk>', views.AuthorView.as_view(), name='authorview'),
    path('listitems/<slug:slug>', views.PostItems.as_view(), name='listitems'),
    path('listitem/<slug:slug>', views.list_detail, name='listitem'),
]