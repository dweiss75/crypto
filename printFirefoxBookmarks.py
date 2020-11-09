# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 13:32:35 2020

@author: dw
"""

import sqlite3
import pandas as pd

from helper import get_firefox_path

path = get_firefox_path("places.sqlite")
conn = sqlite3.connect(path)

bookmarks = pd.read_sql("SELECT * FROM moz_bookmarks", conn)
places = pd.read_sql("SELECT * FROM moz_places", conn)

for key, bookmark in bookmarks[bookmarks["fk"] > 0].iterrows():
    title = bookmark["title"]
    url = places[places["id"] == int(bookmark["fk"])].iloc[0]["url"]
    
    print(title + ": " + url)