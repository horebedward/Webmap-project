import folium
import pandas as pd
mapp = folium.Map(location = [31.4632269,74.3119976],
				  tiles = 'Stamen Terrain',zoom_start = 3 )
fgc = folium.FeatureGroup(name = 'Countries')
# for cordinates in [[31.4609683,74.3193185],[31.4509683,74.3493185]]:

def color(co):
	if co[0] == 'A':
		return 'red'
	elif co[0] == 'B':
		return 'blue'
	elif co[0] == 'C':
		return 'green'
	elif co[0] == 'G':
		return 'yellow'
	elif co[0] == 'M':
		return 'black'
	elif co[0] == 'N':
		return 'brown'
	elif co[0] == 'P':
		return 'purple'
	elif co[0] == 'S':
		return 'darkblue'
	elif co[0] == 'T':
		return 'pink'
	else:
		return 'grey'
	

data = pd.read_csv('countries.csv')


lat  = list(data['latitude'])
lon = list(data['longitude'])
con = list(data['country'])



for lt,ln,co in zip(lat,lon,con):
	
	fgc.add_child(folium.CircleMarker(location = [lt,ln],
							   popup = co, 
							   # tooltip = folium.Tooltip(color = color(co)) 
							   color = color(co),
							   fill=True,
							   radius = 8,
							   fill_opacity = 0.7
								))

fgp = folium.FeatureGroup(name = 'Population')

fgp.add_child(folium.GeoJson(open('world.json','r', encoding = 'utf-8-sig').read(),
							style_function = lambda x:{'fillColor': 'yellow'
											if x['properties']['POP2005'] < 10000000 
											else 'blue' 
											if 10000000 >= x['properties']['POP2005'] <= 20000000
											else 'red'}))


mapp.add_child(fgc)
mapp.add_child(fgp)
mapp.add_child(folium.LayerControl())
mapp.save('map1.html')