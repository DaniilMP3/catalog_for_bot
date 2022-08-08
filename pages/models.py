import mptt.fields
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey, TreeOneToOneField
from mptt.forms import TreeNodeMultipleChoiceField, TreeNodeChoiceField


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=50)
    image = models.ImageField(blank=False, upload_to='categories_images')

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Item(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50)
    category = TreeForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    image = models.ImageField(blank=False, upload_to='items_images')
    description = models.CharField(max_length=255)
    in_stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    old_price = models.FloatField(blank=True, null=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title


class Customer(models.Model):
    device = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return str(self.device)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)


class OrderItem(models.Model):
    product = models.ForeignKey(Item, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    data_added = models.DateTimeField(auto_now_add=True)