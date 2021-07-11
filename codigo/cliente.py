from llamada import *
class Cliente():
    '''
    Un Cliente tiene nombre completo, su número y un valor de abono básico
    Se crea una arreglo de 12 posiciones de listas de llamadas vacías.
    '''
    def __init__(self,nombreCompleto,numero,abono):
        self.numero = numero
        self.nombreCompleto = nombreCompleto
        self.llamadas = self.inicializarLlamadas()
        self.abono = abono
    def __str__(self):
        '''
        Retorna el nombre del cliente, su número y cuánto es el abono básico
        '''
        cadena = f'{self.getNombreCompleto()} | Numero: {str(self.getNumero())} | Abono básico: {str(self.getAbono())}'
        return cadena
    
    def getNumero (self):
        return self.numero
    def getNombreCompleto (self):
        return self.nombreCompleto
    def getLlamadas (self):
        return self.llamadas
    def getAbono (self):
        return self.abono

    def inicializarLlamadas(self):
        '''
        Crea un arreglo de 12 posiciones de listas de llamadas. Cada posición es un mes. 
        '''
        llamadas = []
        for i in range(12):
            llamadas.append([])
        return llamadas

    def setAbono(self,nuevoAbono):
        '''
        Recibe un nuevoAbono y modifica el seteado
        '''
        self.abono = nuevoAbono

    def agregarLlamada(self,nuevaLlamada):
        '''
        Agrega una nueva llamada de tipo Llamada en la posición llamada.getFecha.month-1 porque el arreglo de llamadas es de 0 a 11 y los meses van de 1 a 12 
        '''
        self.llamadas[nuevaLlamada.getFecha().month-1].append(nuevaLlamada)

