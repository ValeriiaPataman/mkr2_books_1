from django.shortcuts import render
from .models import Recipe, Category
from django.db.models import Count


def main(request):
    recipes = Recipe.objects.all().order_by('-created_at')[:5]
    return render(request, 'recipe/main.html', {'recipes': recipes})


def category_list(request):
    categories = Category.objects.annotate(recipes_count=Count('recipe'))
    return render(request, 'recipe/category_list.html', {'categories': categories})
