from django.urls import path

from api.views import TestView, ModificationValuesListView, CategoryListView, \
    FilterModificationsListView, ProductListView, ProductCreateView, ProductItemView, DisplayOptionView, ProductItemGetView, ProductItemImageView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'category', CategoryListView, basename='category')
router.register(r'filter', FilterModificationsListView, basename='modifier')
router.register(r'product', ProductListView, basename='product')
router.register(r'test', TestView, basename='test')
router.register(r'product_items', ProductItemView, basename='product_items')
router.register(r'product_item', ProductItemGetView, basename='product_item')
router.register(r'display_option', DisplayOptionView, basename='display_option')
router.register(r'product_item_img', ProductItemImageView, basename='product_item_img')

urlpatterns = [
    path('modification_value/', ModificationValuesListView.as_view(), name='modifier'),
    path('product/create', ProductCreateView.as_view(), name='product_creator')
] + router.urls 