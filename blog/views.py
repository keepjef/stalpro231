from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from blog.models import Partition, Product
from blog.forms import FeedBackForm
from django.core.mail import send_mail, BadHeaderError
from blog.tlgrm import send_message


# class PartitionListView(ListView):
#
#     model = Partition
#     template_name = 'index.html'

form = FeedBackForm()

def form_post(self, request):
    form = FeedBackForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        addr = form.cleaned_data['addr']
        text = f'Телефон: {phone}\n Имя: {name}\n Адрес: {addr}'
        try:
            send_message(text)
        except ValidationError:
            return form.errors
        return redirect('/')


class ElementsView(View):

    def get(self, request, slug):
        elements = Partition.objects.get(slug=slug)
        fil = elements.elements.all()
        return render(request, 'allnaves.html', {"fil": fil, "elements": elements})


class DetailView(View):

    def get(self, request, param1, param2):
        el = get_object_or_404(Partition, slug=param1)
        element = get_object_or_404(el.elements, slug=param2)
        benefits = element.benefits.all()
        all_naves = element.products.all()
        context = {
            'element': element,
            'benefits': benefits,
            'all_naves': all_naves
        }
        return render(request, 'rubric_detail.html', context)


class HomeView(View):

    def post(self, request):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            addr = form.cleaned_data['addr']
            text = f'Телефон: {phone}\n Имя: {name}\n Адрес: {addr}'
            try:
                send_message(text)
            except BadHeaderError:
                return render(request, 'invalid_form.html', context={'form': form})
            return redirect('/')


    def get(self, request):
        object_list = Partition.objects.all()
        lastworks = Product.objects.all()[:6]
        form = FeedBackForm()
        context = {
            'object_list': object_list, 'lastworks': lastworks, 'form': form
        }
        return render(request, 'index.html', context)


class ProductView(View):

    def post(self, request):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            addr = form.cleaned_data['addr']
            text = f'Телефон: {phone}\n Имя: {name}\n Адрес: {addr}'
            try:
                send_message(text)
            except BadHeaderError:
                return render(request, 'invalid_form.html', context={'form': form})
            return redirect('/')

    def get(self, request, slug2):
        product = Product.objects.get(slug=slug2)
        return render(request, 'product_detail.html', {'form': form, 'product': product})


class ProductsView(View):

    def get(self, request):
        object_list = Partition.objects.all()
        lastworks = Product.objects.all()[:6]
        form = FeedBackForm()
        context = {
            'object_list': object_list, 'lastworks': lastworks, 'form': form
        }
        return render(request, 'products.html', context)

# class FormView(View):
#     def post(self, request):
#         form = FeedBackForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             phone = form.cleaned_data['phone']
#             addr = form.cleaned_data['addr']
#             text = f'Телефон: {phone}\n Имя: {name}\n Адрес: {addr}'
#             try:
#                 send_message(text)
#             except BadHeaderError:
#                 return render(request, 'invalid_form.html', context={'form': form})
#             return redirect('/')
#
#     def get(self, request):
#         return render(request, 'index.html', {'form': form})
