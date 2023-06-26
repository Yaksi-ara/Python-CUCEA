#programacion orientada a funciones
"paradigma: patron, serie de estándares"
class person:
    name:str
    age:int
    
    def greeting():
        print("Hola, mi nombre es")
person1=person
"persona 1 tiene un nombre y una edad"
person1.name = "Yaksi"
person1.age = "19"


person1.greeting()
print(person1.name, person1.age)
