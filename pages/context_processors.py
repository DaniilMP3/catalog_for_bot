from .models import Item, Category


def categories_processor(request):
    return {
        'nodes': Category.objects.all()
    }