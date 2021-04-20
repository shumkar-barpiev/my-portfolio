from django.urls import path
from . import views


app_name = 'my portfolio'

urlpatterns = [
    path('', views.basepage, name='base'),
    path('<slug:post>/', views.post_single, name='post_single'),
]