#El agregado_lineal lo he copiado y pegado del entregado en mi trabajo
from typing import List, TypeVar, Generic , Callable
from abc import ABC, abstractmethod

E = TypeVar('E')

class AgregadoLineal(ABC, Generic[E]):
    def __init__(self):
        self._elements: List[E] = []

    @property
    def size(self) -> int:
        return len(self._elements)

    @property
    def is_empty(self) -> bool:
        return self.size == 0

    @property
    def elements(self) -> List[E]:
        return self._elements.copy()

    @abstractmethod
    def add(self, e: E) -> None:
        pass

    def add_all(self, ls: List[E]) -> None:
        for elem in ls:
            self.add(elem)

    def remove(self) -> E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        removed_elements = []
        while not self.is_empty:
            removed_elements.append(self.remove())
        return removed_elements

#1 (Aquí empieza realmente el ejercicio)

class ColaConLimite(AgregadoLineal[E]):
    def __init__(self, capacidad: int):
        #Creamos el parámetro capacidad
        super().__init__()
        self.capacidad = capacidad
        
    def __str__(self) -> str:
            elementos_str = ', '.join(str(e) for e in self._elements)
            return f"ColaConLimite({elementos_str})"


    def add(self, e: E) -> None:
        if self.is_full():
            raise OverflowError("La cola está llena.")
        self._elements.append(e)

    def is_full(self) -> bool:
        #Comprobamos que no este llena la cola
        return self.size >= self.capacidad

    @classmethod
    def of(cls, capacidad: int) -> 'ColaConLimite[E]':
        return cls(capacidad)


#2
class Agregado_Lineal(ABC, Generic[E]):
    def __init__(self):
        self._elements: List[E] = []

    @property
    def size(self) -> int:
        return len(self._elements)

    @property
    def is_empty(self) -> bool:
        return self.size == 0

    @property
    def elements(self) -> List[E]:
        return self._elements.copy()

    @abstractmethod
    def add(self, e: E) -> None:
        pass

    def add_all(self, ls: List[E]) -> None:
        for elem in ls:
            self.add(elem)

    def remove(self) -> E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        removed_elements = []
        while not self.is_empty:
            removed_elements.append(self.remove())
        return removed_elements
    
    def contains(self, e: E) -> bool:
        #Hacemos la verificación de si está el elemento en el agradado
        if e in self._elements:
            return print(e, 'esta en el agregado:', self.elements)
    
    def find(self, func: Callable[[E], bool]) -> E | None:
        for elem in self._elements:
            if func(elem):
                return elem
        return None
    
    def filter(self, func: Callable[[E], bool]) -> list[E]:
        return [elem for elem in self._elements if func(elem)]

#3. Tests

#1
#Llamo a la clase, dandole un límite de 3 elementos
cola = ColaConLimite.of(3)
#Le añado elementos
cola.add("Tarea 1")
cola.add("Tarea 2")
cola.add("Tarea 3")

#Intento añadir un 4 elemento
try:
    cola.add("Tarea 4")
except OverflowError as e:
    print(e)
print(cola.remove())
print(cola)

#2
# Creamos una subclase concreta de AgregadoLineal
class Lista(Agregado_Lineal[E]):
    def add(self, e: E) -> None:
        self._elements.append(e)

# Ejemplo con Lista
lista = Lista[int]()
lista.add(10)
lista.add(20)
lista.add(30)
lista.add(40)

# Uso de contains
print(lista.contains(20))
print(lista.contains(50))

# Uso de find
print(lista.find(lambda x: x > 25))
print(lista.find(lambda x: x < 5))

# Uso de filter
print(lista.filter(lambda x: x % 2 == 0))
print(lista.filter(lambda x: x > 25))
print(lista.filter(lambda x: x < 15))
