'''
Created on 5 jul. 2022

@author: xavier.ruiz
'''
class cliente:
    
    def __init__(self,nombre,apellido,pais,idioma,nombreAeropuerto):
        
        self.nombre=nombre
        self.apellido=apellido
        self.pais=pais
        self.idioma=idioma
        self.nombreAeropuerto=nombreAeropuerto
        
    def __str__(self):
        print(""+self.nombre+""+self.apellido+""+self.pais+""+self.idioma+""+self.nombreAeropuerto)