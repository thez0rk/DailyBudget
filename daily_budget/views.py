from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        return context





