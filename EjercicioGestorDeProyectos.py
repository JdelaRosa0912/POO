from dataclasses import dataclass
@dataclass

class Colaborador:
    username: str
    email: str

class Proyecto:

    def __init__(self, nombre: str, lenguaje: str):
        self.nombre = nombre
        self.lenguaje = lenguaje
        self.colaboradores = []

    def agregar_colaborador(self, colaborador: Colaborador):
        if self.tiene_colaborador(colaborador.username):
            print("El colaborador ya está en el proyecto.")
        else:
            self.colaboradores.append(colaborador)

    def tiene_colaborador(self, username: str) -> bool:
        for colaborador in self.colaboradores:
            if colaborador.username == username:
                return True
        return False
    def __str__(self) -> str:
        return f"Proyecto: {self.nombre}, Lenguaje: {self.lenguaje} - {len(self.colaboradores)} colaborador(es)"

class GestorProyectos:
    def __init__(self):
        self.proyectos = []

    def registrar_proyecto(self,proyecto: Proyecto) -> None:
        if self.buscar_proyecto(proyecto.nombre) is not None:
            print("El proyecto ya está registrado.")
        else:
            self.proyectos.append(proyecto)
    def buscar_proyecto(self, nombre: str) -> Proyecto:
        for proyecto in self.proyectos:
            if proyecto.nombre == nombre:
                return proyecto
        return None
    
    def listar_proyectos(self) -> Proyecto:
        return self.proyectos

# Colaboradores
ana   = Colaborador(username="ana_dev", email="ana@mail.com")
luis  = Colaborador(username="luis99",  email="luis@mail.com")
sofia = Colaborador(username="sofiaml", email="sofia@mail.com")

# Proyectos
p1 = Proyecto(nombre="InventarioApp", lenguaje="Python")
p1.agregar_colaborador(ana)
p1.agregar_colaborador(luis)
p1.agregar_colaborador(ana)   # aviso: ya existe

p2 = Proyecto(nombre="WebStore", lenguaje="JavaScript")
p2.agregar_colaborador(sofia)

# __str__
print(p1)  # Proyecto: InventarioApp [Python] — 2 colaborador(es)
print(p2)  # Proyecto: WebStore [JavaScript] — 1 colaborador(es)

# tiene_colaborador
print(p1.tiene_colaborador("ana_dev"))  # True
print(p1.tiene_colaborador("sofiaml"))  # False

# Gestor
gestor = GestorProyectos()
gestor.registrar_proyecto(p1)
gestor.registrar_proyecto(p2)
gestor.registrar_proyecto(p1)  # aviso: ya existe

encontrado = gestor.buscar_proyecto("WebStore")
print(encontrado)  # Proyecto: WebStore [JavaScript] — 1 colaborador(es)

no_existe = gestor.buscar_proyecto("OtroProyecto")
print(no_existe)   # None

print(len(gestor.listar_proyectos()))  # 2