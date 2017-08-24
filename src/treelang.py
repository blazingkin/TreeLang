from node_transformation import *
from node_type import *
from primitive_nodes import *
from instance_node import *
import sys, os
class TreeLangRuntime:
    def __init__(self, root):
        self.root = root

    def __eq__(self, other):
        return type(other) == TreeLangRuntime and self.root == other.root

    def __repr__(self):
        return "RUNTIME OBJECT"

    # This will read through the type definition directory and register all user types
    def find_and_register_types(self, dir):
        types_and_children = {}
        for path, subdirs, files in os.walk(dir):
            for name in files:
                file = open(os.path.join(dir, name), 'r')
                type_name = name.split(".")[0]
                children = []
                for line in file:
                    children.append(line.strip())
                types_and_children[type_name] = children
        self.register_types(types_and_children)
        
        
    # This actually registers all of the types
    def register_types(self, types_and_children):
        register_primitive_types()
        for key, val in types_and_children.items():
            NodeType(key)
        for key, val in types_and_children.items():
            children = {}
            for child in val:
                children[child.split("-")[0].strip()] = find_type(child.split("-")[1].strip())
            find_type(key).set_children(children)


    def run_transformation(self, node, transformation):
        return transformation.transform(node)

    def mark_for_transformation(self, node, transformation):
        pass


def add_first_and_second_primitives(x):
    return x.get_child("first") + x.get_child("second")

def mul_first_and_second(x):
    return x.get_child("first") * x.get_child("second")

def display_as_tuple(x):
    return "({!r}, {!r})".format(x.get_child("first"), x.get_child("second"))

def display_int_and_str(x):
    return "int - {!r}, str - {!r}".format(x.get_child("int"), x.get_child("str"))

# Add 2 and 3
tuple_node_type = NodeType("Tuple", {"first": IntNode(), "second": IntNode()})



if ('__main__' == __name__):
    runtime = TreeLangRuntime(None)
    runtime.find_and_register_types('../type_definitions')
    add_node = InstanceNode(find_type("Tuple"), {"first": int_node(2), "second": int_node(3)})
    add_trans = NodeTransformation("Add Tuple", find_type("Tuple"), IntNode(), {"primitive": add_first_and_second_primitives})
    disp_trans = NodeTransformation("Display Tuple", find_type("Tuple"), StrNode(), {"primitive": display_as_tuple})
    mul_tran = NodeTransformation("Mul Tuple", find_type("Tuple"), IntNode(), {"primitive": mul_first_and_second})
    disp_int_and_str = NodeTransformation("DispIandS", find_type("IntAndStr"), StrNode(), {"primitive": display_int_and_str})
    int_and_str_node = InstanceNode(find_type("IntAndStr"), {"int": int_node(7), "str": str_node("Hello!")})
    print(runtime.run_transformation(add_node, add_trans).get_child())
    print(runtime.run_transformation(add_node, disp_trans).get_child())
    print(runtime.run_transformation(add_node, mul_tran).get_child())
    print(runtime.run_transformation(int_and_str_node, disp_int_and_str).get_child())