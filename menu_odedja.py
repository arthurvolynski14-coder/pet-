import pygame
import images
import random
import button
import item
import pygame.freetype

class Menu_ojedja:
    def __init__ (self,game):
        self.game = game
        self.kartinka = images.zagruzit_kart("images/menu/menu_page.png",[900,550])
        self.dalee = button.Button("далее",[100,100],[50,50])
        self.nazad = button.Button("назад",[100,100],[500,50])
        self.buy = button.Button("купить",[100,100],[250,250])
        self.odedza = []
        for ozezda in images.odejdakartinki:
            ojedjaobject = item.Items(ozezda,random.randint(100,250))
            self.odedza.append(ojedjaobject)
        self.a = 0
        self.pisatel = pygame.freetype.Font(None,14)
    def draw(self,okno):
        okno.blit(self.game.background,[0,0])
        okno.blit(self.kartinka,[0,0])
        self.dalee.draw(okno)
        self.nazad.draw(okno)
        self.buy.draw(okno)
        self.pisatel.render_to(okno,[100,100],str(self.odedza[self.a].cena))
        
        self.odedza[self.a].draw(okno)
        
        pygame.display.flip()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.b = -1929392193921939219
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.sostoanie = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.dalee.pramougolnik.collidepoint(event.pos):
                    self.dalee.click()
                    if self.a < 9 :
                        self.a = self.a + 1
                    else:
                        self.a = 0
                if self.nazad.pramougolnik.collidepoint(event.pos):
                    self.nazad.click()
                    if self.a >0:
                        self.a = self.a - 1
                    else:
                        self.a = 9
            if event.type == pygame.MOUSEBUTTONUP:
                self.dalee.unclick()
                self.nazad.unclick()

