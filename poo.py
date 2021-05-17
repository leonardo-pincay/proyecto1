class Persona :
    # metodo constructor 

    def __init__ (self):
        self.edad= 34

   
    def __hablar__(self,mensaje):
        print(mensaje)

    def __sumar__(self):
        print()


Juan = Persona()
Juan.__hablar__("hola")
        