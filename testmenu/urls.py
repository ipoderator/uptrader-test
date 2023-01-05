from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('menu/<slug:menu_title>/category/<slug:pk>', page_with_menu, name='selected_cat')
]