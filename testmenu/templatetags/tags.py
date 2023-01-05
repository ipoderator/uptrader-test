from django import template
from testmenu.models import *


register = template.Library()


@register.inclusion_tag('testmenu/all_categories.html')
def draw_menu(menu):
    all_categories = Category.objects.filter(menu__title=menu).select_related('parent')
    primary_cats = [cat for cat in all_categories if not cat.parent]
    return {
        'primary_cats': primary_cats,
        'menu': menu
        }


@register.inclusion_tag('testmenu/categories.html')
def draw_selected_cat(menu, pk):
    catalog = Category.objects.filter(menu__title=menu).select_related('parent')
    primary_cats = [cat for cat in catalog if not cat.parent]
    subcats = [cat for cat in catalog if cat.parent is not None and cat.parent.title == pk]
    tree = []
    for cat in catalog:
        if cat.title == pk:
            category = cat
    while True:
        if category.parent is None:
            tree.append(category)
            break
        else:
            tree.append(category)
            category = category.parent
    return {'catalog': catalog, 'primary_cats': primary_cats, 'subcats': subcats, 'menu': menu, 'target_cat': pk, 'tree': tree}


@register.inclusion_tag('testmenu/podcategories.html')
def draw_subcats(menu, catalog, tree):
    current_cat = tree[-1]
    tree = tree[0:-1]
    target_cat = tree[0]
    all_categories = []
    subcats = []
    for cat in catalog:
        if cat.parent:
            if cat.parent == current_cat:
                all_categories.append(cat)
            elif cat.parent == target_cat:
                subcats.append(cat)
    return {'catalog': catalog, 'menu': menu, 'all_categories': all_categories, 'tree': tree, "current_cat": current_cat, 'target_cat': target_cat, 'subcats': subcats}



