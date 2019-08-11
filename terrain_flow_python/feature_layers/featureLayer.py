"""pythons objects representing features"""

class FeatureLayer:
    """base feature class"""

    def __init__(self):
        pass

    def GetAllPoints(self):
        raise NotImplementedError
