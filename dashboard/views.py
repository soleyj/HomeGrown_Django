from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, DeleteView,
                                  UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth.models import Permission, User
from django.http import HttpResponseRedirect

def myview(request):
    return HttpResponseRedirect("/dashboard/")


class DashboardView(LoginRequiredMixin,TemplateView):
    # Just set this Class Object Attribute to the template page.
    template_name = 'dashboard/home.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        return context

class PropsView(LoginRequiredMixin,PermissionRequiredMixin,TemplateView):
    # Just set this Class Object Attribute to the template page.
    template_name = 'dashboard/props.html'
    permission_required = "auth.superuser"
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        return context

class AutoPistasView(LoginRequiredMixin,PermissionRequiredMixin,TemplateView):
    # Just set this Class Object Attribute to the template page.
    template_name = 'dashboard/pistas.html'
    permission_required = "auth.superuser"
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        return context

class GameConfigView(LoginRequiredMixin,PermissionRequiredMixin,TemplateView):
    # Just set this Class Object Attribute to the template page.
    template_name = 'dashboard/game_config.html'
    permission_required = "auth.superuser"
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        return context