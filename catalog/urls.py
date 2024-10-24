from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, contacts, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView
from django.views.decorators.cache import cache_page


app_name = CatalogConfig.name

urlpatterns = [
    path('',ProductListView.as_view(), name='home'),
    path('products/<int:pk>/',cache_page(60)(ProductDetailView.as_view()), name='products_detail'),
    path('products/create',ProductCreateView.as_view(), name='products_create'),
    path('products/<int:pk>/update',ProductUpdateView.as_view(), name='products_update'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='products_delete'),
    path('contacts/',contacts,name='contacts')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)