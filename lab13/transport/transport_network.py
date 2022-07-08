from typing import List
from transport.graph import GraphCreator


class Stop:

    def __init__(self, name, latitude, longitude):
        self._name = name
        self._latitude = latitude
        self._longitude = longitude

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        self._latitude = latitude

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        self.longitude = longitude


class BusNetwork:
    def __init__(self) -> None:
        self._stops = []
        self._graph = GraphCreator.get_empty_graph()

    def load_stops(self, f_name: str) -> None:
        inputFile = open(f_name, "r")
        for line in inputFile:
            line = line.strip()
            wordList = line.split(",")
            stop = Stop(wordList[0], float(wordList[1]), float(wordList[2]))
            self._stops.append(wordList[0])
            self._graph.add_node(stop)
        inputFile.close()

    def load_connections(self, f_name: str) -> None:
        inputFile = open(f_name, "r")
        for line in inputFile:
            line = line.strip()
            wordList = line.split(",")
            self._graph.add_edge(wordList[0], self._stops.index(wordList[1]), self._stops.index(wordList[2]))
        inputFile.close()
        pass

    def get_stop(self, stop_name: str) -> Stop:
        return self._graph.get_node(self._stops.index(stop_name)) #value = Stop()

    def get_line(self, from_stop_name: str, to_stop_name: str) -> str:
        return self._graph.get_edge(self._stops.index(from_stop_name), self._stops.index(to_stop_name)) #value = line

    def compute_itinerary(self, from_stop_name: str, to_stop_name: str) -> List[str]:
        fermate = self._graph.find_path(self._stops.index(from_stop_name), self._stops.index(to_stop_name))
        itinerary = []
        for i in range(len(fermate)):
            if i == len(fermate) - 1:
                string = f'{self._stops[fermate[i]]} -> END'
            else:
                string = f'{self._stops[fermate[i]]} -> {self.get_line(self._stops[fermate[i]], self._stops[fermate[i+1]])}'
            itinerary.append(string)
        return itinerary



