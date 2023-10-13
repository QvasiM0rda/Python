class Queue:
    def __init__(self, *args):
        self._queue = list(args)

    
    def add(self, *args):
        self._queue.extend(args)


    def pop(self):
        return self._queue.pop(0) if self._queue else None


    def __str__(self):
        return " -> ".join(str(elem) for elem in self._queue)


    def __eq__(self, other):
        if isinstance(other, Queue):
            return self._queue == other._queue
        return NotImplemented


    def __ne__(self, other):
        if isinstance(other, Queue):
            return self._queue != other._queue
        return NotImplemented


    def __add__(self, other):
        if isinstance(other, Queue):
            return Queue(*self._queue, *other._queue)
        return NotImplemented


    def __iadd__(self, other):
        if isinstance(other, Queue):
            self.add(*other._queue)
            return self
        return NotImplemented


    def __rshift__(self, n):
        if isinstance(n, int):
            return Queue(*self._queue[n:])
        return NotImplemented
