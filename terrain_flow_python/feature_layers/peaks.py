import numpy as np
from .featureLayer import FeatureLayer

class Peaks(FeatureLayer):

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.peaks = []