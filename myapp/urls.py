from django.urls import path
from . import views

urlpatterns = [
    path('',view.hello),
    path('about/',views.about)
]
