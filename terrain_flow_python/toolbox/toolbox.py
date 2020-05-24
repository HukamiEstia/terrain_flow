"""
Parent class for the tool classes used to find the features on the map
"""
from matplotlib import pyplot as plt
from osgeo import gdal
from PIL import Image
import numpy as np

class Toolbox:
    """
    Parent class for the tool classes used to find the features on the map
    """
    def __init__(self, workspace):
        self.work_point = []
        self.work_area = []
        self.workspace = workspace

    def GetWorkPoint(self):
        """return the current working point."""
        return (*self.work_point,)

    def ClearWorkPoint(self):
        """clear work point."""
        self.work_point = []

    def ClearWorkArea(self):
        """clear work area."""
        self.work_area = []

    def Clear(self):
        """clear tool"""
        self.ClearWorkPoint()
        self.ClearWorkArea()

    def UpdateWorkArea(self):
        """Update the list of points surrounding the current working point."""
        if self.work_point == []:
            raise NameError('no current working point')
        else:
            self.work_area = []
            for i in range(3):
                for j in range(3):
                    if ((i,j)!=(1,1) and
                    0 <= self.work_point[0]-1+i < self.workspace.height and
                    0 <= self.work_point[1]-1+j < self.workspace.width):
                        self.work_area.append((self.work_point[0]-1+i,
                                               self.work_point[1]-1+j))
            self.work_area.sort(key=lambda x:self.GetAlt(x))

    def PlaceTool(self, point):
        """set the current working point as the given point"""
        self.work_point = list(point)
        self.UpdateWorkArea()

    def GetWorkArea(self):
        """return the work area"""
        self.UpdateWorkArea()
        return self.work_area

    def NextPoint(self):
        """
        move the working to the next one, it goes through the map
        from left to right and from top to bottom.
        """
        if self.work_point == []:
            self.work_point = [0, 0]
            self.UpdateWorkArea()
            return True
        else:
            if self.work_point[1] < self.workspace.width - 1:
                self.work_point[1] += 1
                self.UpdateWorkArea()
                return True
            elif self.work_point[0] < self.workspace.height - 1:
                self.work_point[0] += 1
                self.work_point[1] = 0
                self.UpdateWorkArea()
                return True
            else:
                self.ClearWorkPoint()
                self.ClearWorkArea()
                return False

    def GetAlt(self, point=None):
        """
        returns the altitude of the given point, if None it return the
        current working point's altitude.
        """
        if point is None:
            point = self.work_point
        return self.workspace.MeasureAltitude(point)
