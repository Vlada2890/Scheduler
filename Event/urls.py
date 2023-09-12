from django.urls import path
from .views import (
    ArticleDetailView,
    ArtView,
)

urlpatterns = [
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path('', ArtView.as_view(), name='articles'),
    
]
