from django.urls import path
from .views import CategoryCountView, ItemCountView, CategoryCreateView, ItemCreateView

urlpatterns = [
    path('category/count/', CategoryCountView.as_view(), name='category-count'),
    path('item/count/', ItemCountView.as_view(), name='item-count'),
    path('category/create/', CategoryCreateView.as_view(), name='category-create'),
    path('item/create/', ItemCreateView.as_view(), name='item-create'),
]
