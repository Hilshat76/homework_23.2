from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from article.apps import ArticleConfig
from article.views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = ArticleConfig.name

urlpatterns = [
    path('', ArticleListView.as_view(), name='articles_list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='articles_detail'),
    path('articles/create', ArticleCreateView.as_view(), name='articles_create'),
    path('articles/<int:pk>/update', ArticleUpdateView.as_view(), name='articles_update'),
    path('articles/<int:pk>/delete', ArticleDeleteView.as_view(), name='articles_delete')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)