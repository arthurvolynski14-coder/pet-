import pygame as pg
import os

def zagruzit_kart(pyt,razmery):
    kartinka = pg.image.load(pyt)
    kartinka = pg.transform.scale(kartinka,razmery)
    return kartinka

golod = zagruzit_kart("images/satiety.png",[100,100])
health = zagruzit_kart("images/health.png",[100,100])
money = zagruzit_kart("images/money.png",[100,100])
happiness = zagruzit_kart("images/happiness.png",[100,100])
button = zagruzit_kart("images/button.png",[100,100])
button2 = zagruzit_kart("images/button_clicked.png",[100,100])
foodnames = os.listdir("images/food")
foodkartinki = []
odejdanames = os.listdir("images/items")
odejdakartinki = []


for foodname in foodnames:
    
    foodkartinka =  zagruzit_kart("images/food/"+foodname,[100,100])
    
    foodkartinki.append(foodkartinka)
for odejda228 in odejdanames:
    odejdakartinka = zagruzit_kart("images/items/"+odejda228,[100,100])
    odejdakartinki.append(odejdakartinka)