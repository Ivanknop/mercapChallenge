import cliente
from colorama import init, Fore

class Factura():
    def __init__(self,cliente):
        self.cliente = cliente
    
    def getCliente(self):
        return self.cliente
   
    def facturarMes(self,mes):
        '''
        compara los meses de las llamadas y hace la factura del mes correspondiente
        '''
        monto = self.getCliente().getAbono() 
        llamada = self.getCliente().getLlamadas()
        for i in range(len(llamada[mes-1])):
            monto = monto + llamada[mes-1][i].facturarLlamada()
        self.imprimirFacturaMensual(round(monto,2),mes)

    def imprimirLlamadasMensual(self,mes):
        cont=0
        llamada = self.getCliente().getLlamadas()
        for i in range(len(llamada[mes-1])):
            print (f'{i+1}) {llamada[mes-1][i]}')
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