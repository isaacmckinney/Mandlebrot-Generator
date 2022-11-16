import BoundsManager

class GraphConfig:
    
    def __init__(self, bounds, resolution):
        self.bounds = BoundsManager.GraphBorder(bounds[0], bounds[1], bounds[2], bounds[3])
        self.resolution = resolution
        self.x = self.resolution[0]
        self.y = self.resolution[1]