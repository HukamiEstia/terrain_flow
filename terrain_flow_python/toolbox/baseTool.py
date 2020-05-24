"""
tool to perform simple tasks or preprocesing. 
"""
import numpy as np
from .toolbox import Toolbox

class BaseTool(Toolbox):
    """
    To find simple features such as peaks or sinks
    and perform precossing tasks such as map the flow
    direction.
    """
    def __init__(self, workspace):
        Toolbox.__init__(self, workspace)
        self.DIR_MAP = np.array([[1, 2, 3],
                                 [8, 0, 4],
                                 [7, 6, 5]])
        self.INPUT_MAP = np.array([[5, 6, 7],
                                   [4, 0, 8],
                                   [3, 2, 1]])

    def DetectSink(self):
        """check wether the current working point is a sink."""
        if self.GetAlt() < self.GetAlt(self.work_area[0]):
            return True
        else:
            return False

    def DetectPeak(self):
        """check wether the current working point is a peak."""
        if self.GetAlt() > self.GetAlt(self.work_area[-1]):
            return True
        else:
            return False

    def AssignDirection(self):
        """Assign a value to each point representing the direction
        of the steepest descent."""
        # |1|2|3|
        # |8|0|4|
        # |7|6|5|

        if self.GetAlt(self.work_area[0]) < self.GetAlt():
            dx = self.work_area[0][0] - self.work_point[0] + 1
            dy = self.work_area[0][1] - self.work_point[1] + 1
            self.workspace.fd_matrix[self.GetWorkPoint()] = self.dirMap[dx,dy]
        else:
            self.workspace.fd_matrix[self.GetWorkPoint()] = 0

    def CountInputs(self):
        """Count the number of upstream points of each point."""
        # |5|6|7|
        # |4|0|8|
        # |3|2|1|

        for point in self.work_area:
            dx = self.work_point[0] - point[0] + 1
            dy = self.work_point[1] - point[1] + 1
            if self.workspace.fd_matrix[point] == self.INPUT_MAP[dx,dy]:
                print('in_matrix workpoint',
                      self.workspace.in_matrix[self.GetWorkPoint()])
                self.workspace.in_matrix[self.GetWorkPoint()] += 1
