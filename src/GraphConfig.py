

class GraphConfig:
    
    def __init__(self, bounds, resolution):
        self.bounds = bounds
        self.resolution = resolution
        self.x = self.resolution[0]
        self.y = self.resolution[1]