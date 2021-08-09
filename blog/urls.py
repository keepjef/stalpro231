from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/<slug:slug>/', ElementsView.as_view(), name='list_elements'),
    path('products/<slug:param1>/<slug:param2>', DetailView.as_view(), name='detail_element'),
    path('works/<slug:slug>', ProductView.as_view(), name='product'),
]