from django.urls import path
from .views import HomePageView, ItemDetailView, categories_or_items_page, updateItem
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('item/<slug:slug>/', ItemDetailView.as_view(), name='single_item'),
    path('category/<slug:slug>/', categories_or_items_page, name='categories_or_items_list'),
    path('update_item/', updateItem, name='update_item'),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

