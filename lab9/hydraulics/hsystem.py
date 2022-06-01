from hydraulics.elements import Element, Source, Tap, Sink, Split
from typing import List


class HSystem:
    def __init__(self) -> None:
        self._elements = []
        self._connected_elements = []

    def add_element(self, elm: Element) -> None:
        self._elements.append(elm)

    def get_elements(self) -> List[Element]:
        return self._elements

    def _HSystem_connections(self):
        self._connected_elements = []
        # for element in self._elements:
        #     for i in self._elements:
        #         if element.check_connection(i) and element not in self._connected_elements:
        #             self._connected_elements.append(element)
        #             if isinstance(element, Split):
        #                 if element.get_outputs()[0] != None:
        #                     self._connected_elements.append(element.get_outputs()[0])
        #                 if element.get_outputs()[1] != None:
        #                     self._connected_elements.append(element.get_outputs()[1])
        #             if isinstance(element, Tap) and isinstance(i, Sink):
        #                 self._connected_elements.append(i)


    def simulate(self) -> List[str]:
        self._HSystem_connections()
        HSystem_info = []
        if isinstance(self._connected_elements[0], Source) and isinstance(self._connected_elements[-1], Sink):
            prev_out_flow = 0
            for element in self._connected_elements:
                if isinstance(element, Source):
                    class_name = "Source"
                    in_flow = 0
                    out_flow = f'{element.get_flow():.3f}'
                    prev_out_flow = element.get_flow()
                if isinstance(element, Tap):
                    class_name = "Tap"
                    if element.get_status() == True:
                        in_flow = prev_out_flow
                        out_flow = f'{prev_out_flow:.3f}'
                    else:
                        in_flow = prev_out_flow
                        out_flow = f'{0:.3f}'
                        prev_out_flow = 0
                if isinstance(element, Sink):
                    class_name = "Sink"
                    in_flow = prev_out_flow
                    out_flow = f'{0:.3f}'
                if isinstance(element, Split):
                    class_name = "Split"
                    in_flow = prev_out_flow
                    if element.get_outputs()[0] != None and element.get_outputs()[1] != None:
                        out_flow = f'{prev_out_flow/2:.3f} {prev_out_flow/2:.3f}'
                        prev_out_flow = prev_out_flow/2
                    else:
                        out_flow = f'{prev_out_flow:.3f}'
                element_info = f'{class_name} {element.get_name()} {in_flow:.3f} {out_flow}'
                HSystem_info.append(element_info)
        return HSystem_info