import numpy as np


class linked_list:
    def __init__(self, value, next_node):
        self.value = value
        self.next = None

    def append(self, insert_value):

        while self.next != None:
            self = self.next

        self.next = linked_list(insert_value)

