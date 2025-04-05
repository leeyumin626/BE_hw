from django.urls import path
from .views import *

app_name  = 'posts'

urlpatterns = [
    path('', list, name='list'),
    path('create/', create , name='create'),
    path('detail/<int:id>/', detail, name='detail'),
    path('update/<int:id>/', update, name='update'),
    path('result/', result, name='result'),
    path('delete/<int:id>' ,delete ,name='delete'),
]