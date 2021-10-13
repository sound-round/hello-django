from django.urls import path
from hello_django.calc.views import IndexView


urlpatterns = [
    path(
        '<int:a>/<int:b>',
        IndexView.as_view(),
        name='calc'
    ),
]