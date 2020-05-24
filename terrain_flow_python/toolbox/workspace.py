"""define the workspace class"""

import numpy as np

class Workspace:
    """
    The workspace class define the division of the map handled
    by the current processor.
    """

    def __init__(self, heightmap, initialPoint=(0, 0),
                 height=0, width=0, features=None):

        self.y_min = initialPoint[0]
        self.x_min = initialPoint[1]
        self.y_max = None
        self.x_max = None
        self.width = None
        self.height = None

        self.heightmap = None
        self.fd_matrix = None
        self.in_matrix = None

        self.peaks = None
        self.sinks = None

        if height == 0:
            self.height = heightmap.shape[0] - self.y_min
            self.y_max = heightmap.shape[0]
        else:
            self.y_max = self.y_min + height
            self.height = height

        if width == 0:
            self.width = heightmap.shape[1] - self.x_min
            self.x_max = heightmap.shape[1]
        else:
            self.x_max = self.x_min + width
            self.width = width

        self.heightmap = heightmap[self.x_min:self.x_max,
                                   self.y_min:self.y_max]
        self.fd_matrix = np.empty(self.heightmap.shape, dtype=int)
        self.in_matrix = np.empty(self.heightmap.shape, dtype=int)

    def GetInitialPoint(self):
        """Get the workspace's top left point's coordinates."""
        return [self.y_min, self.x_min]

    def GetMapDimensions(self):
        """Get the dimensions of the workspace."""
        return self.heightmap.shape

    def MeasureAltitude(self, point):
        """Return the altitude of the given point."""
        return self.heightmap[point[0], point[1]]
