from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('about/', about),
    path('courses/', courses),
    path('contact/',contact),
    path('add/<int:a>/<int:b>',add),
    path('courses/<slug:slug>/',one_page)
]