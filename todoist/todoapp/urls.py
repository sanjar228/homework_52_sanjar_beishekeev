from django.urls import path
from .views import main, del_view

urlpatterns = [
    path('',main ), 
    path('delete/<int:pk>/', del_view)
]
