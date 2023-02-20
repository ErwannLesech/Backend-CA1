from django.urls import path

from . import views

app_name = 'garage'
urlpatterns = [
    # ex: /garage/
    path('', views.index,name='index'),
    # ex: /garage/create/
    path('create/', views.create, name='create'),
    # ex: /garage/5/
    path('<int:motorcycle_id>/', views.description, name='description'),
    # ex: /garage/5/delete/
    path('<int:motorcycle_id>/delete/', views.delete, name='delete'),
    # ex: /garage/5/update/
    path('<int:motorcycle_id>/update/', views.update, name='update'),
]