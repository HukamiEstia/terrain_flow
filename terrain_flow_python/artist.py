from toolbox.baseTool import BaseTool
from toolbox.workspace import Workspace
from toolbox import dataUtils
import features

class Artist():
    
    def __init__(self, data, initialPoint = (0, 0),
                 height = 0, width = 0):

        heightmap = dataUtils.load_heightmap(data)
        self.workspace = Workspace(heightmap, initialPoint=initialPoint,
                                   height=height, width=width)
        self.baseTool = BaseTool(self.workspace)

    def DisplayWorkspace(self):

        drawnHeightmap = dataUtils.draw_heightmap(self.workspace.heightmap)
        drawnPeaks = self.workspace.peaks.Draw()
        drawnSinks = self.workspace.sinks.Draw()
        data = [drawnHeightmap,
                drawnPeaks,
                drawnSinks]

        dataUtils.display_map(data)
        
    def FindPeaks(self):

        peaks = features.Peaks(*self.workspace.GetMapDimensions())

        while self.baseTool.NextPoint():
            if self.baseTool.DetectPeak():
                location = self.baseTool.GetWorkPoint()
                altitude = self.workspace.MeasureAltitude(location)
                peaks.AddPeak(location, altitude)

        self.workspace.peaks = peaks

    def FindSinks(self):

        sinks = features.Sinks(*self.workspace.GetMapDimensions())

        while self.baseTool.NextPoint():
            if self.baseTool.DetectSink():
                location = self.baseTool.GetWorkPoint()
                altitude = self.workspace.MeasureAltitude(location)
                sinks.AddSink(location, altitude)

        self.workspace.sinks = sinks

    def ComputeFD_Matrix(self):
        
        while self.baseTool.NextPoint():
            self.baseTool.AssignDirection()
