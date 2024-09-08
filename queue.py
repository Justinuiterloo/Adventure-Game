class Queue:

    def __init__(self):
        self._data = []

    def size(self):
        return len(self._data)
    # add element to back of queue
    def enqueue(self, element):
        self._data.append(element)

    # remove and return element from front of queue
    def dequeue(self):
        assert self.size() > 0
        return self._data.pop(0)

    def empty(self):
        self._data.clear()

    def peek(self):
        return self._data[0]

q = Queue()
q.enqueue(3)
q.enqueue(1)


print(q.dequeue())
