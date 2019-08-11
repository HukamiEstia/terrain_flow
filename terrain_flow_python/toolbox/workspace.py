
class Workspace:

    def __init__(self, heightmap, initialPoint = (0, 0),
                 height = 0, width = 0, features = None):
        self.yMin = initialPoint[0]
        self.xMin = initialPoint[1]

        if height == 0:
            self.height = heightmap.shape[0] - self.yMin
            self.yMax = heightmap.shape[0]
        else:
            self.yMax = self.yMin + height

        if width == 0:
            self.width = heightmap.shape[1] - self.xMin
            self.xMax = heightmap.shape[1]
        else:
            self.xMax = self.xMin + width

        self.heightmap = heightmap[self.xMin:self.xMax,
                                   self.yMin:self.yMax]

        self.peaks = None


    def GetInitialPoint(self):
        return [self.yMin, self.xMin]

    def GetMapDimensions(self):
        return self.heightmap.shape

    def MeasureAltitude(self, point):
        return self.heightmap[point[0], point[1]]
