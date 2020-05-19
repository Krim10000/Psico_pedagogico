from django import forms
from .models import Modelo_Info_Per
#from .models import Persona_TEST
from .models import Modelo_EVALUA_11
from .models import Modelo_EVALUA_10
from .models import Modelo_EVALUA_09
#from .views import vista_exito

######################################
class Form1(forms.ModelForm):

    class Meta:
        model = Modelo_Info_Per
        fields = ("__all__")
        labels = {
            'Apellido_P':('Apellido paterno'),
            "Apellido_M": ('Apellido materno'),
            "Fecha_nac": ('Fecha de nacimiento'),
        }
        help_texts = {
            "Rut":("12345678-9"),
            'Fecha_nac': ('DD/MM/AAAA'),
        }
#Modelo
# Rut
# Nombres
# Apellido_P
# Apellido_M
# Fecha_nac
# Domicilio
# Observaciones
######################################
# class Form2(forms.ModelForm):
#
#     class Meta:
#         model = Persona_TEST
#         fields = ("__all__")
######################################
class Form_EVALUA_11(forms.ModelForm):

    class Meta:
        model = Modelo_EVALUA_11
        fields = ("__all__")
        labels = {
            'Rut':('Estudiante'),}
#####################################
class Form_EVALUA_10(forms.ModelForm):

    class Meta:
        model = Modelo_EVALUA_10
        fields = ("__all__")
        labels = {
            'Rut':('Estudiante'),
            }

#
# #PUNTAJE IIA1-IIA6 desagregado
# IIA_ACIERTO= models.IntegerField(default=0)
# IIA_ERROR= models.IntegerField(default=0)
# IIA_OMISION= models.IntegerField(default=0)
#
# #II RAZONAMIENTO B. ESPACIAL
# IIB1_ACIERTO= models.IntegerField(default=0)
# IIB1_ERROR= models.IntegerField(default=0)
# IIB1_OMISION= models.IntegerField(default=0)
#
# IIB2_ACIERTO= models.IntegerField(default=0)
# IIB2_ERROR= models.IntegerField(default=0)
# IIB2_OMISION= models.IntegerField(default=0)
# #
# #II RAZONAMIENTO C. DEDUCTIVO
# IIC1_ACIERTO= models.IntegerField(default=0)
# IIC1_ERROR= models.IntegerField(default=0)
# IIC1_OMISION= models.IntegerField(default=0)
#
# #PUNTAJE IIC2
# IIC2_ACIERTO= models.IntegerField(default=0)
# IIC2_ERROR= models.IntegerField(default=0)
# IIC2_OMISION= models.IntegerField(default=0)
#
# # IV LECTURA A COMPRENSION
# IVA_ACIERTO= models.IntegerField(default=0)
# IVA_ERROR= models.IntegerField(default=0)
# IVA_OMISION= models.IntegerField(default=0)
# #
# # IV LECTURA B EFICACIA
# IVB_ACIERTO= models.IntegerField(default=0)
# IVB_ERROR= models.IntegerField(default=0)
# IVB_OMISION= models.IntegerField(default=0)
# #
# # IV LECTURA C VELOCIDAD
# IVC_ACIERTO= models.IntegerField(default=0)
# IVC_ERROR= models.IntegerField(default=0)
# IVC_OMISION= models.IntegerField(default=0)
# #
# #
# # V ESCRITURA A. ORTOGRAFIA
# # PUNTAJE V.A
# VA_ACIERTO= models.IntegerField(default=0)
# VA_ERROR= models.IntegerField(default=0)
# VA_OMISION= models.IntegerField(default=0)
# # #ACIERTO	ERROR	OMISION
# #
# # V ESCRITURA B. EXP ESCRITA
# # PUNTAJE V.B
# # 1	"Composición escrita superior a lo que es propia del nivel escolar."
# # 2	"Composición escrita presenta pequeños errores, no relevantes al proceso de expresión."
# # 3	"Composición acorde al nivel escolar."
# # 4	"Composición inferior a lo esperado acorde al nivel escolar."
# # 5	"Composición con abundantes errores, no logra expresarse."
# # 0	"Vacio"
# V = models.CharField(max_length= 1, choices=ITEM_VB.choices, default=ITEM_VB.VB_1)
# #
# # PUNTAJE VI.A
# #VI APREND MATEMATICOS A CAL&NUM
# #ACIERTO	ERROR	OMISION
# VIA_ACIERTO= models.IntegerField(default=0)
# VIA_ERROR= models.IntegerField(default=0)
# VIA_OMISION= models.IntegerField(default=0)
# #PUNTAJE VI.B
# #VI APREND MATEMATICOS B RESOLUC
#
# VIB_ACIERTO= models.IntegerField(default=0)
# VIB_ERROR= models.IntegerField(default=0)
# VIB_OMISION= models.IntegerField(default=0)



######################################
from django.urls import reverse
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset, ButtonHolder, HTML, Column, Field
from crispy_forms.bootstrap import StrictButton

#class Row(Div):
#    css_class = 'row-fluid'

class Form_EVALUA_09(forms.ModelForm):
    Colegio = forms.CharField(widget=forms.TextInput(attrs={'size':100})),


# tab agregar al final del formulario
    def __init__(self, *args, **kwargs):
       super(Form_EVALUA_09, self).__init__(*args, **kwargs)# FORM  nombre de la forma
       self.helper = FormHelper()
       # self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
       # self.helper.form_method = 'POST'

       #nuevo input
       #self.helper.add_input(Submit('submit', 'Submit', ))
       # self.helper.form_method = 'POST'
       # self.helper.form_id = 'id-personal-data-form'
       # self.helper.form_method = 'post'
       # self.helper.form_action = 'exito'
      # self.helper.add_input(Submit('submit', 'Submit'))
       #self.helper.form_class = 'form-horizontal'
      # self.helper.form_class = 'form-inline'
       self.helper.field_template = 'bootstrap3/layout/inline_field.html'
       self.helper.layout = Layout(
                ######## codigo para columnas y columna 1

                HTML(""" <center> """),#center I1
                Fieldset("",  #Seccion
                HTML(""" <center> DATOS GENERALES </center> """),#Titulo I2-F2
                HTML("""  <p></p> """), #espacio

                Field("Rut","Semestre","Año","Colegio", "Curso","Escolaridad","Fecha","Evaluador" )),

                HTML("""  <p></p> """), #espacio
                HTML(""" </center> """),#center F2
                #/////////////////////////////////////

                HTML("""
                        <html>
                        <head>
                        <meta name="viewport" content="width=device-width, initial-scale=1">
                        <style>
                        * {
                          box-sizing: border-box;
                        }

                        /* Create two equal columns that floats next to each other */
                        .column {
                          float: left;
                          width: 50%;}

                        /* Clear floats after the columns */
                        .row:after {
                          content: "";
                          display: table;
                          clear: both;}
                        </style>
                        </head>
                        <body>

                            <div class="row">
                          <div class="column" >
                                        """),

                HTML(""" <center> """),#center
                Fieldset("",#Seccion
                HTML(""" <center> I ATENCIÓN CONCENTRACIÓN </center> """),#Titulo
                HTML("""  <p></p> """),
                    Field("I_ACIERTO","I_ERROR","I_OMISION")),#Listo
                HTML("""  <p></p> """), #espacio


                Fieldset("",  #Seccion
                HTML(""" <center> II RAZONAMIENTO </center> """),#Titulo
                HTML("""  <p></p> """), #espacio
                Fieldset("II RAZONAMIENTO A. INDUCTIVO PARTE 1",#subtitulo
                    Field("IIA1_ACIERTO","IIA1_ERROR","IIA1_OMISION")),#Listo

                Fieldset("II RAZONAMIENTO A. INDUCTIVO PARTE 2",#subtitulo
                    Field("IIA2_ACIERTO","IIA2_ERROR","IIA2_OMISION")),#Listo

                Fieldset("II RAZONAMIENTO A. INDUCTIVO PARTE 3",#subtitulo
                    Field("IIA3_ACIERTO","IIA3_ERROR","IIA3_OMISION")),#Listo

                Fieldset("II RAZONAMIENTO A. INDUCTIVO PARTE 4",#subtitulo
                    Field("IIA4_ACIERTO","IIA4_ERROR","IIA4_OMISION")),#Listo

                Fieldset("II RAZONAMIENTO A. INDUCTIVO PARTE 5",#subtitulo
                    Field("IIA5_ACIERTO","IIA5_ERROR","IIA5_OMISION")),#Listo

                Fieldset("II RAZONAMIENTO A. INDUCTIVO PARTE 6",#subtitulo
                    Field("IIA6_ACIERTO","IIA6_ERROR","IIA6_OMISION")),#Listo
                Fieldset("II RAZONAMIENTO B. ESPACIAL PARTE 1: Items 1 al 7",
                    Field("IIB1_ACIERTO","IIB1_ERROR","IIB1_OMISION")),#Listo
                Fieldset("II RAZONAMIENTO B. ESPACIAL PARTE 2: Items 8 al 9",
                    Field("IIB2_ACIERTO","IIB2_ERROR","IIB2_OMISION")),#Listo
                Fieldset("II RAZONAMIENTO B. ESPACIAL PARTE 3: Items 10 al 20",
                    Field("IIB3_ACIERTO","IIB3_ERROR","IIB3_OMISION")),#Listo
                Fieldset("II RAZONAMIENTO C. DEDUCTIVO PARTE 1",
                    Field("IIC1_ACIERTO","IIC1_ERROR","IIC1_OMISION")),#Listo
                Fieldset("II RAZONAMIENTO C. DEDUCTIVO PARTE 2",
                    Field("IIC2_ACIERTO","IIC2_ERROR","IIC2_OMISION")),),#Listo


                HTML("""  <p></p> """), #espacio
                HTML("""  </div> """), #fin columna uno
                HTML(""" </center> """),#center

            #////////////////////////////
                HTML(""" <center> """),#center
                HTML("""   <div class="column"  """), #inicio columna dos

                Fieldset("",#Seccion
                Fieldset("",#Seccion
                HTML(""" <center> IV LECTURA </center> """),#Titulo
                HTML("""  <p></p> """),
                Fieldset("IV LECTURA A COMPRENSION",
                    Field("IVA_ACIERTO","IVA_ERROR","IVA_OMISION")),
                Fieldset("IV LECTURA B EFICACIA",
                    Field("IVB_ACIERTO","IVB_ERROR","IVB_OMISION")),
                Fieldset("IV LECTURA C VELOCIDAD",
                    Field("IVC_ACIERTO","IVC_ERROR","IVC_OMISION"))),
                HTML("""  <p></p> """), #espacio


                Fieldset("",#Seccion
                HTML(""" <center> V ESCRITURA </center> """),#Titulo
                HTML("""  <p></p> """),
                Fieldset("V ESCRITURA A. ORTOGRAFIA",
                    Field("VA_ACIERTO","VA_ERROR","VA_OMISION")),
                HTML("""  <p></p> """),
                Fieldset("V ESCRITURA B. EXP ESCRITA",
                    Field("V")),
                HTML("""  <p></p> """)), #espacio


                Fieldset("",#Seccion
                HTML(""" <center> VI APRENDIZAJE MATEMATICOS </center> """),#Titulo
                HTML("""  <p></p> """),
                Fieldset("VI APREND MATEMATICOS A CAL&NUM",
                    Field("VIA_ACIERTO","VIA_ERROR","VIA_OMISION")),
                Fieldset("VI APREND MATEMATICOS B RESOLUC",
                    Field("VIB_ACIERTO","VIB_ERROR","VIB_OMISION"))),
                HTML("""  <p></p> """)), #espacio


                HTML(""" </center> """),#center



            #fin codigo columnas
            HTML("""  </div>
                        </div>

                        </body>
                        </html>
                          """),
HTML(""" <center> """),#center
ButtonHolder(Submit('Save', 'Guardar', css_class='button white'),),# Botton
HTML(""" </center> """),#center

 )# FIN LAYOUT



#Row(
            #     Column('email', css_class='form-group col-md-6 mb-0'),
            #     Column('password', css_class='form-group col-md-6 mb-0'),
            #     css_class='form-row'
            # ),
            # 'address_1',
            # 'address_2',
            # Row(
            #     Column('city', css_class='form-group col-md-6 mb-0'),
            #     Column('state', css_class='form-group col-md-4 mb-0'),
            #     Column('zip_code', css_class='form-group col-md-2 mb-0'),
            #     css_class='form-row'
            # ),
            # 'check_me_out',

            # this is how to add the submit button to your form and since it is the last item in this tuple, it will be rendered last in the HTML
#Submit('submit', u'Submit', css_class='btn btn-success'))
        #             Div('CAMPO', title="label"),),
        #    Fieldset('Contact data', 'email', 'phone', style="color: brown;"),
        #    InlineRadios('color'),
        #    TabHolder(Tab('Address', 'address'),
        #              Tab('More Info', 'more_info')))
        #              Tab('Titulo', 'campo')
        # self.helper.layout = Layout(
        #     Fieldset('tITULO', 'CAMPO1', 'CAMPO2',) )
        # I_ACIERTO= models.IntegerField(default=0)
        # I_ERROR= models.IntegerField(default=0)
        # I_OMISION= models.IntegerField(default=0)
        #
        # #PUNTAJE IIA1-IIA6 desagregado
        # IIA_ACIERTO= models.IntegerField(default=0)
        # IIA_ERROR= models.IntegerField(default=0)
        # IIA_OMISION= models.IntegerField(default=0)
        #
        # #II RAZONAMIENTO B. ESPACIAL
        # IIB1_ACIERTO= models.IntegerField(default=0)
        # IIB1_ERROR= models.IntegerField(default=0)
        # IIB1_OMISION= models.IntegerField(default=0)
        #
        # IIB2_ACIERTO= models.IntegerField(default=0)
        # IIB2_ERROR= models.IntegerField(default=0)
        # IIB2_OMISION= models.IntegerField(default=0)
        # #
        # #II RAZONAMIENTO C. DEDUCTIVO
        # IIC1_ACIERTO= models.IntegerField(default=0)
        # IIC1_ERROR= models.IntegerField(default=0)
        # IIC1_OMISION= models.IntegerField(default=0)
        #
        # #PUNTAJE IIC2
        # IIC2_ACIERTO= models.IntegerField(default=0)
        # IIC2_ERROR= models.IntegerField(default=0)
        # IIC2_OMISION= models.IntegerField(default=0)
        #
        # # IV LECTURA A COMPRENSION
        # # IIB1_ACIERTO= models.IntegerField()
        # IVA_ACIERTO= models.IntegerField(default=0)
        # IVA_ERROR= models.IntegerField(default=0)
        # IVA_OMISION= models.IntegerField(default=0)
        # #
        # # IV LECTURA B EFICACIA
        # IVB_ACIERTO= models.IntegerField(default=0)
        # IVB_ERROR= models.IntegerField(default=0)
        # IVB_OMISION= models.IntegerField(default=0)
        # #
        # # IV LECTURA C VELOCIDAD
        # IVC_ACIERTO= models.IntegerField(default=0)
        # IVC_ERROR= models.IntegerField(default=0)
        # IVC_OMISION= models.IntegerField(default=0)
        # #
        # #
        # # V ESCRITURA A. ORTOGRAFIA
        # # PUNTAJE V.A
        # VA_ACIERTO= models.IntegerField(default=0)
        # VA_ERROR= models.IntegerField(default=0)
        # VA_OMISION= models.IntegerField(default=0)
        # # #ACIERTO	ERROR	OMISION
        # #
        # # V ESCRITURA B. EXP ESCRITA
        # # PUNTAJE V.B
        # # 1	"Composición escrita superior a lo que es propia del nivel escolar."
        # # 2	"Composición escrita presenta pequeños errores, no relevantes al proceso de expresión."
        # # 3	"Composición acorde al nivel escolar."
        # # 4	"Composición inferior a lo esperado acorde al nivel escolar."
        # # 5	"Composición con abundantes errores, no logra expresarse."
        # # 0	"Vacio"
        # V = models.CharField(max_length= 1, choices=ITEM_VB.choices, default=ITEM_VB.VB_1)
        # #
        # # PUNTAJE VI.A
        # #VI APREND MATEMATICOS A CAL&NUM
        # #ACIERTO	ERROR	OMISION
        # VIA_ACIERTO= models.IntegerField(default=0)
        # VIA_ERROR= models.IntegerField(default=0)
        # VIA_OMISION= models.IntegerField(default=0)
        # #PUNTAJE VI.B
        # #VI APREND MATEMATICOS B RESOLUC
        #
        # VIB_ACIERTO= models.IntegerField(default=0)
        # VIB_ERROR= models.IntegerField(default=0)
        # VIB_OMISION= models.IntegerField(default=0)
        #
        #
        #
        #
        #

######################################

    class Meta:
        model = Modelo_EVALUA_09
        fields = ("__all__")
        labels = {
            'Rut':('Estudiante'),
            "I_ACIERTO":("Aciertos"),
            "I_ERROR":("Errores"),
            "I_OMISION":("Omisiones"),
            "IIA1_ACIERTO":("Aciertos"),
            "IIA1_ERROR":("Errores"),
            "IIA1_OMISION":("Omisiones"),
            "IIA2_ACIERTO":("Aciertos"),
            "IIA2_ERROR":("Errores"),
            "IIA2_OMISION":("Omisiones"),
            "IIA3_ACIERTO":("Aciertos"),
            "IIA3_ERROR":("Errores"),
            "IIA3_OMISION":("Omisiones"),
            "IIA4_ACIERTO":("Aciertos"),
            "IIA4_ERROR":("Errores"),
            "IIA4_OMISION":("Omisiones"),
            "IIA5_ACIERTO":("Aciertos"),
            "IIA5_ERROR":("Errores"),
            "IIA5_OMISION":("Omisiones"),
            "IIA6_ACIERTO":("Aciertos"),
            "IIA6_ERROR":("Errores"),
            "IIA6_OMISION":("Omisiones"),
            "IIB1_ACIERTO":("Aciertos"),
            "IIB1_ERROR":("Errores"),
            "IIB1_OMISION":("Omisiones"),
            "IIB2_ACIERTO":("Aciertos"),
            "IIB2_ERROR":("Errores"),
            "IIB2_OMISION":("Omisiones"),
            "IIB3_ACIERTO":("Aciertos"),
            "IIB3_ERROR":("Errores"),
            "IIB3_OMISION":("Omisiones"),
            "IIC1_ACIERTO":("Aciertos"),
            "IIC1_ERROR":("Errores"),
            "IIC1_OMISION":("Omisiones"),
            "IIC2_ACIERTO":("Aciertos"),
            "IIC2_ERROR":("Errores"),
            "IIC2_OMISION":("Omisiones"),
            "IVA_ACIERTO":("Aciertos"),
            "IVA_ERROR":("Errores"),
            "IVA_OMISION":("Omisiones"),
            "IVB_ACIERTO":("Aciertos"),
            "IVB_ERROR":("Errores"),
            "IVB_OMISION":("Omisiones"),
            "IVC_ACIERTO":("Aciertos"),
            "IVC_ERROR":("Errores"),
            "IVC_OMISION":("Omisiones"),
            "VA_ACIERTO":("Aciertos"),
            "VA_ERROR":("Errores"),
            "VA_OMISION":("Omisiones"),
            "V":("Expresión Escrita"),
            "VIA_ACIERTO":("Aciertos"),
            "VIA_ERROR":("Errores"),
            "VIA_OMISION":("Omisiones"),
            "VIB_ACIERTO":("Aciertos"),
            "VIB_ERROR":("Errores"),
            "VIB_OMISION":("Omisiones"),

            }
        widgets = { 'Colegio': forms.Textarea(attrs={"rows":1 ,"cols":50}),
                    'Escolaridad': forms.Textarea(attrs={"rows":1 ,"cols":50}),
                    'Evaluador': forms.Textarea(attrs={"rows":1 ,"cols":50}),
                    }
