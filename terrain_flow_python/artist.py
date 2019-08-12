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
        drawnPeaks = dataUtils.draw_peaks(self.workspace.peaks)
        data = [drawnHeightmap, drawnPeaks]

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

        sinks = []

        while self.baseTool.NextPoint():
            if self.baseTool.DetectSink():
                location = self.baseTool.GetWorkPoint()
                altitude = self.workspace.MeasureAltitude(location)
                sinks.append({"location": location,
                              "altitude": altitude})