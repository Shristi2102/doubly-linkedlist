class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None


class circularll:
    def __init__(self):
        self.head = None

    def add_begin(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.nref = new_node
            new_node.pref = new_node
            self.head = new_node


        else:
            new_node = Node(data)
            new_node.nref = self.head
            new_node.pref = self.head.pref
            self.head.pref.nref = new_node
            self.head.pref = new_node
            self.head = new_node

    def print_ll(self):
        if self.head is None:
            print("circular doubly linked list is empty for forward")

        else:
            n = self.head
            while n.nref is not self.head:
                print(n.data, "---")
                n = n.nref
            print(n.data)

    # backward traversal

    def print_ll_reverse(self):
        if self.head is None:
            print("doubly linked list is empty for backward")

        else:
            n = self.head
            while n.nref is not self.head:
                print("sd")
                print(n.data, "---")
                n = n.nref
            print(n.data)

    def add_end(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.nref = new_node
            new_node.pref = new_node
            self.head = new_node

        else:
            n = self.head
            while n.nref is not self.head:
                n = n.nref
            new_node = Node(data)
            new_node.nref = n.nref
            new_node.pref = n
            n.nref = new_node

    def add_after(self, data, x):
        if self.head is None:
            print("dll is empty")
            return

        n = self.head

        while n.nref is not self.head:
            if x == n.data:
                break
            n = n.nref

        new_node = Node(data)
        new_node.nref = n.nref
        new_node.pref = n
        if n.nref is not self.head:
            n.nref.pref = new_node
        n.nref = new_node

    def add_before(self, data , x):
        if self.head is None:
            print("dll is empty")
            return

        n = self.head

        while n.nref is not self.head:
            if x == n.data:
                break
            n = n.nref

        new_node = Node(data)
        new_node.nref = n
        new_node.pref = n.pref
        if n.nref is not self.head:
            n.pref.nref = new_node
        n.pref = new_node


    def delete_begin(self):
        if self.head is None:
            print("dll is empty")
            return
        if self.head.nref is self.head :
            print("fasdyh")
            self.head = None
        else:
            temp = self.head.pref
            # print("temp", temp.data)
            self.head = self.head.nref
            # print(self.head.data)
            temp.nref = self.head
            self.head.pref = temp
            # print(self.head.pref.data)

    def delete_end(self):
        if self.head is None:
            print("dll is empty")
            return
        if self.head.nref is self.head :
            print("fasdyh")
            self.head = None
        else:
            n = self.head
            while n.nref is not self.head:
                n = n.nref

            temp = n.nref
            n.pref.nref = temp

    def delete_by_value(self, x):
        if self.head is None:
            print("dll is empty")
            return
        if self.head.nref is self.head :
            if x is self.head.data:
                self.head = None
        else:
            print("node not present")

        if x == self.head.data:
            temp = self.head.pref
            print(temp.data, "temp")

            self.head = self.head.nref

            temp.nref = self.head
            self.head.pref = temp

            return
        n = self.head
        while n.nref is not self.head:
            if x == n.data:
                break
            n = n.nref
        if n.nref is not self.head:
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:
            if n.data == x:
                temp = n.nref
                n.pref.nref = temp
            else:
                print("node not present")


cll = circularll()
while (True):
    val = int(input("enter the data of nodes"))
    e = int(input("Enter the 1 to insert at begin 2 at end 3 to insert after the node 4 to insert before node"))

    if e == 1:
        cll.add_begin(val)

    elif e == 2:
        cll.add_end(val)

    elif e == 3:
        x = int(input("tell which node after"))
        cll.add_after(val, x)

    elif e == 4:
        x = int(input("tell which node before"))
        cll.add_before(val, x)

        elif e == 5:
      dll.delete_begin()

        elif e == 6:
        dll.delete_end()
    cll.print_ll()
    cll.print_ll_reverse()

