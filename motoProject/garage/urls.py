from django.urls import path

from . import views

app_name = 'garage'
urlpatterns = [
    # ex: /garage/
    path('', views.index,name='index'),
    # ex: /garage/5/
    path('<int:motorcycle_id>/', views.description, name='description'),
]