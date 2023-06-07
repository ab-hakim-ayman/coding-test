from django.urls import path
from . import views

app_name='product'
urlpatterns = [
    path('', views.home, name='home'),
    path('product_create/', views.product_create, name='product_create'),
    path('category-create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('category-list/', views.CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category'),
    path('category-update/<int:pk>/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('category-delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='category-delete'),
    path('product-create/', views.ProductCreateView.as_view(), name='product-create'),
    path('product-list/', views.ProductListView.as_view(), name='products'),
    path('search_list/<int:page>/', views.search_list, name='search_list'),
    path('category_search/', views.category_search, name='category_search'),
    path('product-update/<int:pk>/', views.ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product'),

]
