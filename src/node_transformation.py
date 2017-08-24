from instance_node import InstanceNode

class NodeTransformation:
    def __init__(self, name, input_type, output_type, functions={}):
        self.name = name
        self.input_type = input_type
        self.output_type = output_type
        self.functions = functions  # Key is output_node child alias, value is a lambda that takes the input_node
        for alias in output_type.children:
            if not alias in functions:
                raise TypeError("{!r} did not have a function to generate {!r} child {!r}".format(self, output_type, alias))

    def __eq__(self, other):
        return type(other) == NodeTransformation and self.name == other.name and self.input_type == other.input_type and self.output_type == other.output_type   
    
    def __repr__(self):
        return "{!r} [{!r} => {!r}]".format(self.name, self.input_type, self.output_type)

    def transform(self, input_node):
        if input_node.type != self.input_type:
            raise TypeError("Cannot apply transformation {!r} to input node {!r}".format(self, input_node))
        newvals = {}
        for alias, func in self.functions.items():
            newvals[alias] = func(input_node)
        return InstanceNode(self.output_type, newvals)