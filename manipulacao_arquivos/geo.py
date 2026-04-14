from pygeocoder import Geocoder

endereço = "1222, Lins de vansconcelos, são paulo, SP"

print(Geocoder('AIzaSyACWaoDaZq0rUGHwc5lLOce7jPK6iTDHYs').geocode(endereço).coordinates)