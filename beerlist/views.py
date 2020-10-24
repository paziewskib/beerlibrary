from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Brewery, Beer


class IndexView(generic.ListView):
    template_name = 'beerlist/index.html'
    context_object_name = 'breweries_list'

    def get_queryset(self):
        return Brewery.objects.all()


class DetailView(generic.DetailView):
    model = Brewery
    template_name = 'beerlist/detail.html'


class BreweryCreate(CreateView):
    model = Brewery
    fields = ['brewery_name', 'hometown', 'country', 'brewery_logo']


class BreweryUpdate(UpdateView):
    model = Brewery
    fields = ['brewery_name', 'hometown', 'country', 'brewery_logo']


class BreweryDelete(DeleteView):
    model = Brewery
    success_url = reverse_lazy('beerlist:index')
