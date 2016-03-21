# This application is Mapview Sample.(Kivy-garden)
from kivy.garden.mapview import MapView, MapMarkerPopup
from kivy.app import App

class MapViewApp(App):
    def build(self):
        #mapview = MapView(zoom=16, lat=35.689767500000, lon=139.767127800000)
        #lat: 35.681382 lon: 139.766084
        mapview = MapView(zoom=15, lat=35.681382, lon=139.766084)
        marker1 = MapMarkerPopup(lat=35.681382, lon=139.766084) 
        mapview.add_marker(marker1)
        return mapview
    
MapViewApp().run()
