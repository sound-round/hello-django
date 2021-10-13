from django.http import HttpResponse
from django.views import View


class IndexView(View):

    def get(self, request, *args, **kwargs):
        a = kwargs['a']
        b = kwargs['b']
        res = a + b
        return HttpResponse(f'{a} + {b} = {res}')