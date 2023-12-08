#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 09:36:05 2023

@author: maxbld
"""

from pyroutelib3 import *
import folium
import webbrowser

router = Router("car")
depart = router.findNode(44.3843, 4.9903)
arrivee = router.findNode(44.3568, 4.7049)
status, route = router.doRoute(depart, arrivee)

if status == 'success':
    routeLatLons = list(map(router.nodeLatLon, route))
    print(routeLatLons)
    
c= folium.Map(location=[44.36, 4.85],zoom_start=12)
for coord in routeLatLons:
    coord=list(coord)
    folium.Marker(coord).add_to(c)
c.save('maCarte.html')

webbrowser.open("maCarte.html")
