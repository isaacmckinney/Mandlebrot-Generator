

class PixelPlot:

    def __init__(self, graphConfig):
        self.config = graphConfig

    
    def createPointsList(self):
        
        newPointsList = []

        xChunkSize = ( self.config.bounds.border[1] - self.config.bounds.border[0] ) / self.config.x

        yChunkSize = ( self.config.bounds.border[3] - self.config.bounds.border[2] ) / self.config.y

        for x in range(self.config.x):
            for y in range(self.config.y):
                newPoint = [ self.config.bounds.border[0] + ( x * xChunkSize ), self.config.bounds.border[3] - ( y * yChunkSize ) ]
                newPointsList.append(newPoint)
        
        return newPointsList
