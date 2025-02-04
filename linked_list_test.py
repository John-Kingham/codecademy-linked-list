import unittest
from linked_list import *

class TestLinkedList(unittest.TestCase):

    def test_node_linking(self):
        node1 = Node(1)
        node2 = Node(2)
        node1.set_next_node(node2)
        self.assertEqual(node1.get_next_node(), node2)      

    def test_new_linked_list(self):
        test_value = 3
        ll = LinkedList(test_value)
        self.assertEqual(ll.get_head_node().get_value(), test_value)

    def test_insert_beginning(self):
        ll = LinkedList(3)
        ll.insert_beginning(5)
        self.assertEqual(ll.get_head_node().get_value(), 5)

    def test_stringify_list(self):
        ll = LinkedList(30)
        ll.insert_beginning(20)
        ll.insert_beginning(10)
        self.assertEqual(ll.stringify_list(), '10\n20\n30\n')

    def test_remove_node(self):
        ll = LinkedList(10)
        ll.insert_beginning(20)
        ll.insert_beginning(30)
        ll.remove_node(20)
        self.assertEqual(ll.get_head_node().get_next_node().get_value(), 10)

if __name__ == '__main__':
    unittest.main()
