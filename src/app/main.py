from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import requests
import time
import datetime
import sqlite3
import commands

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods="GET",
    allow_headers=["*"]
)

class Album():
    def __init__(self, id, title, artist, price, image_url):
         self.id = id
         self.title = title
         self.artist = artist
         self.price = price
         self.image_url = image_url

albums = [ 
    Album(1, "You, Me and an App Id", "Daprize", 10.99, "https://aka.ms/albums-daprlogo"),
    Album(2, "Seven Revision Army", "The Blue-Green Stripes", 13.99, "https://aka.ms/albums-containerappslogo"),
    Album(3, "Scale It Up", "KEDA Club", 13.99, "https://aka.ms/albums-kedalogo"),
    Album(4, "Lost in Translation", "MegaDNS", 12.99,"https://aka.ms/albums-envoylogo"),
    Album(5, "Lock Down Your Love", "V is for VNET", 12.99, "https://aka.ms/albums-vnetlogo"),
    Album(6, "Sweet Container O' Mine", "Guns N Probeses", 14.99, "https://aka.ms/albums-containerappslogo")
]

@app.get("/")
def read_root():
    do_http_req()
    #do_sql_http()
    return {"Azure Container Apps Python Sample API"}


@app.get("/albums")
def get_albums():
    return albums

def do_http_req():
  x = requests.get('https://datadoghq.com')

#def do_sql_http():
#  dbname = 'test.sqlite3'
#  conn = sqlite3.connect(dbname)
#  cursor = conn.cursor()
#  cursor.execute('SELECT * FROM ai_ops_poc where id = 1')
#  print(cursor.fetchone())
#  conn.close()

#  do_http_req2()

#def do_http_req2():
#  y = requests.get('http://172.31.28.18/server-status?auto')
