from django.urls import path
from .views import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import static

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/<slug:slug>/', ElementsView.as_view(), name='list_elements'),
    path('products/<slug:param1>/<slug:param2>', DetailView.as_view(), name='detail_element'),
    path('works/<slug:slug2>', ProductView.as_view(), name='product'),
    path('products/', ProductsView.as_view(), name='products')
]