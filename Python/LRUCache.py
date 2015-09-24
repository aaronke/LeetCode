# beat 100% running time
class LRUCache(object):
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = LinkedNode(-1,-1)
        self.tail = LinkedNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashmap = {}

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.hashmap:
            node = self.hashmap[key]
            self.move_2_head(node)
            return node.val
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.move_2_head(node)
        else:
            if len(self.hashmap) == self.capacity:
                del self.hashmap[self.tail.prev.key]
                self.delete_last()
            node = LinkedNode(key,value)
            self.hashmap[key] = node
            self.insert_2_head(node)

    def move_2_head(self,node):
        # pick node out
        node.prev.next = node.next
        node.next.prev = node.prev
        # insert to head
        self.insert_2_head(node)

    def insert_2_head(self,node):        
        self.head.next.prev = node
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        
    def delete_last(self):
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        
        
class LinkedNode:
    
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
