# We will use a basic node that contains data and one link to another node.
# The node’s data will be specified when creating the node and immutable (can’t be updated).
# The link will be optional at initialization and can be updated.


class Node:
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node

    def set_link_node(self, link_node):
        self.link_node = link_node

    def get_link_node(self):
        return self.link_node

    def get_value(self):
        return self.value


statement1 = Node("likes to walk")
statement2 = Node("likes to watch movies")
statement3 = Node("likes to code")

statement3.set_link_node(statement2)
statement1.set_link_node(statement3)

dots_data = statement1.get_link_node().get_value()
wackos_data = statement3.get_link_node().get_value()

print(dots_data)
print(wackos_data)