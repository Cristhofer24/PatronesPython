
class Televisor:
    def encender(self):
        print("Encendiendo televisor")

    def apagar(self):
        print("Apagando televisor")
        
class Altavoces:
    def encender(self):
        print("Encendiendo altavoces")

    def apagar(self):   
        print("Apagando altavoces")
        
    def volumen(self,nivel):
        print(f"Volumen {nivel}")
class videogame:
    def encender(self):
        print("Encendiendo videogame")

    def apagar(self):   
        print("Apagando videogame")

class Reproductor:
    def encender(self):
        print("Encendiendo reproductor")

    def apagar(self):   
        print("Apagando reproductor")
    def reproducir_pelicula(self,pelicula):
        print("Reproduciendo pelicula : {pelicula}")
class CineCasa:
      def __init__(self, televisor, altavoces, consola, reproductor):
        self.televisor = televisor
        self.altavoces = altavoces
        self.consola = consola
        self.reproductor = reproductor

      def ver_pelicula(self, pelicula):
        print("\n🎥 Preparando sistema de Cine en Casa...\n")
        self.televisor.encender()
        self.altavoces.encender()
        self.altavoces.volumen(50)
        self.consola.encender()
        self.reproductor.encender()
        self.reproductor.reproducir_pelicula(pelicula)
        print("\n🍿 ¡Disfruta la película! 🎬\n")

      def apagar_sistema(self):
        print("\n🔌 Apagando sistema de Cine en Casa...\n")
        self.reproductor.apagar()
        self.consola.apagar()
        self.altavoces.apagar()
        self.televisor.apagar()
        print("\n🎬 Sistema apagado. ¡Hasta la próxima!\n")
        
if __name__ == "__main__":
    # Crear los dispositivos
    tv = Televisor()
    altavoces = Altavoces()
    consola = videogame()
    reproductor = Reproductor()

    # Crear el Facade
    home_theater = CineCasa(tv, altavoces, consola, reproductor)

    # Ver una película
    home_theater.ver_pelicula("El Señor de los Anillos")

    # Apagar el sistema
    home_theater.apagar_sistema()

        