from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def homepage(request):
    context = {'recipes_list': DATA.keys()
               }
    return render(request, 'calculator/home.html', context)


def show_page(request, **kwargs):
    recipe_name = kwargs.get('recipe_name', '')
    servings = int(request.GET.get("servings", 1))
    current_recipe = {}
    for ingredient, quantity in DATA[recipe_name].items():
        current_recipe[ingredient] = quantity * servings
    context = {
        'recipe': current_recipe
    }
    return render(request, 'calculator/index.html', context)
