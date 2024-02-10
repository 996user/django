from py2neo import Graph, Node, Relationship

graph = Graph("neo4j+s://e9146ca1.databases.neo4j.io", auth=("neo4j", "fkbMXPiZCKv_6aLFk5SeDb19qZbi34Q1iekL046mx78"))


# 节点类型

from abc import ABC, abstractmethod

class AbsGNode(ABC):

    @abstractmethod
    def get_data() -> dict:
        pass


LABEL = "标签"
METHOD = "方法"
PACKAGE = "包"
CLASS = "类"
FUNCTION = "函数"
