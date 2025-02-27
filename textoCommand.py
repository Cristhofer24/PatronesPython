class Editor:
    def __init__(self):
        self.texto = ""

    def agregar_texto(self, texto):
        self.texto += texto
        print(f"Texto actual: {self.texto}")

    def eliminar_texto(self, texto):
        if texto in self.texto:
            self.texto = self.texto.replace(texto, "")
            print(f"Texto actual: {self.texto}")
        else:
            print("El texto a eliminar no se encuentra.")

# Comando para agregar texto
class AgregarTextoCommand:
    def __init__(self, editor, texto):
        self.editor = editor
        self.texto = texto

    def ejecutar(self):
        self.editor.agregar_texto(self.texto)

    def deshacer(self):
        self.editor.eliminar_texto(self.texto)

# Comando para eliminar texto
class EliminarTextoCommand:
    def __init__(self, editor, texto):
        self.editor = editor
        self.texto = texto

    def ejecutar(self):
        self.editor.eliminar_texto(self.texto)

    def deshacer(self):
        self.editor.agregar_texto(self.texto)

# Clase Invocador que maneja los comandos y el deshacer
class EditorControl:
    def __init__(self):
        self.comandos = []

    def ejecutar_comando(self, comando):
        self.comandos.append(comando)
        comando.ejecutar()

    def deshacer(self):
        if self.comandos:
            comando = self.comandos.pop()
            comando.deshacer()
        else:
            print("No hay ninguna acción para deshacer.")

# Uso de los comandos
editor = Editor()
control = EditorControl()

agregar_comando = AgregarTextoCommand(editor, "Hola Mundo! ")
eliminar_comando = EliminarTextoCommand(editor, "Mundo")


control.ejecutar_comando(agregar_comando)


control.ejecutar_comando(eliminar_comando)

control.deshacer()


control.deshacer()
