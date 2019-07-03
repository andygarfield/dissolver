import os
import tempfile
from flask import Flask, request, make_response
import geopandas as gpd


app = Flask(__name__)


@app.route("/")
def hello():
    with open('./index.html') as index:
        return index.read()

@app.route("/dissolve", methods=['POST'])
def dissolve():
    with tempfile.NamedTemporaryFile('w+', delete=False) as geofile:
        fn = geofile.name
        geofile.write(request.get_data(as_text=True))
    gdf = gpd.read_file(fn, driver='GeoJSON')
    gdf = gdf[gdf.geometry.notnull()]

    # delete file
    os.remove(fn)
    
    return gpd.GeoSeries(gdf.unary_union).to_json()

