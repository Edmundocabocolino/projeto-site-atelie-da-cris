from django.shortcuts import render, get_object_or_404
from recipes.models import Recipe

def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    # Se ainda não houver publicadas, lista todas para visualização
    if not recipes.exists():
        recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/page/home.html', context={
        'recipes': recipes,
    })

def recipeviews(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    return render(request, 'recipes/page/recipeviews.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })
