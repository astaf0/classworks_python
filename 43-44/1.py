class Counter:
    def __init__(self):
        self.counter = 0

    def _update_count(self):
        self.counter = 0
        return self.counter

    def decrement(self):
        self.counter -= 1
        return self.counter

    def increment(self):
        self.counter += 1

        if self.counter > 10:
            self._update_count()
        return self.counter


counter = Counter()
print(counter.decrement())
print(counter.increment())
print(counter.increment())
print(counter.increment())
print(counter.increment())
print(counter.increment())
print(counter.increment())
print(counter.increment())
print(counter.increment())
print(counter.increment())
print(counter.increment())
print(counter.increment())
print(counter.increment())
print(counter.increment())
print(counter.increment())
print(counter.increment())
print(counter.increment())
print(counter.increment())