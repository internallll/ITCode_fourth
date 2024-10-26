from logging import Filter
from django import forms
from django.views.generic import ListView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, UpdateView
from django_filters.views import FilterView
from rest_framework import viewsets


from bas import filters
from bas.models import *
from bas import serializers

class BusParkAPI(viewsets.ModelViewSet):
    queryset = BusPark.objects.all()
    serializer_class = serializers.BusPark


class BusAPI(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = serializers.Bus

class BusParkList(FilterView):
    model = BusPark
    template_name = 'busPark_list.html'
    context_object_name = 'busPark'
    filterset_class = filters.BusParkFilter



class BusParkDetail(DetailView):
    model = BusPark
    template_name = 'busPark_detail.html'
    context_object_name = 'busPark'


class BusParkUpdate(UpdateView):
    model = BusPark
    template_name= 'busPark_form.html'
    fields = ['title', 'address', 'phone_number', 'year_found', 'description']

    def get_success_url(self):
        return reverse_lazy('park_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['busPark'] = self.object
        return context

class BusParkDelete(DeleteView):
    model = BusPark
    template_name = 'busPark_confirm_delete.html'
    success_url = reverse_lazy('park_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['busPark'] = self.object
        return context




class BusParkCreate(CreateView):
    model =BusPark
    template_name = 'busPark_create.html'
    success_url = reverse_lazy('park_list')

    def get_form_class(self):
        class BusParkForm(forms.ModelForm):
            class Meta:
                model = BusPark
                fields = ['title', 'address', 'phone_number']
        return BusParkForm
