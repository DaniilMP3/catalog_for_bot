from django.http import JsonResponse
from django.shortcuts import render
from .models import Category, Item, Order, OrderItem
from django.views.generic import ListView, DetailView
from django.template.loader import render_to_string
import json


class HomePageView(ListView):
    model = Item
    template_name = 'home.html'
    context_object_name = 'items'


def categories_or_items_page(request, slug):
    cur_category = Category.objects.get(slug=slug)
    if not cur_category.is_leaf_node():
        context = {'categories': Category.objects.filter(parent_id=cur_category.id)}
        return render(request, 'categories_list.html', context)
    elif cur_category.is_leaf_node():
        context = {'items': Item.objects.filter(category_id=cur_category.id)}
        return render(request, 'items_list.html', context)


class ItemDetailView(DetailView):
    model = Item
    template_name = 'single_item.html'


def updateItem(request):
    data = json.loads(request.body)
    productID = data['productID']
    action = data['action']
    device = data['device']
    print('Action:', action)
    print('productID:', productID)


    product = Item.objects.get(id=productID)
    order, created = Order.objects.get_or_create(customer=device, complete=False)

    orderItem,  created = OrderItem.objects.get_or_create(order=order, product=productID)

    return JsonResponse('Item was added', safe=False)
