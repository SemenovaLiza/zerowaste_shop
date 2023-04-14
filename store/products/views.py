from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import Sort, Category


def paginator(request, object):
    paginator = Paginator(object, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def index(request):
    template = 'products/index.html'
    return render(request, template)


def product_sorts(request, slug):
    template = 'products/kitchen-items.html'
    category = get_object_or_404(Category, slug=slug)
    