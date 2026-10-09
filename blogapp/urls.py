from django.urls import path
from blogapp.views import PostListView, post_detail

app_name = 'blog'

urlpatterns = [
    # 1. Barcha postlar ro'yxati (List) uchun URL:
    path('', PostListView.as_view(), name='post_list'),

    # 2. Bitta postning batafsil sahifasi (Detail) uchun URL:
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', post_detail, name='post_detail'),
]