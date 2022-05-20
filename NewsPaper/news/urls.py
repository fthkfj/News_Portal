from django.urls import path
from .views import PostList, PostDetail


urlpatterns = [
    path('', PostList.as_view()),
    path('news_id.html', PostDetail.as_view()),
]
