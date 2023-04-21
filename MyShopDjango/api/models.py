from django.db import models

# Create your models here.


# ------------------ Categories -----------------------
class Category(models.Model):
    category_name = models.CharField(max_length=255)
    category_img = models.FileField('categories/')
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.category_name


class DisplayOption(models.Model):
    display_name = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.display_name


class FilterModification(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    filter_name = models.CharField(max_length=255, unique=True)
    display_option = models.ForeignKey('DisplayOption', on_delete=models.SET_NULL, null=True, default=None)

    def __str__(self) -> str:
        return self.filter_name


class ModificationValue(models.Model):
    modification_value = models.CharField(max_length=255)
    filter_modification = models.ForeignKey(
        'FilterModification', on_delete=models.CASCADE, related_name='filter_value')

    def __str__(self) -> str:
        return self.filter_modification.filter_name +': ' + self.modification_value


# ------------------- Products --------------------------
class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()
    def __str__(self) -> str:
        return self.name


class ProductItem(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE,  related_name='product_variation', related_query_name='product_variation')
    sku = models.CharField(max_length=8, unique=True)
    item_img = models.FileField('item_image')
    hover_img = models.FileField('alter_image', null=True)
    qty_in_stock = models.PositiveBigIntegerField()
    price = models.PositiveIntegerField()
    def __str__(self) -> str:
        return self.product.name +': ' + self.sku


class ProductItemImg(models.Model):
    product = models.ForeignKey('ProductItem', on_delete=models.CASCADE,  related_name='images')
    item_img = models.FileField('big_images')

# ---------------- Products info ----------------
class ProductItemModification(models.Model):
    product_item = models.ForeignKey('ProductItem', on_delete=models.CASCADE, related_name='item_modification')
    modification_value = models.ForeignKey('ModificationValue', on_delete=models.CASCADE)
