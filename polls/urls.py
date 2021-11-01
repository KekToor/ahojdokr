from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/<int:retez>', views.search, name='search'),
]