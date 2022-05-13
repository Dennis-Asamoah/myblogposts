from django.urls import path, include
from . import views 


urlpatterns = [
    path('posts/',views.list_posts, name = 'posts'),
    path('posts/<int:id>', views.detailed_view, name = 'detailled_view'),
    path('postss/',views.ListPost.as_view(), name = 'postss'),
    path('postss/<int:pk>',views.DetailedView.as_view(), name = 'setailedview'),
]