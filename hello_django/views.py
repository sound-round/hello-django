from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from django.urls import reverse


def index(request):
    url = reverse('calc', kwargs={'a': 40, 'b': 2})
    return redirect(url)

    # template_name = 'index.html'
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['who'] = 'World'
    #     return context
