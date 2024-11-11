from typing import List, TypeVar, Generic
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

class Cola(AgregadoLineal[E]):
    def add(self, e: E) -> None:
        self._elements.append(e)

class Pila(AgregadoLineal[E]):
    def __init__(self):
        super().__init__()
        
    def of() -> 'Pila[E]':
        return Pila()

    def add(self, e: E) -> None:
        self._elements.insert(0,e)

    def __str__(self) -> str:
        elementos_str = ', '.join(str(e) for e in self._elements)
        return f"Cola({elementos_str})"

#test
prueba=Pila()
prueba.add(1)
prueba.add(2)
prueba.add(3)
prueba.add(4)
print(prueba)
prueba.remove()
print(prueba)