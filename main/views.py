from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect

from main.utils import reverse_lazy
from main.models import Hacker, Comment, Enterprise, Service
from main.forms import HackerForm, LoginForm


class HackerMixin(object):
    model = Hacker
    form_class = HackerForm
    success_url = reverse_lazy('add_hacker')


class HackerCreateView(HackerMixin, CreateView):
    pass


class HackerListView(HackerMixin, ListView):
    pass


class EnterpriseMixin(object):
    model = Enterprise
    success_url = reverse_lazy('add_enterprise')


class EnterpriseCreateView(EnterpriseMixin, CreateView):
    pass


class EnterpriseListView(EnterpriseMixin, ListView):
    pass


class ServiceCreateView(CreateView):
    model = Service
    success_url = reverse_lazy('add_service')


def timeline_services(request, hacker_id):
    hacker_reputation = Hacker.objects.get(pk=hacker_id).reputation
    services = Service.objects.filter(reputation__lte=hacker_reputation)
    return render_to_response('main/timeline_services.html', {
        'services': services,
    }, RequestContext(request))


def service(request, service_id):
    serv = Service.objects.get(pk=service_id)
    return render_to_response('main/service.html', {
        'service': serv,
    }, RequestContext(request))


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        redirect("list_hackers")
    return render_to_response('main/login.html', RequestContext(request, {
        'form': form,
    }))


add_hacker = HackerCreateView.as_view()
list_hackers = HackerListView.as_view()
add_enterprise = EnterpriseCreateView.as_view()
list_enterprise = EnterpriseListView.as_view()
add_service = ServiceCreateView.as_view()
