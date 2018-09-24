"""Program for reading shapefile and plot coordinates on Google map. It uses gmplot package for plotting
coordinates on street view map
"""

import io
import sys
import os
import geopandas as gp
from shapely.geometry import Point
import gmplot

def mapPlotter(argv):
    current_dir = os.getcwd()
    shp_name = sys.argv[1]
    fp = 'shapefiles/' + shp_name
    
    try:
        with io.open(fp, 'r', encoding='utf-8') as f:
            all_loc = gp.GeoDataFrame.from_file(fp)
            
            lons = []
            lats = []
            for index, row in all_loc.iterrows():
                for pt in list(row['geometry'].coords):
                    lons.append(pt[0])
                    lats.append(pt[1])
                    
            # Define center of map
            gmap = gmplot.GoogleMapPlotter(34.834206, -102.388633, 13)
            
            gmap.scatter(lats, lons, color='red', size=300, marker=False)
            op_fn = shp_name + '.html'
            gmap.draw(op_fn)
            
    except IOError as err:
        print 'Unable to open file "{0}". Check if file exists or it has appropriate permissions.'.format(fp)
        

if __name__ == "__main__":
    mapPlotter(sys.argv[1:])