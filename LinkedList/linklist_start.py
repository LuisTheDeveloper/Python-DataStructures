# Linked list example


# the Node class
# implements the node that wil be stored in LList
# simple class that stores a single data field which is named val
# it has only one single next field - indicates this is a singly Linked List
class Node(object):
    def __init__(self, val):
        self.val = val      # stores a single data field
        self.next = None    # only one single next field

# the following methods are used to both get and set 
# the data field and the next field pointer
    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


# the LinkedList class
class LinkedList(object):
    def __init__(self, head=None):
        # head field here / head reference
        self.head = head

        # count field to keep track how many
        # nodes are in the list
        self.count = 0

    def get_count(self):
        return self.count

    # we are inserting items only at the head of the list within this method
    def insert(self, data):
        # Create a new node object
        new_node = Node(data)

        # New node will be set to the current head of this list
        new_node.set_next(self.head)

        # Tell the head to point to the new node and update the count
        self.head = new_node
        self.count += 1

    def find(self, val):
        # Starts at the head of the list - first item
        item = self.head

        # We need to iterate over the nodes until we found the first one
        # that has the matching data argument - val
        while (item != None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()

        return None

    def getHeader(self):
        return self.head

    # The function will delete the node that is at the given index
    def deleteAt(self, idx):
        # Make sure that the index is within the number of existing nodes in the list
        if idx > self.count-1:
            return

        # Check first if we are deleting the current head node, 
        # if so we need to set the new head node to whatever the current head node 
        # is pointing at.
        if idx == 0:
            self.head = self.head.get_next()
            self.count -= 1
        else:
            tempIdxCounter = 0
            node = self.head
            # we need the node just before the one we are deleting because that is the one
            # that has the node that has the next pointer we need to fix
            while tempIdxCounter < idx - 1:
                node = node.get_next()
                tempIdxCounter += 1
                # Once we found the previous node to the one we want to delete, we just set its
                # next field to the node that's after the one we want to delete
            node.set_next(node.get_next().next)
            self.count -= 1


    # utility function that prints the contents of the LList:
    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()


# create a linked list and insert some items
itemlist = LinkedList()
itemlist.insert(38)
itemlist.insert(49)
print("Address for 38 is:", itemlist.find(38))
print("Address for 49 is:", itemlist.find(49))
print("the header address node is: ", itemlist.getHeader())
# itemlist.insert(13)
# itemlist.insert(15)
print("Item count: ", itemlist.get_count())
itemlist.dump_list()

# delete an item
itemlist.deleteAt(0)
print("Current Header node deleted")
print("Item count: ", itemlist.get_count())
itemlist.dump_list()
print("the new header address node is: ", itemlist.getHeader())

itemlist.deleteAt(0)
print("Current Header node deleted")
print("Item count: ", itemlist.get_count())
itemlist.dump_list()
print("the new header address node is: ", itemlist.getHeader())

