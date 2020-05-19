from django.db import models
from datetime import datetime

class Modelo_Info_Per(models.Model):
    Rut=models.CharField(max_length=10, unique= True)
    Nombres =models.CharField(max_length=50)
    Apellido_P =models.CharField(max_length=50,) #label= "Apellido paterno"
    Apellido_M =models.CharField(max_length=50, null=True, blank=True)
    Fecha_nac = models.DateField()
    Domicilio =models.CharField(max_length=50, null=True, blank=True)
    Observaciones =models.TextField(blank = True, null=True)

    class Meta:
        ordering = ["Apellido_P"]
 ###esto es esencial para los modelos y como se muestran
    def __str__(self):
        return '%s %s %s, %s' % (self.Apellido_P, self.Apellido_M, self.Nombres, self.Rut)

    def get_absolute_url(self):
        return f"/estudiante/{self.Rut }/"
#############################################################################################
# class  TIPO_DE_TEST(models.TextChoices):
#     EVALUA_11 = "E11","Evalua 11"
#     EVALUA_10 = "E10","Evalua 10"
#     EVALUA_09 = "E09","Evalua 09"
#     EVALUA_08 = "E08","Evalua 08"
#     EVALUA_07 = "E07","Evalua 07"
#############################################################################################
# class Persona_TEST(models.Model):
#     Rut = models.ForeignKey(Modelo_Info_Per,on_delete=models.CASCADE, to_field ="Rut")
#     Test = models.CharField(max_length= 4,
#                             choices=TIPO_DE_TEST.choices,
#                             default=TIPO_DE_TEST.EVALUA_09,
#                             )
#     Semestre = models.IntegerField()
#
#     Año = models.IntegerField()
#
#     class Meta:
#         ordering = ["Año"]
#
#     def __str__(self):
#         return '%s-%s %s %s' % (self.Año, self.Semestre, self.Test,  self.Rut, )
#############################################################################################
class Modelo_EVALUA_11(models.Model):

    Rut = models.ForeignKey(Modelo_Info_Per,on_delete= models.DO_NOTHING, to_field ="Rut")
    Semestre = models.IntegerField()
    Año = models.IntegerField()

    Pregunta_1= models.IntegerField()
    Pregunta_2= models.IntegerField()
    Pregunta_3= models.IntegerField()


    class Meta:
            ordering = ["Año"]

    def __str__(self):
        return '%s-%s %s ' % (self.Año, self.Semestre, self.Rut, )
############################################
class Modelo_EVALUA_10(models.Model):

    Rut = models.ForeignKey(Modelo_Info_Per,on_delete=models.DO_NOTHING, to_field ="Rut")
    Semestre = models.IntegerField()
    Año = models.IntegerField()

    Pregunta_1= models.IntegerField()
    Pregunta_2= models.IntegerField()
    Pregunta_3= models.IntegerField()


    class Meta:
            ordering = ["Año"]

    def __str__(self):
        return '%s-%s %s ' % (self.Año, self.Semestre, self.Rut, )
#############################################
class  ITEM_VB(models.TextChoices):
    VB_1= "1","Composición escrita superior a lo que es propia del nivel escolar."
    VB_2= "2","Composición escrita presenta pequeños errores, no relevantes al proceso de expresión."
    VB_3= "3","Composición acorde al nivel escolar."
    VB_4= "4","Composición inferior a lo esperado acorde al nivel escolar."
    VB_5= "5","Composición con abundantes errores, no logra expresarse."

#     EVALUA_11 = "E11","Evalua 11"
#     EVALUA_10 = "E10","Evalua 10"
#     EVALUA_09 = "E09","Evalua 09"
#     EVALUA_08 = "E08","Evalua 08"
#     EVALUA_07 = "E07","Evalua 07"

def semestre():
    M =datetime.now().month
    if M <= 6:
        S=1
    else:
        S=2
    return S


class Modelo_EVALUA_09(models.Model):
    Rut = models.ForeignKey(Modelo_Info_Per,on_delete=models.DO_NOTHING, to_field ="Rut")
    Semestre = models.IntegerField( default = semestre)
    Año = models.IntegerField(default= datetime.now().year )
    Colegio = models.TextField(max_length= 150, default = "Colegio Técnico Profesional República Argentina")
    Curso=models.CharField(max_length=3)
    Escolaridad=models.TextField(max_length= 250)
    Fecha= models.DateField(default=datetime.now)
    Evaluador= models.TextField(max_length= 100, default= "Carlos Diego Riquelme González")
    #I ATENCION CONCENTRACION
    I_ACIERTO= models.IntegerField(default=0)
    I_ERROR= models.IntegerField(default=0)
    I_OMISION= models.IntegerField(default=0)

    #PUNTAJE IIA1-IIA6 desagregado
    IIA1_ACIERTO= models.IntegerField(default=0)
    IIA1_ERROR= models.IntegerField(default=0)
    IIA1_OMISION= models.IntegerField(default=0)

    IIA2_ACIERTO= models.IntegerField(default=0)
    IIA2_ERROR= models.IntegerField(default=0)
    IIA2_OMISION= models.IntegerField(default=0)

    IIA3_ACIERTO= models.IntegerField(default=0)
    IIA3_ERROR= models.IntegerField(default=0)
    IIA3_OMISION= models.IntegerField(default=0)

    IIA4_ACIERTO= models.IntegerField(default=0)
    IIA4_ERROR= models.IntegerField(default=0)
    IIA4_OMISION= models.IntegerField(default=0)

    IIA5_ACIERTO= models.IntegerField(default=0)
    IIA5_ERROR= models.IntegerField(default=0)
    IIA5_OMISION= models.IntegerField(default=0)

    IIA6_ACIERTO= models.IntegerField(default=0)
    IIA6_ERROR= models.IntegerField(default=0)
    IIA6_OMISION= models.IntegerField(default=0)

    #II RAZONAMIENTO B. ESPACIAL
    IIB1_ACIERTO= models.IntegerField(default=0)
    IIB1_ERROR= models.IntegerField(default=0)
    IIB1_OMISION= models.IntegerField(default=0)

    IIB2_ACIERTO= models.IntegerField(default=0)
    IIB2_ERROR= models.IntegerField(default=0)
    IIB2_OMISION= models.IntegerField(default=0)

    IIB3_ACIERTO= models.IntegerField(default=0)
    IIB3_ERROR= models.IntegerField(default=0)
    IIB3_OMISION= models.IntegerField(default=0)
    #
    #II RAZONAMIENTO C. DEDUCTIVO
    IIC1_ACIERTO= models.IntegerField(default=0)
    IIC1_ERROR= models.IntegerField(default=0)
    IIC1_OMISION= models.IntegerField(default=0)

    #PUNTAJE IIC2
    IIC2_ACIERTO= models.IntegerField(default=0)
    IIC2_ERROR= models.IntegerField(default=0)
    IIC2_OMISION= models.IntegerField(default=0)

    # IV LECTURA A COMPRENSION
    IVA_ACIERTO= models.IntegerField(default=0)
    IVA_ERROR= models.IntegerField(default=0)
    IVA_OMISION= models.IntegerField(default=0)
    #
    # IV LECTURA B EFICACIA
    IVB_ACIERTO= models.IntegerField(default=0)
    IVB_ERROR= models.IntegerField(default=0)
    IVB_OMISION= models.IntegerField(default=0)
    #
    # IV LECTURA C VELOCIDAD
    IVC_ACIERTO= models.IntegerField(default=0)
    IVC_ERROR= models.IntegerField(default=0)
    IVC_OMISION= models.IntegerField(default=0)
    #
    #
    # V ESCRITURA A. ORTOGRAFIA
    # PUNTAJE V.A
    VA_ACIERTO= models.IntegerField(default=0)
    VA_ERROR= models.IntegerField(default=0)
    VA_OMISION= models.IntegerField(default=0)
    # #ACIERTO	ERROR	OMISION
    #
    # V ESCRITURA B. EXP ESCRITA
    # PUNTAJE V.B
    # 1	"Composición escrita superior a lo que es propia del nivel escolar."
    # 2	"Composición escrita presenta pequeños errores, no relevantes al proceso de expresión."
    # 3	"Composición acorde al nivel escolar."
    # 4	"Composición inferior a lo esperado acorde al nivel escolar."
    # 5	"Composición con abundantes errores, no logra expresarse."
    # 0	"Vacio"
    V = models.CharField(max_length= 1, choices=ITEM_VB.choices, default=ITEM_VB.VB_1)
    #
    # PUNTAJE VI.A
    #VI APREND MATEMATICOS A CAL&NUM
    #ACIERTO	ERROR	OMISION
    VIA_ACIERTO= models.IntegerField(default=0)
    VIA_ERROR= models.IntegerField(default=0)
    VIA_OMISION= models.IntegerField(default=0)
    #PUNTAJE VI.B
    #VI APREND MATEMATICOS B RESOLUC

    VIB_ACIERTO= models.IntegerField(default=0)
    VIB_ERROR= models.IntegerField(default=0)
    VIB_OMISION= models.IntegerField(default=0)








    class Meta:
            ordering = ["Año"]

    def __str__(self):
        return '%s-%s %s ' % (self.Año, self.Semestre, self.Rut, )

    def get_absolute_url(self):
        return f"/E09/{self.pk}/"
