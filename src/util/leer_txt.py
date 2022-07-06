'''
Created on 5 jul. 2022

@author: xavier.ruiz
'''
from model.cliente import cliente
class leer_txt:
    
    def leer(self,archivo):
        lineas=archivo.readlines()
        cli=[]
        for linea in lineas:
            for i in range(5):
               
                
                coma=int(linea.find(","))
                cli.append(linea[0:coma])
                linea=linea[coma+1:len(linea)]
                
        cliente1=cliente(cli[0],cli[1],cli[2],cli[3],cli[4])
        cliente2=cliente(cli[5],cli[6],cli[7],cli[8],cli[9])      
        return cliente1,cliente2
    
        




