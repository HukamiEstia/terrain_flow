import numpy as np
from .featureLayer import FeatureLayer
import plotly.graph_objects as go

class Sink():
    """store one sink's location and altitude"""

    __slots__ = ('location', 'altitude')

    def __init__(self, location, altitude):
        self.location = location
        self.altitude = altitude

class Sinks(FeatureLayer):
    """store all the sinks into a array"""

    __slots__ = (('height', 'width', 'Sinks'))

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.sinks = []

    def __len__(self):
        return len(self.sinks)

    def AddSink(self, location, altitude):
        """
        create a sink of given location and altitude
        and append it to the list of sinks.
        """
        self.sinks.append(Sink(location, altitude))

    def Draw(self):
        x_coord = []
        y_coord = []
        z_coord = []
        for sink in self.sinks:
            x_coord.append(30*sink.location[1])
            y_coord.append(30*sink.location[0])
            z_coord.append(sink.altitude)
        data = go.Scatter3d(x=x_coord, y=y_coord, z=z_coord,
                            mode='markers',
                            marker={"size": [Z/50 for Z in z_coord],
                                    "color":z_coord,
                                    "colorscale":'Blues',
                                    "opacity":1,
                                    "symbol":'diamond'})
        return data
