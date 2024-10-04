# blog/urls.py
from django.urls import path
from .views import (
    home,
    article_list,
    user_articles,
    article_detail,
    favourites,
    login_view,
    logout_view,
)

urlpatterns = [
    path('', home, name='home'),
    path('articles/', article_list, name='article_list'),
    path('my_articles/', user_articles, name='user_articles'),
    path('articles/<int:pk>/', article_detail, name='article_detail'),
    path('favourites/', favourites, name='favourites'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

]
