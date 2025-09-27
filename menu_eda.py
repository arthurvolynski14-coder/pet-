import images
import pygame
import eda
import button
class Menu_eda:
    def __init__(self,game):
        self.kartinka = images.zagruzit_kart("images/menu/menu_page.png",[900,550])
        self.game = game
        self.foods = []
        self.dalee = button.Button("далее",[0,0],[50,50])
        for food in images.foodkartinki:
            edaobject = eda.Eda(food,100)
            self.foods.append(edaobject)
            
    def draw (self,okno):
        okno.blit(self.game.background,[0,0])
        okno.blit(self.kartinka,[0,0])
        self.foods[0].draw(okno)
        pygame.display.flip()
    def event (self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.b =   -10000000000000000
                