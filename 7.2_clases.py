class Person: #DEFINIMOS LA CLASE
    def __init__(self, name, age):        #DEFINIMOS EL CONSTRUCTOR CON __init__, un arrancador inicial
        self.name = name
        self._age = age
        
        #agregar un _ significa q es propiedad privada, nomas puedo modificarlo mediante el método setter
        """ EJ: self._name = name     self._age = age, esto para q no se pueda cambiar el tipo de valor"""
        
        #esto nada más define a la clase de persona, si no, definiría a todo el programa pero no queremos eso
        
    def greeting(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} años")
        
p1 = Person ("Yaksi", 19)
p2 = Person ("Víctor", 18)
    
p1.greeting()
p2.greeting()