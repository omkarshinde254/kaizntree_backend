from django.urls import path
from .views import CategoryCountView, ItemCountView, CategoryCreateView, ItemCreateView, CategoryListView, ItemListView, CategoryFilterView, ItemFilterView

urlpatterns = [
    path('category/count/', CategoryCountView.as_view(), name='category-count'),
    path('item/count/', ItemCountView.as_view(), name='item-count'),
    path('category/create/', CategoryCreateView.as_view(), name='category-create'),
    path('item/create/', ItemCreateView.as_view(), name='item-create'),
    path('category/list/', CategoryListView.as_view(), name='category-list'),
    path('item/list/', ItemListView.as_view(), name='item-list'),
    path('filter/category', CategoryFilterView.as_view(), name='category-filter'),
    path('filter/item', ItemFilterView.as_view(), name='item-filter'),
]
