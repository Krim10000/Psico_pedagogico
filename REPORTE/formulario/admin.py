from django.contrib import admin

# Register your models here.
from .models import Modelo_Info_Per, Modelo_EVALUA_11, Modelo_EVALUA_10, Modelo_EVALUA_09
#from .models import Persona_TEST
from . forms import *

admin.site.register(Modelo_Info_Per)
#admin.site.register(Persona_TEST)
admin.site.register(Modelo_EVALUA_11)
admin.site.register(Modelo_EVALUA_10)
admin.site.register(Modelo_EVALUA_09)
