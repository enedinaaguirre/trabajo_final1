from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('carreras/<int:pk>', views.detalles, name='detalles-carrera'),
#    path('author/<int:pk>', views.author_detail, name='author-detail'),
]
