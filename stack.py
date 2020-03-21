class Stack:
    def __init__(self):
        self._data = []

    def push(self):
        pass

    def pop(self):
        pass

    def top(self):
        if self.empty():
            return None
        return self._data[-1]

    def empty(self):
        return not self._data


if __name__ == '__main__':
    pass
