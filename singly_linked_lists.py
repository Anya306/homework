class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None


class LinkedList:
    def __init__(self):
        self.start_node = None

    def insert_in_emptylist(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("list is not empty")

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.nref = self.start_node
        self.start_node = new_node

    def insert_at_end(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node

    def insert_after_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                n.nref = new_node

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return

        # Если элемент в начале списка
        if self.start_node.item == x:
            self.insert_at_start(data)
            return

        n = self.start_node
        while n.nref is not None:
            if n.nref.item == x:
                break
            n = n.nref
        if n.nref is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.nref = n.nref
            n.nref = new_node

    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, "->", end=" ")
                n = n.nref
            print("None")

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        self.start_node = self.start_node.nref

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            self.start_node = None
            return
        n = self.start_node
        while n.nref.nref is not None:
            n = n.nref
        n.nref = None

    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return

        if self.start_node.item == x:
            self.start_node = self.start_node.nref
            return

        n = self.start_node
        while n.nref is not None:
            if n.nref.item == x:
                n.nref = n.nref.nref
                return
            n = n.nref
        print("Element not found")

    def reverse_linked_list(self):
        if self.start_node is None:
            print("The list has no element to reverse")
            return

        q = self.start_node
        p = None

        while q is not None:
            next_node = q.nref
            q.nref = p
            p = q
            q = next_node

        self.start_node = p

    def search_element(self, x):
        if self.start_node is None:
            return False

        q = self.start_node
        while q is not None:
            if q.item == x:
                return True
            q = q.nref
        return False


    def ai_an(self):
        if self.start_node is None:
            return
        else:
            x = self.start_node
            while x.nref is not None:
                x = x.nref

            an = x.item
            n = self.start_node
            while n is not None:
                print(n.item - an, end=" ")
                n = n.nref


ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_end(4)
ll.insert_at_end(5)
ll.insert_at_end(6)
ll.insert_at_end(7)
print(ll.search_element(9))
# задача 1

print(ll.ai_an())
# задача 3