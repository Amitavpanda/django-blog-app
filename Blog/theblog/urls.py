from django.urls import path
from . import views
from .views import HomeView
from .views import ArticleDetailsView, AddPostView, EditPostView, DeletePostView
urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailsView.as_view(), name='article_details'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/update_post/<int:pk>', EditPostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),




]