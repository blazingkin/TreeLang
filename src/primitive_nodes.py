from node_type import NodeType
class PrimitiveNode(NodeType):
    def __init__(self, name, children):
        super(PrimitiveNode, self).__init__(name, children)
    
class IntNode(PrimitiveNode):
    def __init__(self):
        super(IntNode, self).__init__("int", {"primitive": 0})

class StrNode(PrimitiveNode):
    def __init__(self):
        super(StrNode, self).__init__("string", {"primitive": ""})

class BoolNode(PrimitiveNode):
    def __init__(self):
        super(BoolNode, self).__init__("bool", {"primitive": True})

def register_primitive_types():
    BoolNode()
    StrNode()
    IntNode()