from colorama import init, Fore

class Factura():
    def __init__(self,cliente):
        self.cliente = cliente
    
    def getCliente(self):
        return self.cliente
   
    def facturarMes(self,mes):
        '''
        inicia monto con el abono básico
        llamada almacena el arreglo de listas de llamadas
        se posiciona en la la posición mes-1 del arreglo de llamadas para recorrer y sumar en monto el valor de cada llamada
        se invoca al método privado imprimirFacturaMensual enviando el monto rendondeado en dos decimales y el mes
        '''
        monto = self.getCliente().getAbono() 
        llamada = self.getCliente().getLlamadas()
        for i in range(len(llamada[mes-1])):
            monto = monto + llamada[mes-1][i].facturarLlamada()
        self._imprimirFacturaMensual(round(monto,2),mes)

    def _imprimirLlamadasMensual(self,mes):
        '''
        cont almacena la cantidad de llamadas de un mes
        llamadas almacena el arreglo de llamadas
        se posiciona en llamada[mes-1] y recorre esa posición del arreglo imprimiendo en consola cada llamada e incrementa cont
        retorna cont 
        '''
        cont=0
        llamada = self.getCliente().getLlamadas()
        for i in range(len(llamada[mes-1])):
            print (f'{i+1}) {llamada[mes-1][i]}')
            cont+=1
        return cont

    def _imprimirFacturaMensual(self,monto,mes):
        '''
        Arma la visualización de la factura en consola
        Fore cambia el color del texto en consola
        '''
        init()
        print('')
        print(Fore.YELLOW+'*********************************'.center(100)+'\n'+'SISTEMA DE FACTURACIÓN'.center(100))
        print(Fore.WHITE+f'CLIENTE: {self.getCliente()}')
        print (f'Llamadas realizadas en el mes {mes}:'.upper())
        totLlamadasMensual = self._imprimirLlamadasMensual(mes)
        print (f'Total de Llamadas del mes: {totLlamadasMensual}')
        print ('')
        print (f'Mes: {mes} | Monto a pagar: {monto}')
        print('')
        print(Fore.YELLOW+'GRACIAS POR USAR EL SERVICIO'.center(100)+'\n'+'*********************************'.center(100))