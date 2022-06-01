from correzione.hydraulics.elements import Element, Source, Tap, Sink, Split
from typing import List


class HSystem:
    def __init__(self) -> None:
        self._elements = []

    def add_element(self, elm: Element) -> None:
        self._elements.append(elm)

    def get_elements(self) -> List[Element]:
        return self._elements

    def simulate(self) -> List[str]:
        sim_list = []
        to_simulate = [] #ha elementi del tipo tupla (elm, inflow)
        for elm in self._elements: #cerco il primo elemento del sistema (Source)
            if isinstance(elm, Source):
                to_simulate += elm.simulate(None, sim_list) #il metodo .simulate() aggiunge alla lista sim_list la simulazione
        while to_simulate: #finchè la lista to_simulate ha degli elementi faccio le simulazioni
            elm, inflow = to_simulate[-1] #simulo l'ultimo elemento aggiunto alla lista
            to_simulate = to_simulate[:-1] #tolgo l'ultimo elemento della lista (ovvero quello appena simulato)
            to_simulate += elm.simulate(inflow, sim_list)
        return sim_list



