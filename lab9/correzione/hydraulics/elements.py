from typing import List, Optional
from abc import ABC, abstractmethod


class Element(ABC):
    def __init__(self, name: str) -> None:
        self._name = name
        self._next = {0:None}

    def get_name(self) -> str:
        return self._name

    def connect(self, elm: "Element") -> None:
        self._next[0] = elm

    def get_output(self) -> Optional["Element"]:
        return self._next[0]

    @abstractmethod #i metodi astratti devono essere implementati in TUTTE le sottoclassi di Element
    def simulate(self, inflow, sim_list): #per simulare il funzionamento dell'elemento (flusso in entrata e uscita)
        pass


class Source(Element):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._flow = 0

    def set_flow(self, flow: float) -> None:
        self._flow = flow

    def simulate(self, inflow, sim_list):
        sim_list.append(f'Source {self._name} {0:.3f} {self._flow:.3f}')
        return [(self._next[0], self._flow)] #restituisco l'elemento attaccatto alla Source e il flusso in uscita dalla Source


class Tap(Element):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._open = False

    def set_status(self, to_open: bool = True) -> None:
        self._open = to_open

    def simulate(self, inflow, sim_list):
        if self._open:
            outflow = inflow
        else:
            outflow = 0
        sim_list.append(f'Source {self._name} {inflow:.3f} {outflow:.3f}')
        return [(self._next[0], outflow)]


class Sink(Element):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def connect(self, elm: "Element") -> None: #sovrascrivo connect() solo in Sink perchè è l'unico elemento che si comporta diversamente dagli altri
        pass   #"Il metodo [ connect() ], se invocato su un oggetto Sink, non ha nessun effetto"

    def simulate(self, inflow, sim_list):
        sim_list.append(f'Source {self._name} {inflow:.3f} {0:.3f}')
        return []


class Split(Element):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._next[1] = None  #aggiungo un'altra chiave al dizionario --> self._next = {0:None, 1:None}

    def connect_at(self, elm: Element, pos: int) -> None:
        self._next[pos] = elm

    def get_outputs(self) -> List[Optional[Element]]:
        return [self._next[0], self._next[1]]

    def simulate(self, inflow, sim_list):
        sim_list.append(f'Source {self._name} {inflow:.3f} {inflow/2:.3f} {inflow/2:.3f}')
        return [(self._next[0], inflow/2), (self._next[1], inflow/2)]
