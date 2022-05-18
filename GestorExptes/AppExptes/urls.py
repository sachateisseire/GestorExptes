from django.urls import path
from AppExptes.views import saluda2, saluda3


urlpatterns = [
    path('', saluda2),
    path('test/', saluda3),
]