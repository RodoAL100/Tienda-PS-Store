from django.urls import path
from producto import views
{# aqui iran las conecciones#}
urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('productos/', views.listado_productos, name="productos"),
    path('productos/crear', views.crear, name="crear"),
    path('productos/editar/<int:id>', views.editar_producto, name="editar_producto"),
    path('productos/eliminar/<int:id>', views.eliminar_producto, name="eliminar_producto"),
    path('productos/acerca_de/', views.acerca_de, name='acerca_de'),
]
