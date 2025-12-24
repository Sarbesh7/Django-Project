

from django.urls import path
from .views import Home, Create, Delete, Update

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('create/', Create.as_view(), name='create'),
    path('delete/<int:id>/', Delete.as_view(), name='delete'),
    path('update/<int:id>/', Update.as_view(), name='update'),
]
