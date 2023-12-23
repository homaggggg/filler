# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from mysite.docgurnal.models import *

from mysite.home.models import Profile


@login_required(login_url="/login/")
def index(request):
    context = {}

    gurnal_list = gurnal.objects.filter(user=request.user)[:5]
    docs_count = gurnal.objects.filter(user=request.user).count()

    context['col1name'] = gurnal._meta.get_field("created_at").verbose_name
    context['col2name'] = gurnal._meta.get_field("updated_at").verbose_name
    context['collastname'] = 'Сервисы'
    context['gurnal_list'] = gurnal_list
    context['gurnals_count'] = docs_count

    return render(request, 'home/index.html', context)


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


def static_html(request, template_name):
    return render(request, f"home/{template_name}.html")


from django.views.generic.detail import DetailView
class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'home/profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context



class CreateProfilePageView(CreateView):
    model = Profile

    template_name = 'home/create_profile.html'
    fields = ['profile_pic', 'bio', 'facebook', 'twitter', 'instagram']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('user_profile')
    # success_url = '/home/profile/'