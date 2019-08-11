from toolbox.baseTool import BaseTool
from toolbox.workspace import Workspace
from toolbox import dataUtils

class Artist():
    
    def __init__(self, data, initialPoint = (0, 0),
                 height = 0, width = 0):
        heightmap = dataUtils.load_heightmap(data)
        self.workspace = Workspace(heightmap, initialPoint=initialPoint,
                                   height=height, width=width)
        self.baseTool = BaseTool(self.workspace)

    def FindPeaks(self):
        Peaks = []
        while self.baseTool.NextPoint():
            if self.baseTool.DetectPeak():
                location = self.baseTool.GetWorkPoint()
                altitude = self.workspace.MeasureAltitude(location)
                Peaks.append({"location": location,
                              "altitude": altitude})
        self.workspace.peaks = Peaks
        