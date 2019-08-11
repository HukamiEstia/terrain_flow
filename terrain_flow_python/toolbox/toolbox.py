from matplotlib import pyplot as plt
from osgeo import gdal
from PIL import Image
import numpy as np

class Toolbox:

    def __init__(self, workspace):
        self.workPoint = []
        self.workArea = []
        self.workspace = workspace

    def GetWorkPoint(self):
        return (self.workPoint[0], self.workPoint[1])

    def ClearWorkPoint(self):
        self.workPoint = []

    def ClearWorkArea(self):
        self.workArea = []
    
    def Clear(self):
        self.ClearWorkPoint()
        self.ClearWorkArea()

    def UpdateWorkArea(self):

        if self.workPoint == []:
            raise NameError('no current working point')
        else:
            self.workArea = []
            for i in range(3):
                for j in range(3):
                    if ((i,j)!=(1,1)
                    and 0 <= self.workPoint[0]-1+i < self.workspace.yMax
                    and 0 <= self.workPoint[1]-1+j < self.workspace.xMax):
                        self.workArea.append((self.workPoint[0]-1+i,self.workPoint[1]-1+j))
            self.workArea.sort(key=lambda x:self.GetAlt(x))

    def PlaceTool(self, point):
        self.workPoint = list(point)
        self.UpdateWorkArea()

    def GetWorkArea(self):
        self.UpdateWorkArea()
        return self.workArea

    def NextPoint(self):
        if self.workPoint == []:
            self.workPoint = [self.workspace.yMin, self.workspace.xMin]
            self.UpdateWorkArea()
            return True
        else:
            if self.workPoint[1] < self.workspace.xMax - 1:
                self.workPoint[1] += 1
                self.UpdateWorkArea()
                return True
            elif self.workPoint[0] < self.workspace.yMax - 1:
                self.workPoint[0] += 1
                self.workPoint[1] = self.workspace.xMin
                self.UpdateWorkArea()
                return True
            else:
                self.ClearWorkPoint()
                self.ClearWorkArea()
                return False

    def GetAlt(self, point=None):
        if point == None:
            point = self.workPoint
        return self.workspace.MeasureAltitude(point)