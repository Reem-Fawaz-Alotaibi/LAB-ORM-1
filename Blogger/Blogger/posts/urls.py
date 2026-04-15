from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_post, name='add_post'),
    path('<int:id>/', views.detail_post, name='detail_post'),
    path('<int:id>/update/', views.update_post, name='update_post'),
    path('<int:id>/delete/', views.delete_post, name='delete_post'),
]