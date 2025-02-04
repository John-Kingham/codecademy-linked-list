class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node
    
    def get_value(self):
        return self.value

class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node
    
    def insert_beginning(self, new_head_node_value):
        new_head_node = Node(new_head_node_value)
        new_head_node.set_next_node(self.head_node)
        self.head_node = new_head_node

    def stringify_list(self):
        values_string = ''
        node = self.head_node
        while node is not None:
            if node.get_value() is not None:
                values_string += str(node.get_value()) + '\n'
            node = node.get_next_node()
        return values_string

    def remove_node(self, value_to_remove):
        if self.head_node.get_value() == value_to_remove:
            self.head_node = self.head_node.get_next_node()
            return
        current_node = self.head_node
        next_node = current_node.get_next_node()
        while next_node is not None:
            if next_node.get_value() == value_to_remove:
                current_node.set_next_node(next_node.get_next_node())
                return
            else:
                current_node = next_node
                next_node = current_node.get_next_node()