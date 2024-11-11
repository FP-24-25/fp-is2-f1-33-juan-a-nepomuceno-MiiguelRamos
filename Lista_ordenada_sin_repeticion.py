from typing import List, TypeVar, Generic, Callable

# Definimos tipos genéricos E y R
E = TypeVar('E')
R = TypeVar('R')

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

class ListaOrdenadaSinRepeticion(AgregadoLineal[E], Generic[E, R]):
    def __init__(self, order: Callable[[E], R]):
        super().__init__()
        self.__order = order

    @staticmethod
    def of(order: Callable[[E], R]) -> 'ListaOrdenada[E, R]':
        return ListaOrdenadaSinRepeticion(order)

    def __index_order(self, e: E) -> int:
        for i, element in enumerate(self._elements):
            if self.__order(e) < self.__order(element):
                return i
        return len(self._elements)

    def add(self, e: E) -> None:
        if e not in self.elements:
            index = self.__index_order(e)
            self._elements.insert(index, e)

    def __str__(self) -> str:
        elementos_str = ', '.join(str(e) for e in self._elements)
        return f"ListaOrdenadaSinRepeticion({elementos_str})"

#test    
lista = ListaOrdenadaSinRepeticion.of(lambda x: -x)
lista.add(23)
lista.add(47)
lista.add(47)
lista.add(1)
lista.add(2)
lista.add(-3)
lista.add(4)
lista.add(5)
print(lista)

print(lista.remove())

lista.add(23)
#print(lista.remove_all())

lista.add(0)
print(lista)
lista.add(0)
print(lista)
lista.add(7)
print(lista)