from typing import List, Optional
from abc import ABC


class Element(ABC):
    def __init__(self, name: str) -> None:
        self._name = name

    def get_name(self) -> str:
        return self._name

    def connect(self, elm: "Element") -> None:
        return None

    def check_connection(self, elm):
        return None

    def get_output(self) -> Optional["Element"]:
        return None


class Source(Element):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._output = None #Tap (rubinetto) or Sink (scarico) or Split
        self._flow = 0

    def connect(self, elm):
        self._output = elm

    def check_connection(self, elm):
        if self._output == elm:
            return True

    def get_output(self):
        return self._output

    def set_flow(self, flow: float) -> None:
        self._flow = flow

    def get_flow(self):
        return self._flow


class Tap(Element):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._output = None #Split or Sink (scarico)
        self._status = None

    def connect(self, elm):
        self._output = elm

    def check_connection(self, elm):
        if self._output == elm:
            return True

    def get_output(self):
        return self._output

    def set_status(self, to_open: bool = True) -> None:
        self._status = to_open
        return self._status

    def get_status(self):
        return self._status


class Sink(Element):
    def __init__(self, name: str) -> None:
        super().__init__(name)


class Split(Element):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._outputs = [None,None]  #Sinks

    def connect_at(self, elm: Element, pos: int) -> True:
        self._outputs[pos] = elm

    def check_connection(self, elm):
        if self._outputs[0] == elm or self._outputs[1] == elm:
            return True

    def get_outputs(self) -> List[Optional[Element]]:
        return self._outputs
