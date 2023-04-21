from rest_framework import serializers
from api.models import Product, ProductItem, ProductItemModification, Category, ModificationValue, FilterModification, DisplayOption, ProductItemImg


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ModificationValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModificationValue
        fields = '__all__'

class FilterModificationSerializer(serializers.ModelSerializer):
    filter_value = ModificationValueSerializer(many=True)
    class Meta:
        model = FilterModification
        fields = ['id', 'category', 'filter_name', 'filter_value', 'display_option']

class ModificationValueGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModificationValue
        fields = '__all__'
        depth = 1

class ProductItemModificationSerializer(serializers.ModelSerializer):
    modification_value = ModificationValueGetSerializer()
    class Meta:
        model = ProductItemModification
        fields = ['product_item', 'modification_value']


class ProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = '__all__'

class ProductItemImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItemImg
        fields = '__all__'

class ProductItemApiGetSerializer(serializers.ModelSerializer):
    item_modification = ProductItemModificationSerializer(many=True)
    images = ProductItemImgSerializer(many=True)
    class Meta:
        model = ProductItem
        fields = ['id', 'sku', 'item_img', 'qty_in_stock','price', 'item_modification', 'product', 'images']
        depth = 4

class ProductItemGetSerializer(serializers.ModelSerializer):
    item_modification = ProductItemModificationSerializer(many=True)
    class Meta:
        model = ProductItem
        fields = ['id', 'sku', 'item_img', 'hover_img', 'qty_in_stock','price', 'item_modification']

class ProductSerializer(serializers.ModelSerializer):
    product_variation = ProductItemGetSerializer(many=True)
    class Meta:
        model = Product
        fields = ['id', 'product_variation', 'name', 'category', 'description']
        depth=7

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class DisplayOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisplayOption
        fields = '__all__'