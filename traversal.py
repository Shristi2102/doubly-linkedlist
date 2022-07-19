class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class doublyll:
    def __init__(self):
        self.head = None

# forward traversal
    def print_ll(self):
        if self.head is None:
            print("doubly linked list is empty for forward")

        else:
            n = self.head
            while n is not None:
                print(n.data, "---", end=" ")
                n = n.nref

#backward traversal
    def print_ll_reverse(self):
        if self.head is None:
            print("doubly linked list is empty for backward")

        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, "---")
                n = n.pref

dll = doublyll()
dll.print_ll()
dll.print_ll_reverse()

