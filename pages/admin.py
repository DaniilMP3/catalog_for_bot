from django.contrib import admin
from .models import Category, Item
from mptt.admin import MPTTModelAdmin
from mptt.fields import TreeForeignKey
from django import forms


class ItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(id__in=[category.id for category in Category.objects.all() if category.is_leaf_node()])
        self.fields['category'].level_indicator = ''

    class Meta:
        model = Item
        exclude = ('',)



class ItemModelAdmin(admin.ModelAdmin):

    form = ItemForm



admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Item, ItemModelAdmin)
