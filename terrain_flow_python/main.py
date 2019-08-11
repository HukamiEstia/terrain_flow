from artist import Artist
from toolbox.workspace import Workspace
 
if __name__ == '__main__':
    artist = Artist('../data/n45_e006_1arc_v3.dt2', 
                    initialPoint = (0, 0),
                    height = 300, width = 300)
    
    artist.FindPeaks()
    print(len(artist.workspace.peaks))