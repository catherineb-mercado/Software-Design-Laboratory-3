#singly insertion

def insert(self, data):
    new_node = (data)
    new_node.set_next(self.head)
    self.head = new_node

#singly deletion

def delete(self, data):
    current = self.head
    previous = None
    found = False
    while current and found is False:
        if current.get_data() == data:
            found = True
        else:
            previous = current
            current = current.get_next()
        if current is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

