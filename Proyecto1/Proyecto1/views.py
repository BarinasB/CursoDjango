from django.http import HttpResponse 
import datetime
from django.template import Template, Context


class Persona(object): 

    def __init__(self, nombre, apellido):

        self.nombre=nombre 

        self.apellido2=apellido 

def saludo(request):  # primera vista 

    p1=Persona("Brayan", "Perdomo")
    nombre ="Estiven"
    apellido = "Barinas"
    ahora  = datetime.datetime.now()
    temasDelCurso = ["plantillas","Modelos","Formularios"]
    temasDelCurso2 = []


    doc_externo = open("C:/Users/BarinasB/Desktop/Curso Django/Proyecto1/Proyecto1/plantillas/saludo.html") 
    plt=Template(doc_externo.read())
    doc_externo.close() 
    ctx= Context({"nombre_persona":p1.nombre,"apellido_persona":apellido,"tiempo_ahora":ahora, "temas":temasDelCurso2})
    documento  = plt.render(ctx)
    return HttpResponse(documento)

def despedir(request): # segunda de las vistas  

    return HttpResponse("Adios este era el primer saludo")
 



def dameFecha (request): 

    fecha_actual = datetime.datetime.now()

    documento = """<html>
    <body>
    <h1>fecha y hora actuales %s </h1>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)



def calculaEdad(request,edad, agno,):


    periodo = agno-2019 
    edadFutura = edad + periodo 
    documento ="<html><body><h2> en el año %s tendras %s años" %(agno, edadFutura)

    return HttpResponse(documento)


