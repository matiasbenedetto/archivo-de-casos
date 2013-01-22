# -*- coding: utf-8 -*-
from archivo.models import *
from django.http import HttpResponse
from django.shortcuts import render_to_response


def parsear ():
    
    Caso.objects.all().delete()
    
    
    file = open("/home/matias/Escritorio/ARCHIVO_2011.txt")
    
    for line in file:
        
        nombre=""
        apellido=""
        edad=""
        ciudad=""
        fecha_deceso=""
        anio=""
        mes=""
        dia=""
        provincia=""
        imputados=""
        situacion_procesal=""
        circunstancias=""
        
        #obtiene Nombre
        if line[:7] == "Nombre:" :
            caso = Caso()
            print "------------------------------------"
            nombreCompleto = unicode(line[7:].strip(), "utf-8").title()            
            print nombreCompleto
            try:
                nombre = nombreCompleto.split(",")[1]
            except:
                pass            
            apellido = nombreCompleto.split(",")[0].lstrip()
            print nombre
            print apellido
            caso.nombre = nombre
            caso.apellido = apellido
    
        # obtiene Edad y Ciudad
        if line[:5] == "Edad:" :
            linea = line.split("Ciudad:")
            edad = linea[0][5:].strip()
            if edad=="Mayor" or edad=="mayor":
                edad = -1
            elif edad=="Menor" or edad=="menor":
                edad = -2
            elif edad=="Sin datos" or edad=="Sin datos.":
                edad = None
            elif edad=="11 meses" or edad=="10 meses" or edad=="9 meses" or edad=="8 meses" or edad=="7 meses" or edad=="6 meses" or edad=="5 meses" or edad=="4 meses" or edad=="3 meses" or edad=="2 meses" or edad=="1 mes" :
                edad=0
                
            caso.edad = edad
    
            ciudad = unicode(linea[1][7:].strip(), "utf-8").title()
            print ciudad
            caso.ciudad = ciudad
    
        #obtiene Fecha de deceso y Provincia
        if line[:16] == "Fecha de Deceso:":
            linea = line.split("Provincia:")
            fecha_deceso = unicode(linea[0][16:].strip(), "utf-8")
            try:
                anio = fecha_deceso.split("/")[2]
                mes = fecha_deceso.split("/")[1]
                dia = fecha_deceso.split("/")[0]
                caso.fecha_deceso = "%s-%s-%s" % (anio, mes, dia)
            except:
                pass
            print fecha_deceso
            
    
            provincia = unicode(linea[1][10:].strip(), "utf-8").title()
            print provincia
            caso.provincia = provincia
    
        #obtiene Imputados
        if line[:10] == "Imputados:":
            imputados = unicode(line[10:].strip(), "utf-8")
            print imputados
            caso.imputados = imputados
    
        #obtiene Circunstancias
        if line[:15] == "Circunstancias:":
            circunstancias = unicode(line[15:].strip(), "utf-8")
            print circunstancias
            caso.circunstancias = circunstancias
            
        
            caso.save()
            
            
            
def parsear2(requset):
    file = open("/home/matias/Escritorio/ARCHIVO_2011-3.txt")
    Caso.objects.all().delete()
    #file = unicode(file.read()).split("-*-*-*-")
    file = file.read()
    file = file.split("-*-*-*-")
    
    
    for item in file:
        nombre=""
        apellido=""
        edad=""
        ciudad=""
        fecha_deceso=""
        anio=""
        mes=""
        dia=""
        provincia=""
        imputados=""
        situacion_procesal=""
        circunstancias=""
        
        item = item.split("|||")    
        caso = Caso() 
           
        for line in item:
            #print line
            #print "--------------------"  
             
            if line[:8] == " Nombre:" :
                #print "------------------------------------"
                nombreCompleto = unicode(line[8:].strip(), "utf-8").title()            
                #print line
                try:
                    nombre = nombreCompleto.split(",")[1].strip()
                except:
                    pass            
                apellido = nombreCompleto.split(",")[0].strip()
                #print nombre
                #print apellido
                caso.nombre = nombre
                caso.apellido = apellido 
                
                
            # obtiene Edad
            if line[:5] == "Edad:" :                
                edad = line[5:].strip()
                caso.edad = edad
                #print edad    
                
            #obtiene ciudad
            if line[:7] == "Ciudad:"     :
                ciudad = line[7:].strip()
                ciudad = unicode(ciudad, "utf-8").strip().title()
                caso.ciudad = ciudad
                #print ciudad
                
            if line[:10] == "Provincia:" :
                provincia = unicode(line[10:].strip(), "utf-8").title()
                caso.provincia = provincia
                #print provincia
                
            
            #obtiene Fecha de deceso
            if line[:16] == "Fecha de Deceso:":
                fecha_deceso = unicode(line[16:].strip(), "utf-8")
                try:
                    anio = fecha_deceso.split("/")[2]
                    mes = fecha_deceso.split("/")[1]
                    dia = fecha_deceso.split("/")[0]
                    caso.fecha_deceso = "%s-%s-%s" % (anio, mes, dia)
                except:
                    pass
                #print fecha_deceso
                
                
            #obtiene Imputados
            if line[:10] == "Imputados:":
                imputados = unicode(line[10:].strip(), "utf-8")
                imputados = imputados.replace("  ", "").replace("\n","").replace("\r"," ")
                caso.imputados = imputados   
                #print imputados
                
                
            #obtiene Circunstancias
            if line[:15] == "Circunstancias:":
                circunstancias = unicode(line[15:].strip(), "utf-8")
                circunstancias = circunstancias.replace("  ", "").replace("\n","").replace("\r"," ")
                caso.circunstancias = circunstancias
                #print circunstancias
                
            
            #obtiene Situación Procesal
            if line[:20] == "Situación Procesal:":
                situcionProcesal = unicode(line[20:].strip(), "utf-8")
                situcionProcesal = situcionProcesal.replace("  ", "").replace("\n","").replace("\r"," ") 
                caso.situacion_procesal = situcionProcesal
                print situcionProcesal
                
        
        caso.save()              
        

    return HttpResponse(file)
    






