from .models import Item, Category, Order, Customer


def categories_processor(request):
    if 'device' in request.COOKIES:
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cart_items = order.orderitem_set.all()
        return {
            'nodes': Category.objects.all(),
            'cart_items': cart_items,
            'order': order}

    else:
        cart_items = []
        return {
            'nodes': Category.objects.all(),
            'cart_items': cart_items,}



