"""classes to store all the peaks"""

import numpy as np
from .featureLayer import FeatureLayer
import plotly.graph_objects as go

class Peak():
    """store one peak's location and altitude"""

    __slots__ = ('location', 'altitude')

    def __init__(self, location, altitude):
        self.location = location
        self.altitude = altitude

class Peaks(FeatureLayer):
    """store all the peaks into a array"""

    __slots__ = (('height', 'width', 'peaks'))

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.peaks = []

    def __len__(self):
        return len(self.peaks)

    def AddPeak(self, location, altitude):
        """
        create a peak of given location and altitude
        and append it to the list of peaks.
        """
        self.peaks.append(Peak(location, altitude))

    def Draw(self):
        """
        plot the peaks with plotly
        """
        x_coord = []
        y_coord = []
        z_coord = []
        for peak in self.peaks:
            x_coord.append(30*peak.location[1])
            y_coord.append(30*peak.location[0])
            z_coord.append(peak.altitude)
        data = go.Scatter3d(x=x_coord, y=y_coord, z=z_coord,
                            mode='markers',
                            marker={"size": [Z/50 for Z in z_coord],
                                    "color":z_coord,
                                    "colorscale":'Reds',
                                    "opacity":1,
                                    "symbol":'diamond'})
        return data
