from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
# Create your views here.
from groups.models import Group,GroupMembers
from . import models
from django.shortcuts import get_object_or_404


class CreateGroup(LoginRequiredMixin,generic.CreateView):
    fields = ('name','description')
    model = Group
class SingleGroup(generic.DetailView):
    model = Group

class ListGroup(generic.ListView):
    model = Group

class JoinGroup(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get('slug'))

        try:
            GroupMembers.objects.create(user=self.request.user,group=group)
        except:
            messages.warning(self.request,'Warning already a member')
        else:
            messages.success(self.request,'You are now a member')

        return super().get(request,*args,**kwargs)

class LeaveGroup(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get('slug'))

        try:
            membership = models.GroupMembers.objects.filter(user=self.request.user,group__slug=kwargs.get('slug')).get()
        except:
            messages.warning(self.request,'You are not in this group')
        else:
            membership.delete()
            messages.success(self.request,'You have left the group')

        return super().get(request,*args,**kwargs)