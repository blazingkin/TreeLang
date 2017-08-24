from primitive_nodes import *
class InstanceNode:
    def __init__(self, type, children={}):  # Key for dictionary is alias, Value is another instance node
        self.type = type
        self.children = children

    def __eq__(self, other):
        return type(other) == InstanceNode and self.type == other.type and self.children == other.children

    def __repr__(self):
        return "<{!r}>".format(self.type)

    def get_child(self, name="primitive"):
        if not name in self.children:
            raise ValueError("{!r} has no property {!r}".format(self, name))
        if name != "primitive" and isinstance(self.children[name].type, PrimitiveNode):
            return self.children[name].children["primitive"]
        return self.children[name]

def int_node(_int):
    return InstanceNode(IntNode(), {"primitive": _int})

def str_node(_str):
    return InstanceNode(StrNode(), {"primitive": _str})

def bool_node(_bool):
    return InstanceNode(BoolNode(), {"primitive": _bool})