class Llamada():
    def __init__(self,duracion,codigoOrigen,fecha,codigoDestino,mes):
        self.duracion= duracion
        self.codigoOrigen = codigoOrigen
        self.fecha = fecha
        self.codigoDestino = codigoDestino
        self.mes=mes
    def __str__(self):
        cadena = (f'Duración: {str(self.getDuracion())} | Costo de la Llamada: {str(self.facturarLlamada())} | Fecha de la llamada: {self.fechaEnStr()} | ' )
        return cadena
    
    def getMes(self):
        return self.mes
    def getCodigoDestino(self):
        return self.codigoDestino
    def getDuracion (self):
        return self.duracion
    def getCodigoOrigen (self):
        return self.codigoOrigen
    def getFecha(self):
        return self.fecha
    def fechaEnStr(self):
        '''
        toString que devuelve fecha en el formato MM/DD HH:MM
        '''
        cadena = f'{self.fecha.day}/{self.fecha.month}  {self.fecha.time()}'
        return cadena

    def facturarLlamada(self):
        pass

class LlamadaLocal(Llamada):
    '''
    ::param franjaHoraria es una hora de time convertida a int
    ::param diaHabil es un boolean
    ::param duracion es un float
    '''
    def __init__(self,duracion,codigoDestino,codigoOrigen,fecha,mes=None):
        self.codigoDestino = codigoDestino
        Llamada.__init__(self,duracion,codigoOrigen,fecha,codigoDestino,mes)
    def __str__(self):
        return super().__str__()+'| Llamada Local'

    def verFranjaHoraria(self):
        return (self.getFecha().hour>=8) & (self.getFecha().hour<= 20)
    
    def esDiaHabil(self):
        return self.getFecha().isoweekday() < 5

    def facturarLlamada(self):
        if (self.esDiaHabil()) & (self.verFranjaHoraria()):
            return round(0.20* self.getDuracion(),2)
        else: return round(0.10* self.getDuracion(),2)

class LlamadaNacional(Llamada):
    def __init__(self,duracion,codigoDestino,codigoOrigen,fecha,mes=None):
        self.codigoDestino = codigoDestino
        Llamada.__init__(self,duracion,codigoOrigen,fecha,codigoDestino,mes)
    def __str__(self):
        return super().__str__()+'| Llamada Nacional'
    
    def facturarLlamada(self):
        if self.getCodigoDestino()<50:
            return 2*self.getDuracion()
        else: return 5*self.getDuracion()

class LlamadaInternacional(Llamada):
    def __init__(self,duracion,codigoDestino,codigoOrigen,fecha,mes=None):
        self.codigoDestino = codigoDestino
        Llamada.__init__(self,duracion,codigoOrigen,fecha,codigoDestino,mes)
    def __str__(self):
        return super().__str__()+'| Llamada Internacional'
    
    def facturarLlamada(self):
        if self.getCodigoDestino()<200:
            return 10*self.getDuracion()
        else: return 20*self.getDuracion()
