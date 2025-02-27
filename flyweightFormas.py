class Circulo:
    def __init__(self,color):
        self.color = color

    def dibujar(self,x,y,radio):
        print(f"Dibujando circulo de color {self.color} en ({x},{y}) con radio {radio}")

class Cuadrado:
    def __init__(self,color):
        self.color = color

    def dibujar(self,x,y,lado):
        print(f"Dibujando cuadrado de color {self.color} en ({x},{y}) con lado {lado}")

class Rectangulo:
    def __init__(self,color):
        self.color = color

    def dibujar(self,x,y,lado1,lado2):
        print(f"Dibujando rectangulo de color {self.color} en ({x},{y}) con lados {lado1} y {lado2}")

class Triangulo:
    def __init__(self,color):
        self.color = color  

    def dibujar(self,x,y,lado1,lado2,lado3):
        print(f"Dibujando triangulo de color {self.color} en ({x},{y}) con lados {lado1}, {lado2} y {lado3}")

class CirculoFactory:
    _circle={}
    @staticmethod
    def get_circle(color):
        if color not in CirculoFactory._circle:
            print(f"Creando circulo de color {color}")
            CirculoFactory._circle[color] = Circulo(color)
        else:
            print(f"Reutilizando circulo de color {color}")
        return CirculoFactory._circle[color]

class CuadradoFactory:
    _square={}
    @staticmethod
    def get_square(color):
        if color not in CuadradoFactory._square:
            print(f"Creando cuadrado de color {color}")
            CuadradoFactory._square[color] = Cuadrado(color)
        else:
            print(f"Reutilizando cuadrado de color {color}")
        return CuadradoFactory._square[color]

class RectanguloFactory:
    _rectangle={}
    @staticmethod
    def get_rectangle(color):
        if color not in RectanguloFactory._rectangle:
            print(f"Creando rectangulo de color {color}")
            RectanguloFactory._rectangle[color] = Rectangulo(color)
        else:
            print(f"Reutilizando rectangulo de color {color}")
        return RectanguloFactory._rectangle[color]

class TrianguloFactory:
    _triangle={}
    @staticmethod
    def get_triangle(color):
        if color not in TrianguloFactory._triangle:
            print(f"Creando triangulo de color {color}")
            TrianguloFactory._triangle[color] = Triangulo(color)
        else:
            print(f"Reutilizando triangulo de color {color}")
        return TrianguloFactory._triangle[color]

if __name__ == "__main__":
    factory = CirculoFactory()
    circulo1 = factory.get_circle("rojo")
    circulo1.dibujar(10, 20, 5)

    circulo2 = factory.get_circle("azul")
    circulo2.dibujar(30, 40, 10)
    
if __name__ == "__main__":
    factory = CuadradoFactory()
    cuadrado1 = factory.get_square("verde")
    cuadrado1.dibujar(10, 20, 5)

    cuadrado2 = factory.get_square("amarillo")
    cuadrado2.dibujar(30, 40, 10)
    
if __name__ == "__main__":
    factory = RectanguloFactory()
    rectangulo1 = factory.get_rectangle("azul")
    rectangulo1.dibujar(10, 20, 5, 10)

    rectangulo2 = factory.get_rectangle("verde")
    rectangulo2.dibujar(30, 40, 10, 15) 
    
if __name__ == "__main__":
    factory = TrianguloFactory()
    triangulo1 = factory.get_triangle("rojo")
    triangulo1.dibujar(10, 20, 5, 10, 15)

    triangulo2 = factory.get_triangle("azul")
    
    triangulo2.dibujar(30, 40, 10, 15, 20)
    