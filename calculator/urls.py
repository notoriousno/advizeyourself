from django.urls import path

from . import views


urlpatterns = [
    path('retirement', views.calculate_retirement, name='retirement'),
]
