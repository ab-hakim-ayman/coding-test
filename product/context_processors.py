from .models import Category

def get_all_categories(request):
    categories = Category.objects.order_by('-created_at')
    context = {
        'categories' : categories
    }
    return context