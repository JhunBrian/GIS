import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import os
from dotenv import load_dotenv

import pystac_client
import planetary_computer as pc
import odc
from odc.stac import stac_load
from odc.algo import to_rgba


class QuerySatelliteImage:
    def __init__(self, coord:tuple, box_size, time_window, sensor:list=["sentinel-2-l2a"]):
        self.coord = coord 
        self.box_size = box_size
        self.time_window = time_window
        self.sensor = sensor
        self.endpoint = "https://planetarycomputer.microsoft.com/api/stac/v1"
        
        load_dotenv()
        pc.settings.set_subscription_key(os.environ.get("PC_KEY"))
        
    def query(self):
        min_lon = self.coord[1]-self.box_size/2
        min_lat = self.coord[0]-self.box_size/2
        max_lon = self.coord[1]+self.box_size/2
        max_lat = self.coord[0]+self.box_size/2
        self.__bounds = (min_lon, min_lat, max_lon, max_lat)

        stac = pystac_client.Client.open(self.endpoint)
        search = stac.search(collections=self.sensor, bbox=self.__bounds, datetime=self.time_window)
        self.__items = list(search.get_all_items())
        print(f"There are {len(self.__items)} scenes for this region.")
        
    def get_stac_load(self, resolution, bands:list=['red','green','blue'], crs:str='EPSG:4326', chunks:dict={'x':2048, 'y':2048}):
        self.__scale = resolution / 111320.0 # degrees per pixel for CRS:4326 
        self.xx = stac_load(
        self.__items,
        bands=bands,
        crs=crs, # Latitude-Longitude
        resolution=self.__scale, # Degrees
        chunks=chunks,
        dtype="uint16",
        patch_url=pc.sign,
        bbox=self.__bounds
        )
        display(self.xx)
        
    def visualize_scenes(self, vmax, col_wrap=4, bands:list=['red','green','blue']):
        plot_xx = self.xx[bands].to_array()
        plot_xx.plot.imshow(col='time', col_wrap=4, robust=True, vmin=0, vmax=vmax)
        plt.show()