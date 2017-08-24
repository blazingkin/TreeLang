class NodeType:
    def __init__(self, name, children={}):  # Key for dictionary is alias, value is NodeType
        self.name = name
        self.children = children
        _node_type_lookup[name] = self

    def __eq__(self, other):
        return type(other) == NodeType and self.name == other.name and self.children == other.children

    def __repr__(self):
        return self.name

    def set_children(self, children={}):
        self.children = children

_node_type_lookup = {}
def find_type(name):
    if not name in _node_type_lookup:
        raise ValueError("{!r} node type does not exist".format(name))
    return _node_type_lookup[name]