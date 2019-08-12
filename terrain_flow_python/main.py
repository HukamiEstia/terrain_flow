from artist import Artist
from toolbox.workspace import Workspace
 
if __name__ == '__main__':
    artist = Artist('../data/n45_e006_1arc_v3.dt2', 
                    initialPoint = (600, 600),
                    height = 300, width = 300)
    
    artist.ComputeFD_Matrix()
    print(artist.workspace.fd_matrix[295:, 295:])