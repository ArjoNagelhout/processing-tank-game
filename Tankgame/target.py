class Target(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self._size = 10
    
    def update(self):
        pass
    
    def render(self):
        fill(255, 0, 0)
        rect(self.x-self._size/2, self.y-self._size/2, self._size, self._size)
