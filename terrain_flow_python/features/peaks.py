import numpy as np
from .featureLayer import FeatureLayer

class Peak():

    __slots__ = ('location', 'altitude')

    def __init__(self, location, altitude):
        self.location = location
        self.altitude = altitude

class Peaks(FeatureLayer):

    __slots__ = (('height', 'width', 'peaks'))

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.peaks = []

    def __len__(self):
        return len(self.peaks)

    def AddPeak(self, location, altitude):
        self.peaks.append(Peak(location, altitude))

    def Draw(self):
        x = []
        y = []
        z = []
        for peak in self.peaks:
            x.append(30*peak.location[1])
            y.append(30*peak.location[0])
            z.append(peak.altitude)
        data = go.Scatter3d(x=x, y=y, z=z,
                            mode='markers',
                            marker={"size": [Z/50 for Z in z],
                                    "color":z,
                                    "colorscale":'Reds',
                                    "opacity":1,
                                    "symbol":'diamond'})
        return data