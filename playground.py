from cliente import *
from facturacion import *
from llamada import *
from datetime import date, datetime
'''
    esNacional(codigo) permite determinar en qué categoría va la llamada.
    Por un tema de simplifiación determiné que los códigos menores a 100 son nacionales
    En la clase Llamada, diferencié dos tipos de codigos para nacionales e internacionales para simplificar el problema
'''

def esNacional(codigo):
    return (codigo < 100)

'''
Variables creadas para testeo. mes, listaDia,listaHorarios no se utilizan porque se hace uso del objeto datetime almacenado en fecha. 
Si se reemplaza fecha por esas listas en la posición [i] y se agregan los mismos en la clase LlamadaLocal, se puede testear.
'''
#codigo de origen
origen = 12
#abono basico
abono= 50
fecha = datetime.today()
llamadas = []
llamadas2 = []
clienteIvan = Cliente('Ivan',221,abono)
clienteDiana = Cliente('Diana',221,abono+10)
#codigos de destinos
listaDeDestinos1 = [12,100,32,305,12,42,59]
#mes es una lista que almacena números. Sólo para test. Es reemplazado por fecha.month
mes1 = [1,1,1,2,5,5,10]
#listaHorarios es una lista solo para test. Es reemplazado por fecha.hour
listaHorarios1 = [2,14,24,15,5,9,17]
listaDuracion1 =[2,10,15,3,7,1.5,1.4]
#listaDia permite saber si es día hábil o no. Se usa invocando al método esHabil(dia) desde el objeto llamada. 
listaDia1 =['sabado','jueves','domingo','lunes','miercoles','jueves','viernes']

listaDeDestinos2 = [40,90,145,12,47]
listaHorarios2 = [2,14,24,15,20]
listaDuracion2 = [3,1.5,4.2,10,4]
listaDia2 = ['domingo','lunes','jueves','martes','viernes']
mes2= [4,4,10,11,11]

for i in range(len(listaDeDestinos1)):
    #compara el código origen al código de la llamada y así determina de qué tipo será la llamada (local, nacional, internacional)
    if listaDeDestinos1[i]==origen:
        unaLlamada = LlamadaLocal(listaDuracion1[i],listaDeDestinos1[i],origen,fecha)
    elif esNacional(listaDeDestinos1[i]):
        unaLlamada = LlamadaNacional(listaDuracion1[i],listaDeDestinos1[i],origen,fecha)
    else:
        unaLlamada = LlamadaInternacional(listaDuracion1[i],listaDeDestinos1[i],origen,fecha)
    clienteIvan.agregarLlamada(unaLlamada)

for i in range(len(listaDeDestinos2)):
    if listaDeDestinos2[i]==origen:
        unaLlamada = LlamadaLocal(listaDuracion2[i],listaDeDestinos2[i],origen,fecha)
    elif esNacional(listaDeDestinos2[i]):
        unaLlamada = LlamadaNacional(listaDuracion2[i],listaDeDestinos2[i],origen,fecha)
    else:
        unaLlamada = LlamadaInternacional(listaDuracion2[i],listaDeDestinos2[i],origen,fecha)
    clienteDiana.agregarLlamada(unaLlamada)

factura1 = Factura(clienteIvan)
factura2 = Factura(clienteDiana)

factura1.facturarMes(7)
factura1.facturar()