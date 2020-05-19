from django.contrib import admin
from django.urls import path, include
from django.urls import re_path,include
from .views import  *
from .evalua09export import EV09EXP2


urlpatterns = [
    #path("", Listado_Estudiantes),
    path("", login),
    path("URL1", input_new),
    path("EV09", Vista_EVALUA_09),
    path("EV10", Vista_EVALUA_10),
    path("EV11", Vista_EVALUA_11),
    path("exito", vista_exito, name="url_exito"),
    path("listado", Listado_Estudiantes),
#    re_path("EST/(?P<pk>\d+)$", Detalle_Estudiantes, name='Detalle_Estudiantes'),
  # re_path(r'^EST/(?P<pk>\d+)$', Detalle_Estudiantes, name='Detalle_Estudiantes'),
    path ("estudiante/<Rut>/", Detalle_Estudiantes, name='Detalle_Estudiantes'),
    #path ("editar+Detalle_Estudiantes", Edit_EST, name= 'Editar_Estudiantes'),
    path ("delete/estudiante/<Rut>/", borrar),
    path("exportar1", export_users_xls, name ="exportar1"),

    path("Listado_E09", Listado_E09, name ="Listado_E09"),
    path("E09/<pk>/", Detalle_Estudiantes_E09),
    path ("delete/E09/<pk>/", borrar_E09),
    path("portada", portada, name = "menu"),
    #path('', welcome),
    #path('register', register),
    path('login/', login, name="login"),
    path('logout', logout),
    path("test/E09/<pk>/",EV09EXP2)
    #path('admin/', admin.site.urls),

]
