from .models import Accounts
from .forms import PlantForm
from apps.plants.models import PlantedTree
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

class Dashboard(LoginRequiredMixin, ListView):
    template_name = 'accounts/dashboard.html'
    model = PlantedTree

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['planted_trees'] = PlantedTree.objects.filter(user=self.request.user)
        return context


class TreeView(LoginRequiredMixin, DetailView):
    model = PlantedTree

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tree = get_object_or_404(PlantedTree, pk=self.kwargs['pk'])

        if not tree.user == self.request.user:
            raise PermissionDenied

        context['planted_tree'] = tree
        return context


class PlantTree(LoginRequiredMixin, CreateView):
    model = PlantedTree
    fields = ['tree', 'latitude', 'longitude',]
    template_name = 'plants/plantedtree_form.html'
    success_url = '/'

    def form_valid(self, form):
        tree = form.save(commit=False)
        tree.user = self.request.user
        return super(PlantTree, self).form_valid(form)


class PlantsAccount(ListView):
    model = PlantedTree

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        accounts = Accounts.objects.filter(users=self.request.user, active=True)
        users = []
        for account in accounts:

            for user in account.users.all():
                if user != self.request.user:
                    users.append(user.email)

        users.append(self.request.user.email)
        print(users)
        context['planted_tree_account'] = PlantedTree.objects.filter(user__email__in=users)
        return context
