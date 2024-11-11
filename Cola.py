from typing import List, TypeVar, Generic

E = TypeVar('E')

class AgregadoLineal(Generic[E]):
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

    def remove(self) -> E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        removed_elements = []
        while not self.is_empty:
            removed_elements.append(self.remove())
        return removed_elements

    def add_all(self, ls: List[E]) -> None:
        for elem in ls:
            self.add(elem)

    def add(self, e: E) -> None:
        raise NotImplementedError("El método add debe ser implementado por la subclase")

class Cola(AgregadoLineal[E]):
    @staticmethod
    def of() -> 'Cola[E]':
        return Cola()

    def add(self, e: E) -> None:
        self._elements.append(e)

    def __str__(self) -> str:
        elementos_str = ', '.join(str(e) for e in self._elements)
        return f"Cola({elementos_str})"

#test
prueba=Cola()
prueba.add(23)
prueba.add(47)
prueba.add(47)
prueba.add(1)
prueba.add(2)
prueba.add(-3)
prueba.add(4)
prueba.add(5)
print(prueba)

print(prueba.remove_all())