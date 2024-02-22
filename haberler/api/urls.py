from django.urls import path 
from haberler.api import views as api_views


# CLASS APIVIEW
urlpatterns = [
    path('writers/', api_views.WriterListCreateAPIView.as_view(),name='writer-list'),
    path('articles/', api_views.ArticleListCreateAPIView.as_view(), name='article-list'),
    path('articles/<int:pk>', api_views.ArticleDetailAPIView.as_view(), name='article-detail'),
]

