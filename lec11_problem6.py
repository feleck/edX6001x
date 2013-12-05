class Queue(object):
    def __init__(self):
        self.vals = []
    def insert(self, x):
        if not x in self.vals:
            self.vals.append(x)
    
    def remove(self):
        try:
            return self.vals.pop()
        except:
            raise ValueError()
            
queue = Queue()
queue.insert(5)
queue.insert(6)
queue.insert(7)
print queue.vals

queue.remove()

print queue.vals
