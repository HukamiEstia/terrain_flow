import numpy as np
from .toolbox import Toolbox

class BaseTool(Toolbox):

    def __init__(self, workspace):
        Toolbox.__init__(self, workspace)
        self.dirMap = np.array([[1,2,3],
                                [8,0,4],
                                [7,6,5]])

    def DetectSink(self):
        if self.GetAlt() < self.GetAlt(self.workArea[0]):
            return True
        else:
            return False

    def DetectPeak(self):
        if self.GetAlt() > self.GetAlt(self.workArea[-1]):
            return True
        else:
            return False

    def AssignDirection(self):

        # |1|2|3|
        # |8|0|4|
        # |7|6|5|

        if self.GetAlt(self.workArea[0]) < self.GetAlt():
            dx = self.workArea[0][0] - self.workPoint[0] + 1
            dy = self.workArea[0][1] - self.workPoint[1] + 1
            self.workspace.fd_matrix[self.workPoint[0],
                                     self.workPoint[1]] = self.dirMap[dx,dy]
        else:
            self.workspace.fd_matrix[self.workPoint] = 0

    def CountInputs(self):

        # |5|6|7|
        # |4|0|8|
        # |3|2|1|

        inputDirections = np.array([[5,6,7][4,0,8][3,2,1]])
        for point in self.workArea:
            i = self.workPoint[0] - point[0] + 1
            j = self.workPoint[1] - point[1] + 1
            if self.workspace.flowDirection[point] == inputDirections[i,j]:
                self.workspace.drainageInput[self.workPoint] += 1