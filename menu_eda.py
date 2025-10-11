import images
import pygame
import eda
import button
import random
import pygame.freetype

class Menu_eda:
    def __init__(self,game):
        self.kartinka = images.zagruzit_kart("images/menu/menu_page.png",[900,550])
        self.game = game
        self.pisatel = pygame.freetype.Font(None,25)
        self.foods = []
        self.dalee = button.Button("далее",[100,100],[50,50])
        self.nazad = button.Button("назад",[100,100],[500,50])
        self.buy = button.Button("купить",[100,100],[250,250])
        for food in images.foodkartinki:
            edaobject = eda.Eda(food,random.randint(100,250))
            self.foods.append(edaobject)
        self.a = 0
    def draw (self,okno):
        okno.blit(self.game.background,[0,0])
        okno.blit(self.kartinka,[0,0])
        self.nazad.draw(okno)
        self.dalee.draw(okno)
        self.buy.draw(okno)
        self.foods[self.a].draw(okno)
        self.pisatel.render_to(okno,[100,50],str(self.foods[self.a].cena))
        pygame.display.flip()
    def event (self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.b =   -10000000000000000
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.sostoanie = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.dalee.pramougolnik.collidepoint(event.pos):
                    self.dalee.click()
                    if self.a < 5 :
                        self.a = self.a + 1
                    else:
                        self.a = 0
                if self.nazad.pramougolnik.collidepoint(event.pos):
                    self.nazad.click()
                    if self.a >0:
                        self.a = self.a - 1
                    else:
                        self.a = 5
                if self.buy.pramougolnik.collidepoint(event.pos):
                    self.buy.click()
                    if self.foods[self.a].cena<=self.game.money.znachenie:
                        self.game.money.znachenie = self.game.money.znachenie - self.foods[self.a].cena
                        self.game.golod.znachenie = self.game.golod.znachenie + random.randint(1,20)

            if event.type == pygame.MOUSEBUTTONUP:
                self.dalee.unclick()
                self.nazad.unclick()
                self.buy.unclick()
                