from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.list = DoublyLinkedList()
        self.table = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.table:
            spot = self.table[key]
            if spot is not None:
                self.list.move_to_front(spot)
                self.table[key] = self.list.head
                spot.delete()
                
                return list(self.list.head.value.values())[0]
            else:
                return None
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        di = {}
        di[key] = value
        if key not in self.table:
            self.list.add_to_head(di)
            self.table[key] = self.list.head
            #print(list(self.list.head.value.values())[0])

        else:
            spot = self.table[key]
            spot.value = di
            self.list.move_to_front(spot)

        
        if self.list.length > self.limit:
            self.table[list(self.list.tail.value.keys())[0]] = None
            self.list.remove_from_tail()
            

a = LRUCache(3)
a.set('a', 1)
a.set('a', 2)
a.set('b', 2)
a.set('c', 2)
a.set('d', 2)
# a.set('c', 3)
# a.set('d', 4)
# a.set('a', 5)
# a.set('h', 6)
# print(a.get('a'))