from django.shortcuts import render
from django.views import generic
from . models import Product
from .forms import CategoryForm
# Create your views here.

def index(request):
    return render(request, 'shop/index.html')

class CategoryView(generic.ListView):
    model = Product
    template_name = 'shop/category.html'

class ProductView(generic.DetailView):
    model = Product
    template_name = 'shop/product.html'

def form(request):
    return render(request, 'shop/form.html', {'form':CategoryForm()})