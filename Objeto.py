class Persona():
    def __init__(self, nombre, apellido, altura, peso, c_ojos):
        Persona.nombre = nombre
        Persona.apellido = apellido
        Persona.altura = altura
        Persona.peso = peso
        Persona.c_ojos = c_ojos
    def Comer(self, ensalada, fondo, postre):
        return f"{self.nombre} come {ensalada} con {fondo} y {postre}"
    def Sentarse(self, asiento):
        return f"{self.nombre} se sienta en un {asiento}"
    def Dormir(self, lugar, temperatura):
        return f"{self.nombre} se duerme en {lugar} con {temperatura}"

Persona_1 = Persona('Javier', 'Hernandez', 175, 65, 'cafe')
print (Persona_1.Comer('tomate', 'empanada', 'arroz con leche'))
print (Persona_1.Dormir('basura', 'frio'))