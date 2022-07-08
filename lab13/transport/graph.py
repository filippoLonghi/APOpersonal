import abc
from abc import ABC
from typing import Any, Set, List


class Graph(ABC):

    def __init__(self):
        pass

    @abc.abstractmethod
    def add_node(self, value: Any) -> int:
        pass

    @abc.abstractmethod
    def add_edge(self, value: Any, from_id: int, to_id: int) -> None:
        pass

    @abc.abstractmethod
    def get_node(self, node_id: int) -> Any:
        pass

    @abc.abstractmethod
    def get_edge(self, from_id: int, to_id: int) -> Any:
        pass

    @abc.abstractmethod
    def is_connected(self, from_id: int, to_id: int) -> bool:
        pass

    @abc.abstractmethod
    def get_parents(self, node_id: int) -> Set[int]:
        pass

    @abc.abstractmethod
    def get_children(self, node_id: int) -> Set[int]:
        pass

    @abc.abstractmethod
    def find_path(self, from_id: int, to_id: int) -> List[int]:
        pass

class GraphCreator:
    def __init__(self):
        raise NotImplementedError

    @staticmethod
    def get_empty_graph() -> Graph:
        return GraphMatrix()

class GraphMatrix(Graph):

    def __init__(self):
        super().__init__()
        self._nodes = []
        self._matrix = []

    def add_node(self, value: Any) -> int:
        node = Node(value)
        self._nodes.append(node)

        self._matrix.append([])
        for elm in self._matrix:
            for i in range(len(self._matrix)):
                while len(elm) < len(self._matrix):
                    elm.append(0)

        return self._nodes.index(node)

    def add_edge(self, value: Any, from_id: int, to_id: int) -> None:
        edge = Edge(value, from_id, to_id)
        self._matrix[from_id][to_id] = edge
        self._nodes[from_id].children = to_id
        self._nodes[to_id].parents = from_id

    def get_node(self, node_id: int) -> Any:
        return self._nodes[node_id].value

    def get_edge(self, from_id: int, to_id: int) -> Any:
        return self._matrix[from_id][to_id].value

    def is_connected(self, from_id: int, to_id: int) -> bool:
        return self._matrix[from_id][to_id] != 0

    def get_parents(self, node_id: int) -> Set[int]:
        # nodes = set()
        # for i in range(len(self._matrix)):
        #     if self._matrix[i][node_id] != 0:
        #         nodes.add(i)
        # return nodes
        return set(self._nodes[node_id].parents)

    def get_children(self, node_id: int) -> Set[int]:
        # nodes = set()
        # for i in range(len(self._matrix[node_id])):
        #     if self._matrix[node_id][i] != 0:
        #         nodes.add(i)
        # return nodes
        return set(self._nodes[node_id].children)

    # def find_path(self, from_id: int, to_id: int) -> List[int]:
    #     start = self._nodes[from_id]
    #     stop = self._nodes[to_id]
    #     key_list = []
    #     self._depth_first(start, stop, key_list, count = 0)
    #     return key_list
    #
    # def _depth_first(self, current, stop, key_list, count):
    #     if current is stop:
    #         key_list.insert(0, self._nodes.index(current))
    #         return
    #     elif count >= len(self):
    #         return
    #     if current.children != []:
    #         self._depth_first(self._nodes[current.children[0]], stop, key_list, count + 1)
    #     else:
    #         return
    #     if len(key_list) >= 1:
    #         key_list.insert(0, self._nodes.index(current))
    #     else:
    #         key_list = []

    def find_path(self, from_id: int, to_id: int) -> List[int]:
        start = self._nodes[from_id]
        # stop = self._nodes[to_id]
        key_list = [from_id]
        visited = [from_id]
        if self._depth_first(start, to_id, key_list, visited):
            return key_list
        else:
            return []

    def _depth_first(self, current, stop, key_list, visited):
        for node_id in current.children:
            if node_id not in visited:
                key_list.append(node_id)
                visited.append(node_id)
                if node_id == stop:
                    return True
                if self._depth_first(self._nodes[node_id], stop, key_list, visited):
                    return True
                key_list.pop()
        return False

    def __len__(self):
        return len(self._nodes)

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []
        self._parents = []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, from_id):
        self._children.append(from_id)

    @property
    def parents(self):
        return self._parents

    @parents.setter
    def parents(self, to_id):
        self._parents.append(to_id)

class Edge:
    def __init__(self, value, from_id, to_id):
        self._value = value
        self._from_id = from_id
        self._to_id = to_id

    @property
    def value(self):
        return self._value

    @property
    def from_id(self):
        return self._from_id

    @property
    def to_id(self):
        return self._to_id