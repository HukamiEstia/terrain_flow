import numpy as np
from .featureLayer import FeatureLayer
import plotly.graph_objects as go

class Sink():

    __slots__ = ('location', 'altitude')

    def __init__(self, location, altitude):
        self.location = location
        self.altitude = altitude

class Sinks(FeatureLayer):

    __slots__ = (('height', 'width', 'Sinks'))

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.Sinks = []

    def __len__(self):
        return len(self.Sinks)

    def AddSink(self, location, altitude):
        self.Sinks.append(Sink(location, altitude))

    def Draw(self):
        x = []
        y = []
        z = []
        for Sink in self.Sinks:
            x.append(30*Sink.location[1])
            y.append(30*Sink.location[0])
            z.append(Sink.altitude)
        data = go.Scatter3d(x=x, y=y, z=z,
                            mode='markers',
                            marker={"size": [Z/50 for Z in z],
                                    "color":z,
                                    "colorscale":'Blues',
                                    "opacity":1,
                                    "symbol":'diamond'})
        return data