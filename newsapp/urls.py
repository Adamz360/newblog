from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.postslist.as_view(), name="posts"),
    path('<slug:slug>/', views.postdetail.as_view(), name="post_detail"),
]