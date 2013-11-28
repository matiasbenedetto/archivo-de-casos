# -*- coding: utf-8 -*-
from archivo.models import *
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
import requests
from geoposition import Geoposition
import json
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q



def index (request):
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))
    

def caso (request, id):
    caso = Caso.objects.get(id=id)
    return render_to_response('caso.html', locals(), context_instance=RequestContext(request))

def mapa (request):
    return render_to_response('mapa.html', locals(), context_instance=RequestContext(request))


def que_es (request):
    return render_to_response('que-es.html', locals(), context_instance=RequestContext(request))


@csrf_exempt
def cargar_marcadores (request):
    
    if request.method == "POST":

        desde = request.POST["desde"]
        hasta = request.POST["hasta"]
        tipo_edad = request.POST["tipo_edad"]
        sexo = request.POST["sexo"]
        fuerza = request.POST["fuerza"]
        provincia = request.POST["provincia"]

        q = Q()

        q = q & Q(anio__gte=desde)
        q = q & Q(anio__lte=hasta)

        if tipo_edad:
            q = q & Q(tipo_edad__id=tipo_edad)

        if sexo:
            q = q & Q(sexo=sexo)

        if fuerza:
            q = q & Q(fuerza=fuerza)

        if provincia:
            q = q & Q(provincia=provincia)


        casos = list(Caso.objects.filter(q).values_list('coordenadas', 'nombre', 'apellido', 'id', 'sexo').exclude(coordenadas=Geoposition(0,0)))
    else:
        casos = list(Caso.objects.filter(anio=2011).values_list('coordenadas', 'nombre', 'apellido', 'id', 'sexo').exclude(coordenadas=Geoposition(0,0)))

    return HttpResponse(json.dumps(casos), content_type="application/json")


def importar_bd (request):
    Caso.objects.all().delete()

    for c in Archivodecasos.objects.all().order_by("numcaso").reverse():

        edad = c.edad
        try:
            edad = int(c.edad)
        except:
            edad = None

        try:
            circunstancia = Circunstancia.objects.get(id=c.cod_circunstancia)
        except:
            circunstancia = None

        try:
            nombre=c.nombre.split(",")[1].title()
            apellido=c.nombre.split(",")[0].title()
        except:
            nombre=c.nombre
            apellido=c.nombre

        try:
            tipo_edad = TipoEdad.objects.get(id=c.cod_edad)
        except:
            tipo_edad = None


        print c.numcaso
        print c.cod_circunstancia

        caso=Caso(
                id=c.numcaso,
                nombre = nombre,
                apellido = apellido,
                edad = edad,
                tipo_edad = tipo_edad,
                mayor = c.mayor,
                ciudad = c.ciudad.title(),
                provincia = c.provincia.title(),
                fecha_deceso = c.fecha_de_deceso,
                anio = c.anio,
                imputados = c.imputados,
                situacion_procesal = c.situacion_procesal,
                circunstancia = circunstancia,
                circunstancias = c.circunstancias,
                fuerza = Fuerza.objects.get(nombre=c.cod_fuerza)
            )


        caso.save()

    casos = Caso.objects.all()

    return render_to_response('importar_bd.html', locals(), context_instance=RequestContext(request))


def crear_fuerzas (request):
    Fuerza.objects.all().delete()

    f=Fuerza(id=1, nombre="PFA")
    f.save()
    f=Fuerza(id=2, nombre="PP")
    f.save()
    f=Fuerza(id=3, nombre="SP")
    f.save()
    f=Fuerza(id=4, nombre="PNA")
    f.save()
    f=Fuerza(id=5, nombre="GNA")
    f.save()
    f=Fuerza(id=6, nombre="Otras Fuerzas")
    f.save()
    f=Fuerza(id=7, nombre="Seguridad Privada")
    f.save()
    f=Fuerza(id=8, nombre="PM")
    f.save()

    return HttpResponse("Fuerzas Creadas")


def crear_circunstancias (request):
    Circunstancia.objects.all().delete()

    c=Circunstancia(id=1, nombre="Gatillo fácil")
    c.save()
    c=Circunstancia(id=2, nombre="Muerte en cárcel, comisaría o bajo custodia")
    c.save()
    c=Circunstancia(id=3, nombre="Muerte intrafuerza o intrafamiliar")
    c.save()
    c=Circunstancia(id=4, nombre="Causa fraguada o consecuencia de otros delitos")
    c.save()
    c=Circunstancia(id=5, nombre="En movilizacion o protesta social")
    c.save()
    c=Circunstancia(id=6, nombre="Sin datos")
    c.save()
    c=Circunstancia(id=7, nombre="Otras circunstancias")
    c.save()

    return HttpResponse("Circunstancias Creadas")

def crear_tipo_edad (request):
    TipoEdad.objects.all().delete()

    t=TipoEdad(id=1, nombre="Hasta 14 Años")
    t.save()
    t=TipoEdad(id=2, nombre="De 15 a 25 Años")
    t.save()
    t=TipoEdad(id=3, nombre="De 26 a 35 Años")
    t.save()
    t=TipoEdad(id=4, nombre="De 36 a 45 años")
    t.save()
    t=TipoEdad(id=5, nombre="Más de 45 Años")
    t.save()

    return HttpResponse("Tipos de Edad creados")

def buscar_coordenadas(request):

    for caso in Caso.objects.filter(coordenadas=Geoposition(0,0)):


        try:
            ciudad = caso.ciudad.split("-")[0]
        except:
            ciudad = caso.ciudad

        if not ciudad:
            opciones = {'q': caso.provincia, 'countrycodes': 'ar', 'limit':1, 'format': 'json'}
        else:
            opciones = {'city': ciudad, 'state': caso.provincia, 'country': 'ar', 'limit':1, 'format': 'json'}

        r = requests.get("http://nominatim.openstreetmap.org/search", params=opciones)
        datos = r.json()

        try:
            print caso.id
            print caso.ciudad
            print "PROVINCIA: " + caso.provincia

            lat = datos[0]["lat"]
            lon = datos[0]["lon"]
            caso.coordenadas.latitude = lat
            caso.coordenadas.longitude = lon
            caso.save()
            
            print lat + " , " + lon
            print "-----------------------------------"
        except Exception, err:
            print Exception, err

            print "ERROR"
            print caso.id
            print caso.ciudad
            print "-----------------------------------"

    return HttpResponse("Coordandas Buscadas")


