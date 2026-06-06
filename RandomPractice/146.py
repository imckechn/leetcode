class Linkedlist:
    def __init__(self, val, key, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.head = None #Newest element
        self.tail = None #Oldest element
        self.values = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        if (key in self.values.keys()):
            if (self.head.key == key):
                return self.head.val
            
            elif (self.tail.key == key):
                elem = self.tail
                self.tail = self.tail.prev
                self.tail.next = None
                elem.prev = None

                self.head.prev = elem
                elem.next = self.head
                self.head = elem
                return self.head.val

            elem = self.values[key]
            prev = elem.prev
            next = elem.next

            next.prev = prev
            prev.next = next

            elem.prev = None
            elem.next = self.head
            self.head.prev = elem

            self.head = elem
            return self.head.val
        
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if (key in self.values.keys()):
            ll = self.values[key]
            ll.val = value

            if (ll == self.head):
                return

            prev = ll.prev
            next = ll.next

            next.next = prev
            prev.prev = next

            ll.prev = None
            ll.next = self.head
            self.head = ll

        else:
            ll = Linkedlist(value, key)
            self.values[key] = ll

            if (len(self.values.keys()) <= self.cap):
                #Adding a new element
                if (self.head == None):
                    self.head = ll
                    self.tail = ll

                else:
                    self.tail.next = ll
                    ll.prev = self.tail
                    self.tail = ll

            else:
                oldTail = self.tail
                self.tail = oldTail.prev
                self.values.pop(oldTail.key)

                ll.next = self.head
                self.head = ll
