from django import forms

from  .models import Category, Product, ProductImage, ProductVariant, ProductVariantPrice

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        
class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'
        
class ProductImageForm(forms.ModelForm):
    
    class Meta:
        model = ProductImage
        fields = '__all__'
        
class ProductVariantForm(forms.ModelForm):
    
    class Meta:
        model = ProductVariant
        fields = '__all__'
        
class ProductVariantPriceForm(forms.ModelForm):
    
    class Meta:
        model = ProductVariantPrice
        fields = '__all__'


class SearchForm(forms.Form):
    title = forms.CharField()
    category = forms.CharField()
    price_from = forms.FloatField()
    price_to = forms.FloatField()
    date = forms.DateField()
    
class CategorySearchForm(forms.Form):
    title = forms.CharField()