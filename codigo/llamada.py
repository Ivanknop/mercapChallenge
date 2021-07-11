class Llamada():
    '''
    Llamada se crea con una duración (float), código de Origen de la llamada, código de Destino a donde se llama y a fecha exacta de realización de la llamada. La fecha es de tipo datetime (AA/MM/DD HH:MM:SS))
    '''
    def __init__(self,duracion,codigoOrigen,fecha,codigoDestino):
        self.duracion= duracion
        self.codigoOrigen = codigoOrigen
        self.fecha = fecha
        self.codigoDestino = codigoDestino
    def __str__(self):
        cadena = (f'Duración: {str(self.getDuracion())} | Costo de la Llamada: {str(self.facturarLlamada())} | Fecha de la llamada: {self.fechaEnStr()} | ' )
        return cadena
    
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
        devuelve fecha en el formato MM/DD HH:MM
        '''
        if self.fecha.minute <10:
            minutos = '0'+str(self.fecha.minute)
            cadena = f'{self.fecha.day}/{self.fecha.month}  {self.fecha.hour}:{minutos}'
        else:
            cadena = f'{self.fecha.day}/{self.fecha.month}  {self.fecha.hour}:{self.fecha.minute}'
        return cadena

    def facturarLlamada(self):
        pass

class LlamadaLocal(Llamada):
    '''
    ::param franjaHoraria es una hora de time convertida a int
    ::param diaHabil es un boolean
    ::param duracion es un float
    '''
    def __init__(self,duracion,codigoDestino,codigoOrigen,fecha):
        self.codigoDestino = codigoDestino
        Llamada.__init__(self,duracion,codigoOrigen,fecha,codigoDestino)
    def __str__(self):
        return super().__str__()+' Llamada Local'

    def verFranjaHoraria(self):
        '''
        compara la hora de la llamada con 8 y 20 para establecer. Retorna True o False
        '''
        return (self.getFecha().hour>=8) & (self.getFecha().hour<= 20)
    
    def esDiaHabil(self):
        '''
        isoweekday() retorna un día de la semana del 1 al 7, siendo 1 lunes. 
        compara ese resultado con 6 (sabado) para establecer si es dia de semana o no
         '''
        return self.getFecha().isoweekday() < 6

    def facturarLlamada(self):
        '''
        si self.esDiaHabil ==True y self.verFranjaHoraria == True entonces ingresa al if, si no al else
        '''
        if (self.esDiaHabil()) & (self.verFranjaHoraria()):
            return round(0.20* self.getDuracion(),2)
        else: return round(0.10* self.getDuracion(),2)

class LlamadaNacional(Llamada):
    def __init__(self,duracion,codigoDestino,codigoOrigen,fecha):
        self.codigoDestino = codigoDestino
        Llamada.__init__(self,duracion,codigoOrigen,fecha,codigoDestino)
    def __str__(self):
        return super().__str__()+' Llamada Nacional'
    
    def facturarLlamada(self):
        '''
        utiliza el codigo de destino para establecer qué precio tiene la llamada nacional
        '''
        if self.getCodigoDestino()<50:
            return 2*self.getDuracion()
        else: return 5*self.getDuracion()

class LlamadaInternacional(Llamada):
    def __init__(self,duracion,codigoDestino,codigoOrigen,fecha):
        self.codigoDestino = codigoDestino
        Llamada.__init__(self,duracion,codigoOrigen,fecha,codigoDestino)
    def __str__(self):
        return super().__str__()+' Llamada Internacional'
    
    def facturarLlamada(self):
        
        '''
        utiliza el codigo de destino para establecer qué precio tiene la llamada internacional
        '''
        if self.getCodigoDestino()<200:
            return 10*self.getDuracion()
        else: return 20*self.getDuracion()
