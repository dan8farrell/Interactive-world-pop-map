import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map([38.58,-99.09], zoom_start=6, tiles="Mapbox Bright")

fg_v = folium.FeatureGroup(name="Volcanoes")


def colorize(elevation):
	if elevation < 1000:
		return 'green'
	elif  1000<= elevation < 3000:
		return 'orange'
	else:
		return 'red'


for lt, ln, el in zip(lat, lon, elev):
	fg_v.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=str(el) + " m", fill_color=colorize(el), fill=True, color = 'grey', fill_opacity=0.8))

fg_p = folium.FeatureGroup(name="Population")

fg_p.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fg_v)
map.add_child(fg_p)
map.add_child(folium.LayerControl())

map.save("map1.html")