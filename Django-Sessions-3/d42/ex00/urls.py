# ex00/urls.py
from django.urls import path
from .views import home, create_tip, signup, login_view, logout_view, tips, tips_list, delete_tip, downvote_tip

urlpatterns = [
    path('tips/<int:tip_id>/delete/', delete_tip, name='delete_tip'),
    path('tips/<int:tip_id>/downvote/', downvote_tip, name='downvote_tip'),
    path('', home, name='home'),
    path('tips/', tips_list, name='tips_list'),
    path('create-tip/', create_tip, name='create_tip'),  # URL pour créer un tip
    path('signup/', signup, name='signup'),
    path('tips/', tips, name='tips'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
