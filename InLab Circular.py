#circular insertion
# This function is only for empty list
def addToEmpty(self, data):
    if (self.last != None):
        return self.last

    # Creating the newnode temp
    temp = (data)
    self.last = temp

    # Creating the link
    self.last.next = self.last
    return self.last

#circular deletion
# Function to print nodes in a given
# circular linked list
def printList(head):
    temp = head
    if (head != None):
        while (True):
            print(temp.data, end=" ")
            temp = temp.next
            if (temp == head):
                break
    print()

#circular traversal
# Function to print nodes in a given Circular linked list
def printList(self):
    temp = self.head

    # If linked list is not empty
    if self.head is not None:
        while (True):

            # Print nodes till we reach first node again
            print(temp.data, end=" ")
            temp = temp.next
            if (temp == self.head):
                break
