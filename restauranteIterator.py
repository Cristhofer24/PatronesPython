class ListaMenu:
    def __init__(self, nombre, precio):
        self.nombre = nombre  
        self.precio = precio  

    def __str__(self):
        return f"{self.nombre}: ${self.precio}"  
class Menu:
    def __init__(self):
        self.lista = []  

    def agregarList(self, lista):
        self.lista.append(lista)  

    def __iter__(self):
        return MenuIterator(self.lista)  

class MenuIterator:
    def __init__(self, lista):
        self.lista = lista  
        self.indice = 0  

    def __iter__(self):
        return self  

    def __next__(self):
        if self.indice < len(self.lista):
            item = self.lista[self.indice]  
            self.indice += 1 
            return item 
        else:
            raise StopIteration  

Lista1 = ListaMenu("Pollo", 10)
Lista2 = ListaMenu("Carne", 15)
Lista3 = ListaMenu("Pescado", 20)

Menu1 = Menu()
Menu1.agregarList(Lista1)
Menu1.agregarList(Lista2)
Menu1.agregarList(Lista3)

print("Menu de comida:")
for item in Menu1:
    print(item)  
