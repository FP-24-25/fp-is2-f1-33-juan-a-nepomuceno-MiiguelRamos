from typing import List, TypeVar, Generic, Callable, Tuple

E = TypeVar('E')
P = TypeVar('P')

class ColaPrioridad(Generic[E, P]):
    def __init__(self):
        self._elements: List[E] = []
        self._priorities: List[P] = []

    @property
    def size(self) -> int:
        return len(self._elements)

    @property
    def is_empty(self) -> bool:
        return self.size == 0

    @property
    def elements(self) -> List[E]:
        return self._elements.copy()

    def add(self, e: E, priority: P) -> None:
        index = self.__index_order(priority)
        self._elements.insert(index, e)
        self._priorities.insert(index, priority)

    @staticmethod
    def of() -> 'ColaPrioridad[E, P]':
        return ColaPrioridad()

    def add_all(self, ls: List[Tuple[E, P]]) -> None:
        for elem, priority in ls:
            self.add(elem, priority)

    def remove(self) -> E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        self._priorities.pop(0)
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        removed_elements = []
        while not self.is_empty:
            removed_elements.append(self.remove())
        return removed_elements

    def __index_order(self, priority: P) -> int:
        for i, p in enumerate(self._priorities):
            if priority < p:
                return i
        return len(self._priorities)

    def decrease_priority(self, e: E, new_priority: P) -> None:
        if e in self._elements:
            index = self._elements.index(e)
            current_priority = self._priorities[index]
            if new_priority > current_priority:
                self._elements.pop(index)
                self._priorities.pop(index)
                self.add(e, new_priority)

    def __str__(self) -> str:
        elementos_prioridades = ', '.join(f"({e}, {p})" for e, p in zip(self._elements, self._priorities))
        return f"ColaPrioridad[{elementos_prioridades}]"


#test
cola_prioridad = ColaPrioridad.of()
cola_prioridad.add("Paciente A", 3)
cola_prioridad.add("Paciente B", 2)
cola_prioridad.add("Paciente C", 1)
print(cola_prioridad)

print(cola_prioridad.remove())
print(cola_prioridad)

cola_prioridad.decrease_priority("Paciente B", 3)
print(cola_prioridad)
 