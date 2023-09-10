from django.shortcuts import render
from django.views.generic import TemplateView
from portal.settings import *


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["hoge"] = EMAIL_HOST_USER
        context["hoge2"] = SECRET_KEY
        return context

# Create your views here.
