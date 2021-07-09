import cliente
from colorama import init, Fore

class Factura():
    def __init__(self,cliente):
        self.cliente = cliente
    
    def getCliente(self):
        return self.cliente

    def facturar(self):
        '''
        llamada almacena la lista de llamadas del cliente.
        facturas es una lista vacía de los meses del año
        recorre llamada y almacena el monto a pagar de cada llamada según sea el mes correspondiente
        invoca a imprimirFacturas(facturas) para hacer la impresión en pantalla
        '''

        facturas = []
        for i in range(12):
            facturas.append(self.getCliente().getAbono())
        llamada = self.getCliente().getLlamadas()
        #el código de abajo sirve para el test duro, con fecha harcodeada
        #for i in range(len(llamada)):
         #   facturas[llamada[i].getMes()] = facturas[llamada[i].getMes()] + llamada[i].facturarLlamada()  
        for i in range(len(llamada)):
            facturas[llamada[i].getFecha().month-1] = facturas[llamada[i].getFecha().month-1] + llamada[i].facturarLlamada()
            facturas[llamada[i].getFecha().month-1] =round(facturas[llamada[i].getFecha().month-1],2)            
        self.imprimirTodasFactura(facturas)
    
    def facturarMes(self,mes):
        '''
        compara los meses de las llamadas y hace la factura del mes correspondiente
        '''
        monto = self.getCliente().getAbono() 
        llamada = self.getCliente().getLlamadas()
        for i in range (len(llamada)):
            if llamada[i].getFecha().month == mes:
                monto = monto + llamada[i].facturarLlamada()
        self.imprimirFacturaMensual(round(monto,2),mes)


    def imprimirTodasLlamadas(self):
        for i in range(len(self.getCliente().getLlamadas())):
            print (f'{i+1}) {self.getCliente().getLlamadas()[i]}')
    
    def imprimirLlamadasMensual(self,mes):
        cont=0
        for i in range(len(self.getCliente().getLlamadas())):
            if self.getCliente().getLlamadas()[i].getFecha().month == mes:
                print (f'{i+1}) {self.getCliente().getLlamadas()[i]}')
                cont+=1
        return cont

    def imprimirFacturaMensual(self,monto,mes):
        init()
        print(Fore.YELLOW+'*********************************'.center(100)+'\n'+'SISTEMA DE FACTURACIÓN'.center(100))
        print(Fore.WHITE+'CLIENTE: {self.getCliente()}')
        print (f'Llamadas realizadas en el mes {mes}:'.upper())
        totLlamadasMensual = self.imprimirLlamadasMensual(mes)
        print (f'Total de Llamadas del mes: {totLlamadasMensual}')
        print ('')
        print (f'Mes: {mes} | Monto a pagar: {monto}')
        print('')
        print(Fore.YELLOW+'*********************************'.center(100)+'\n'+'GRACIAS POR USAR EL SERVICIO'.center(100))

    def imprimirTodasFactura(self,facturas):
        print('*********************************'.center(100)+'\n'+'SISTEMA DE FACTURACIÓN'.center(100))
        print(Fore.WHITE+f'CLIENTE: {self.getCliente()}')
        print (f'Total de Llamadas: {str(len(self.getCliente().getLlamadas()))}\n'.upper())
        print ('Llamadas realizadas:'.upper())
        self.imprimirTodasLlamadas()
        print ('')
        for i in range(len(facturas)):
            print ('Mes: ',i,' |Monto a pagar: ',facturas[i])
        print('')
        print(Fore.YELLOW+'*********************************'.center(100)+'\n'+'GRACIAS POR USAR EL SERVICIO'.center(100))

