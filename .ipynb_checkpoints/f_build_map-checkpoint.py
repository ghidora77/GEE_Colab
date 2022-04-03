import geemap


def build_map(lat, lon, zoom, vizParams, image, name):
    map = geemap.Map(center = [lat, lon], zoom = zoom)
    map.addLayer(image, vizParams, name)
    
    
    """
    map = folium.Map(location=[lat, lon], zoom_start=zoom)
    map.add_ee_layer(image, vizParams, name)
    map.add_basemap('ROADMAP')
    """
    return map