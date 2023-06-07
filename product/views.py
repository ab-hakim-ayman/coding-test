from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .forms import ProductForm, ProductImageForm, ProductVariantForm, ProductVariantPriceForm, SearchForm, CategorySearchForm
from .models import Category, Product

# Create your views here.
def home(request):
    product = Product.objects.all()
    context = {
        'product': product,
    }
    return render(request, 'dashboard.html', context)


class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('product:home')
    template_name = "category-form.html"


class CategoryListView(ListView):
    model = Category
    paginate_by = 2
    template_name = "category-list.html"
    

class CategoryDetailView(DetailView):
    model = Category
    template_name = "category-detail.html"



class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['title', 'description']
    template_name = "category-form.html"


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('product:category-list')



class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product:home')
    template_name = "product-form.html"
    

class ProductListView(ListView):
    model = Product
    paginate_by = 2
    template_name = "product-list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product-detail.html"
    

class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product:products')
    template_name = "product-form.html"
    

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product:product-list')
    

def product_create(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        product_image_form = ProductImageForm(request.POST, request.FILES)
        product_variant_form = ProductVariantForm(request.POST)
        product_variant_price_form = ProductVariantPriceForm(request.POST)
        if product_form.is_valid() and product_image_form.is_valid() and product_variant_form.is_valid() and product_variant_price_form.is_valid():
            product_form.save()
            product_image_form.save()
            product_variant_form.save()
            product_variant_price_form.save()
    product_form = ProductForm()
    product_image_form = ProductImageForm()
    product_variant_form = ProductVariantForm()
    product_variant_price_form = ProductVariantPriceForm()
    context = {
        'product_form':product_form,
        'product_image_form':product_image_form,
        'product_variant_form':product_variant_form,
        'product_variant_price_form':product_variant_price_form
    }
    return render(request, 'creation_form.html', context)

    
    
def search_list(request, page=1):
    # title = request.GET.get('title')
    # category = request.GET.get('category')
    # price_from = request.GET.get('price_from')
    # price_to = request.GET.get('price_to')
    # date = request.GET.get('date')
    # products = Product.objects.filter(Q(title__icontains=title) | Q(category__title__icontains=category) | Q(created_at=date))
    # paginator = Paginator(products, 2)
    # try:
    #     results = paginator.page(page)
    # except PageNotAnInteger:
    #     results = paginator.page(1)
    # except EmptyPage:
    #     results = paginator.page(paginator.num_pages)
    # context = {
    #     'results':results,
    #     'products':products
    # }
    # return render(request, 'search_list.html', context)

    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            category = form.cleaned_data['category']
            price_from = form.cleaned_data['price_from']
            price_to = form.cleaned_data['price_to']
            date = form.cleaned_data['date']
            products = Product.objects.filter(Q(title__icontains=title) | Q(category__title__icontains=category) | Q(created_at=date))
            # results = results.union(ProductVariantPrice.objects.filter(price__range=(price_from, price_to)))
            paginator = Paginator(products, 6)
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                results = paginator.page(1)
            except EmptyPage:
                results = paginator.page(paginator.num_pages)
            context = {
                'results':results,
                'products':products
            }
            return render(request, 'search_list.html', context)
    context = {
        'form':form
    }
    return render(request, 'dashboard.html', context)
    
def category_search(request):
    form = CategorySearchForm()
    if request.method == 'POST':
        form = CategorySearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            results = Category.objects.filter(Q(title__icontains=title))
            context = {
                'results':results
            }
            return render(request, 'category-list.html', context)
        return render(request, 'category-list.html')
    return render(request, 'category-list.html', {'form':form})
    
    
# def product_update(request, id):
#     instance = get_object_or_404(Product, id=id)
    
#     if request.method == 'POST':
#         form = ProductForm(request.POST, instance=instance)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = ProductForm(instance=instance)
        
#     context = {
#         'form':form,
#         'instance':instance
#     }
#     return render(request, 'product-form.html', context)
    
    
    
    
    
