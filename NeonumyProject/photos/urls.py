from django.urls import path
from . import views
urlpatterns = [
    path('list/', views.list_photo, name='image_list'),
    path('upload/', views.image_upload, name='image_upload'),
    path('<int:pk>/', views.image_detail, name='image_detail'),
    path('<int:pk>/delete/', views.image_delete, name='image_delete'),
]
