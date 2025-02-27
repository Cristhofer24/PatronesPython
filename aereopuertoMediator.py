class TorreControl:
    def __init__(self):
        self.aviones_espera=[]
        self.aterrisaje_progreso = False
    def solicituar_aterrisaje(self,avion):
        if not self.aterrisaje_progreso:
            print(f"{avion.nombre} ha recibido permiso para aterrisar")
            self.aterrisaje_progreso = True
            avion.aterrisar()
        else:
            print(f"{avion.nombre} debe esperar , el aterrisaje esta en curso")
    
    def fin_aterrisaje(self):
        print("Aterrisaje completado, La torre de control esta disponible para otros aviones")
        self.aterrisaje_progreso = False
        if self.aviones_espera:
            siguiente_avion = self.aviones_espera.pop(0)
            self.solicituar_aterrisaje(siguiente_avion)
    
class Avion:
    def __init__(self,nombre):
        self.nombre = nombre
    def solicitud_aterrisaje(self,torre_control):
        torre_control.solicituar_aterrisaje(self)
    
    def aterrisar(self):
        print(f"{self.nombre} ha aterrisado")
    
torre_control = TorreControl()
avion1 = Avion("Avion 1")
avion2 = Avion("Avion 2")
avion3 = Avion("Avion 3")

avion1.solicitud_aterrisaje(torre_control)
avion2.solicitud_aterrisaje(torre_control)
avion3.solicitud_aterrisaje(torre_control)

torre_control.fin_aterrisaje()
            