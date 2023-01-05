from django.shortcuts import render

def index(request):
    return render(request, 'testmenu/base.html')

def page_with_menu(request, menu_title, pk):
    return render(request, 'testmenu/menu.html', {'menu': menu_title, 'pk': pk})
