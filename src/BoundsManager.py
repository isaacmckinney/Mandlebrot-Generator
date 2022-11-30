
class GraphBorder:

    def __init__(self, x1, x2, y1, y2):
        self.border = [x1, x2, y1, y2]
        self.lineage = []
    
    def setBorder(self, newBorder):
        self.border = newBorder

    def zoom(self, sector):

        convertedSector = sector


        changes = self.border.copy()
        if convertedSector in [9, 6, 3]:
            changes[0] = self.border[0] + ( 2 * ( ( self.border[1] - self.border[0] ) / 3 ) )
        if convertedSector in [8, 5, 2]:
            changes[0] = self.border[0] + ( ( self.border[1] - self.border[0] ) / 3 )
            changes[1] = self.border[1] - ( ( self.border[1] - self.border[0] ) / 3 )
        if convertedSector in [7, 4, 1]:
            changes[1] = self.border[1] - ( 2 * ( ( self.border[1] - self.border[0] ) / 3 ) )
        if convertedSector in [7, 8, 9]:
            changes[2] = self.border[2] + ( 2 * ( ( self.border[3] - self.border[2] ) / 3 ) )
        if convertedSector in [4, 5, 6]:
            changes[2] = self.border[2] + ( ( self.border[3] - self.border[2] ) / 3 )
            changes[3] = self.border[3] - ( ( self.border[3] - self.border[2] ) / 3 )
        if convertedSector in [1, 2, 3]:
            changes[3] = self.border[3] - ( 2 * ( ( self.border[3] - self.border[2] ) / 3 ) )
        
        print("Previous Border: \n")
        print("Bounds: [\n  " + str(self.border[0]) + ",\n  " + str(self.border[1]) + ",\n  " + str(self.border[2]) + ",\n  " + str(self.border[3]) + "\n]")

        print("New Border: \n")
        print("Bounds: [\n  " + str(changes[0]) + ",\n  " + str(changes[1]) + ",\n  " + str(changes[2]) + ",\n  " + str(changes[3]) + "\n]")

        self.lineage.append(self.border.copy())
        self.border = changes
        return self.border
    
    def undoZoom(self):
        if len(self.lineage) != 0:
            self.border = self.lineage[len(self.lineage) - 1]
            self.lineage.pop()
        else:
            print("No zooms to undo")