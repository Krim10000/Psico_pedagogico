from django.shortcuts import render
from .forms import Form1
from .forms import Form_EVALUA_09
from .forms import Form_EVALUA_10
from .forms import Form_EVALUA_11
from .models import Modelo_Info_Per
from .models import *
from datetime import date
from datetime import datetime
hoy = date.today()




from django.contrib.auth.decorators import login_required

#def input_new(request):
#    form = Form1()
#    return render (request, "form.html", {"form": form})
#https://www.hektorprofe.net/tutorial/django-sistema-registro-login-logout
########################################################
from django.shortcuts import render, redirect

def welcome(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "portada.html")
    # En otro caso redireccionamos al login
    return redirect('login')
########################################################
# def register(request):
#     return render(request, "users/register.html")
########################################################
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/portada')

    # Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})


########################################################
from django.contrib.auth import logout as do_logout
def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')
################################################################################
def portada(request):
    return render (request, "portada.html")

################################################################################
@login_required
#@permission_required( raise_exception=True)
def input_new(request):

    submitted= False
    if request.method == "POST":
        titulo= "Nuevo estudiante"
        form = Form1(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            #return HttpResponseRedirect('/thanks/')
            return render(request, "exito.html")#, pk=post.pk)
    else:
        form = Form1()
        titulo= "Nuevo estudiante"
        if submitted in request.GET:
            submitted = True

    return render(request, 'form3.html', {'form': form, "submitted" : submitted, "titulo" : titulo})

################################################################################
@login_required
def vista_exito(request):
    return render(request, "exito.html")
################################################################################
@login_required
def portada(request):

    #Mayuscula para la primera letra y el resto en minuscula
    usuario = request.user
    usuario = str(usuario)
    usuario=usuario.lower()
    Resto = usuario[1:]
    Mayuscula =usuario[0].upper()
    usuario = Mayuscula + Resto

    # usuario = usuario.upper(0)



    return render(request, "portada.html", {'usuario': usuario})
################################################################################
@login_required
def Vista_EVALUA_11(request):
    titulo= "Evalua 11"
    submitted= False
    if request.method == "POST":
        form = Form_EVALUA_11(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            #return HttpResponseRedirect('/thanks/')
            return render(request, "exito.html")#, pk=post.pk)
    else:
        form = Form_EVALUA_11()
        if submitted in request.GET:
            submitted = True

    return render(request, 'form.html', {'form': form, "submitted" : submitted, "titulo" : titulo})
################################################################################
@login_required
def Vista_EVALUA_10(request):
    titulo= "Evalua 10"
    submitted= False
    if request.method == "POST":
        form = Form_EVALUA_10(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            #return HttpResponseRedirect('/thanks/')
            return render(request, "exito.html")#, pk=post.pk)
    else:
        form = Form_EVALUA_10()
        if submitted in request.GET:
            submitted = True

    return render(request, 'form.html', {'form': form, "submitted" : submitted, "titulo" : titulo})
################################################################################
@login_required
def Vista_EVALUA_09(request):
    titulo= "Evalua 09"
    submitted= False
    if request.method == "POST":
        form = Form_EVALUA_09(request.POST)
        if form.is_valid():
            mau = form.save(commit=True)
            #form.save()
            mau.save()
            #return HttpResponseRedirect('/thanks/')
            return render(request, "exito.html")#, pk=post.pk)
    else:
        form = Form_EVALUA_09()
        if submitted in request.GET:
           submitted = True

    #return render(request, 'form.html', {'form': form, "titulo" : titulo})
    return render(request, 'form.html', {'form': form, "submitted" : submitted, "titulo" : titulo})

################################################################################
@login_required
def Listado_Estudiantes(request):

    estu = Modelo_Info_Per.objects.all().order_by("-Rut")
    context_object_name = 'estudiante'



    if request.POST.get('edad'):
        Rut = (request.POST.get('Rut'))
        personas = Modelo_Info_Per.objects.all().filter(Rut=Rut)

    return render(request, 'listado.html', {'estu': estu, "Rut" :Rut })


################################################################################
################################################################################
################################################################################
@login_required
def Detalle_Estudiantes(request, Rut):

    EST=Modelo_Info_Per.objects.get(Rut=Rut)
    form = Form1(instance=EST)
    if request.method == "POST":
        form = Form1(request.POST, instance=EST)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, "exito.html")

    return render(request,'Detalle_EST.html',{'form':form,})






################################################################################
@login_required
def borrar(request, Rut):#en proceso

    EST=Modelo_Info_Per.objects.get(Rut=Rut)
    form = Form1(instance=EST)

    # Recuperamos la instancia de la persona y la borramos
    EST.delete()

    # Después redireccionamos de nuevo a la lista
    return render(request, "exito.html")
#
# def borrar_E09(request, pk):#Listo
#
#     test=Modelo_EVALUA_09.objects.get(pk=pk)
#     form = Form_EVALUA_09(instance=test)
#
#     # Recuperamos la instancia de la persona y la borramos
#     test.delete()

    # Después redireccionamos de nuevo a la lista
    return render(request, "exito.html")




################################################################################

import xlwt

from django.http import HttpResponse
from django.contrib.auth.models import User

@login_required
def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Estudiantes.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Estudiantes')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Rut', 'Nombres', 'Apellido paterno', 'Apellido materno', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
# Modelo_Info_Per.objects
# Rut
# Nombres
# Apellido_P
# Apellido_M
# Fecha_nac
# Domicilio
# Observaciones

    rows = Modelo_Info_Per.objects.all().values_list('Rut', 'Nombres', 'Apellido_P', 'Apellido_M')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response



################################################################################
# class Modelo_EVALUA_09(models.Model):
#     Rut = models.ForeignKey(Modelo_Info_Per,on_delete=models.DO_NOTHING, to_field ="Rut")
#     Semestre = models.IntegerField( default = semestre)
#     Año = models.IntegerField(default=
@login_required
def Listado_Estudiantes(request):

    estu = Modelo_Info_Per.objects.all().order_by("-Rut")
    context_object_name = 'estudiante'

    return render(request, 'listado.html', {'estu': estu})
################################################################################
@login_required
def Listado_E09(request):
    titulo = "Evalua 09"
    gato = Modelo_EVALUA_09.objects.all().order_by("-Año")
    context_object_name = 'E09'



    return render(request, 'listado_test.html', {'gato': gato, "titulo":titulo })
################################################################################

@login_required
def Detalle_Estudiantes_E09(request, pk):
    titulo = "Evalua 09"
    test = Modelo_EVALUA_09.objects.get(pk=pk)
    form = Form_EVALUA_09(instance=test)


    if request.method == "POST":
        form = Form_EVALUA_09(request.POST, instance=test)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, "exito.html")
    return render(request,'Detalle_EST.html',{'form':form, "titulo":titulo} )

################################################################################
################################################################################

@login_required
def borrar_E09(request, pk):#Listo

    test=Modelo_EVALUA_09.objects.get(pk=pk)
    form = Form_EVALUA_09(instance=test)

    # Recuperamos la instancia de la persona y la borramos
    test.delete()

    # Después redireccionamos de nuevo a la lista
    return render(request, "exito.html")
#############################################################################

@login_required
def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')


    ##filename = str(Año) + str(Semestre) +str(Rut) + ".xls"

    response['Content-Disposition'] = 'attachment; filename="Estudiantes.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Estudiantes')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Rut', 'Nombres', 'Apellido paterno', 'Apellido materno', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
# Modelo_Info_Per.objects
# Rut
# Nombres
# Apellido_P
# Apellido_M
# Fecha_nac
# Domicilio
# Observaciones

    rows = Modelo_Info_Per.objects.all().values_list('Rut', 'Nombres', 'Apellido_P', 'Apellido_M')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
            #ws.write(fila , columna, contenido, font_style)




    wb.save(response)
    return response
