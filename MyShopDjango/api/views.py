from django.shortcuts import render
from rest_framework import views, generics
from api.serializers import *
from api.models import *
from rest_framework import viewsets
from django_filters import rest_framework as filters
import django_filters

# Create your views here.


class TestView(viewsets.ModelViewSet):
    queryset = ProductItemModification.objects.all()
    serializer_class = ProductItemModificationSerializer
    # filter_backends = [filters.SearchFilter]
    filterset_fields = ['modification_value__modification_value', 'product_item']
    
    def get_queryset(self):
        return super().get_queryset()

    def filter_queryset(self, queryset):
        return super().filter_queryset(queryset)

class ModificationValuesListView(generics.ListCreateAPIView):
    queryset = ModificationValue.objects.all()
    serializer_class = ModificationValueSerializer
    filterset_fields = ['filter_modification__category__category_name', 'filter_modification__filter_name', 'filter_modification']
    
    def get_queryset(self):
        return super().get_queryset()

class ProductItemView(viewsets.ModelViewSet):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer
    filterset_fields = ['product__category']


class ProductItemGetView(viewsets.ReadOnlyModelViewSet):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemApiGetSerializer
    filterset_fields = ['product__category']


class CategoryListView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ['category_name']

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class FilterModificationsListView(viewsets.ModelViewSet):
    queryset = FilterModification.objects.all()
    serializer_class = FilterModificationSerializer
    filterset_fields = ['category__category_name', 'filter_name', 'category']

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class DisplayOptionView(viewsets.ModelViewSet):
    queryset = DisplayOption.objects.all()
    serializer_class = DisplayOptionSerializer


class NumberInFilter(django_filters.BaseInFilter, django_filters.NumberFilter):
    pass


class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter
    product_variation__item_modification__modification_value = NumberInFilter(distinct=True)
    
    class Meta:
        model = Product
        fields = ['category', 'product_variation__item_modification__modification_value']


class ProductListView(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter

    def get_queryset(self):
        return super().get_queryset()

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer


class ProductItemImageView(viewsets.ModelViewSet):
    queryset = ProductItemImg.objects.all()
    serializer_class = ProductItemImgSerializer
