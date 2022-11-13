

class PixelPlot:

    def __init__(self, graphConfig):
        self.config = graphConfig

        self.pointsList = None

    
    def createPointsList(self):
        
        newPointsList = []

        xChunkSize = ( self.config.bounds[1] - self.config.bounds[0] ) / self.config.x

        yChunkSize = ( self.config.bounds[3] - self.config.bounds[2] ) / self.config.y

        for x in range(self.config.x):
            for y in range(self.config.y):
                newPoint = [ self.config.bounds[0] + ( x * xChunkSize ), self.config.bounds[3] - ( y * yChunkSize ) ]
                newPointsList.append(newPoint)
        
        return newPointsList
