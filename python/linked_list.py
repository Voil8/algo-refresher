class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        a = '--' + str(self.value) + '--'
        return a


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def push_back(self, node):
        curr = self.tail
        if curr is None:
            self.head = node
            self.tail = node
            self.len += 1
            return 
        
        curr.next = node
        node.prev = curr
        self.tail = node
        self.len += 1

    def push_front(self, node):
        curr = self.head
        if curr is None:
            self.head = node
            self.tail = node
            self.len += 1
            return 

        curr.prev = node
        node.next = curr
        self.head = node

        self.len += 1

    def find_node_(self, value):
        curr = self.head
        while curr is not None:
            if curr.value == value:
                return curr
            curr = curr.next

        
    def remove(self, value):
        node = self.find_node_(value)
        if node is not None:
            if node is self.head:
                self.head = self.head.next
                if self.head is not None:
                    self.head.prev = None
                self.len -= 1
                return 

            if node is self.tail:
                self.tail = self.tail.prev
                if self.tail is not None:
                    self.tail.next = None
                self.len -= 1
                return 

            prev = node.prev
            next_ = node.next

            prev.next = next_
            next_.prev = prev
            self.len -= 1
        
    
    def __repr__(self):
        a = ''
        curr = self.head
        while curr is not None:
            a += repr(curr)
            curr = curr.next
        return a + ':' + str(self.len)



if __name__ == '__main__':
    import random
    s = random.choices(range(100), k=10)
    print('random numbers', s)

    linked_l = LinkedList()
    for j, i in enumerate(s):

        linked_l.push_back(Node(i)) if j%2 else linked_l.push_front(Node(i))
    
    print(linked_l)

    print(f'is {s[-5]} in linked_list', linked_l.find_node_(s[-5]))
    

    linked_l.remove(s[-5])
    linked_l.remove(s[-1])

    print(linked_l)
    print(linked_l.tail)
    


        



        