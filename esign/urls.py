from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name='home'),
    path("/embedded", views.embedded, name='embedded')
]