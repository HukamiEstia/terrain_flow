"""
functions to handle the data.
"""

from osgeo import gdal
from PIL import Image
import plotly.graph_objects as go
import glob
import os

def load_heightmap(filename):
    """load a heightmap from file"""
    ds = gdal.Open(filename)
    bnd = ds.GetRasterBand(1) #1 based
    return bnd.ReadAsArray()

def data_iterator(directory, ext):
    """iterator to access multiple heightmaps successively."""
    for data_path in glob.glob(os.path.join(directory, f"*.{ext}")):
        heightmap = load_heightmap(data_path)
        yield heightmap

def save_map(heightmap, name):
    """save a heightmap to file."""
    im = Image.fromarray(heightmap)
    im.save(name)

def draw_heightmap(heightmap):
    """plot the heightmap."""
    data = go.Surface(x=[30*i for i in range(len(heightmap))],
                      y=[30*i for i in range(len(heightmap))],
                      z=heightmap,
                      colorscale="Greens")
    return data

def display_map(data):
    """show the map."""
    fig = go.Figure(data=data)

    fig.update_layout(title='DEM map', autosize=True,
                      margin={"l":0, "r":0, "b":0, "t":0},
                      scene_aspectmode='data',
                      scene={"xaxis":{"visible":False},
                             "yaxis":{"visible":False},
                             "zaxis":{"visible":False}})
    fig.show()
