class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class doublyll:
    def __init__(self):
        self.head = None

    def add_begin(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node

        else:
            new_node = Node(data)
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

# forward traversal
    def print_ll(self):
        if self.head is None:
            print("doubly linked list is empty for forward")

        else:
            n = self.head
            while n is not None:
                print(n.data, "---")
                n = n.nref

# backward traversal
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

    def add_end(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            new_node = Node(data)
            n.nref = new_node
            new_node.pref = n


    def add_after(self, data, x):
        if self.head is None:
            print("dll is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("node not found")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node

   

dll = doublyll()
while (True):
    val = int(input("enter the data of nodes"))
    e = int(input("Enter the 1 to insert at begin 2 at end 3 to insert after the node 4 to insert before node"))

    if e == 1:
        dll.add_begin(val)

    elif e == 2:
        dll.add_end(val)

    else:
        x = int(input("tell which node after"))
        dll.add_after(val, x)

   
    dll.print_ll()
