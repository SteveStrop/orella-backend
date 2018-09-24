from django.urls import path
from . import views

urlpatterns = [

    path(r'WebGrab/', views.WebGrab.as_view()),
]
