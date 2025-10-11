import pygame as pg
import dog
import images
import harakteristiki as har
import button
import menu_ojedja
import menu_eda
# Инициализация pg
pg.init()

# Размеры окна
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 550


class Game:
    def __init__(self):

        # Создание окна
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Виртуальный питомец")
        self.background  = pg.image.load("images/background.png")  
        self.background = pg.transform.scale(self.background,[SCREEN_WIDTH,SCREEN_HEIGHT])
        self.dog = dog.Doggy()
        self.golod = har.Harakter(images.golod,100,[0,0])
        self.health = har.Harakter(images.health,100,[0,100])
        self.money = har.Harakter(images.money,100,[0,200])
        self.happiness = har.Harakter(images.happiness,100,[0,300])
        self.eda = button.Button("eda",[200,100],[700,100])
        self.ojedja = button.Button("odejda",[200,100],[700,200])
        self.game = button.Button("game",[200,100],[700,300])
        self.menu_edya = menu_eda.Menu_eda(self)
        self.menu_ojejda = menu_ojedja.Menu_ojedja(self)
        self.sostoanie = 0 
        self.a = 1
        self.b = 2 
        self.run()
        
        

    def run(self):
        while self.a < self.b:
            self.update()
            if self.sostoanie == 0:
                self.event()

                self.draw()
            if self.sostoanie == 1:
                self.menu_edya.draw(self.screen)
                self.menu_edya.event()
            if self.sostoanie == 2:
                self.menu_ojejda.draw(self.screen)
                self.menu_ojejda.event()
    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.b =   -10000000000000000
                
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.dog.pramougol.collidepoint(event.pos) == True:
                    self.money.znachenie += 1 
                if self.ojedja.pramougolnik.collidepoint(event.pos) == True:
                    self.ojedja.click()
                    self.sostoanie = 2
                if self.eda.pramougolnik.collidepoint(event.pos) == True:
                    self.eda.click()
                    self.sostoanie = 1
                if self.game.pramougolnik.collidepoint(event.pos) == True:
                    self.game.click()
                
                
                

                
            if event.type == pg.MOUSEBUTTONUP:
                
                    self.ojedja.unclick()
                    self.eda.unclick()
                    self.game.unclick()
    def update(self):
        ...

    def draw(self):

        self.screen.blit(self.background,[0,0])
        self.dog.draw(self.screen)
        self.happiness.draw(self.screen)
        self.golod.draw(self.screen)
        self.money.draw(self.screen)
        self.health.draw(self.screen)
        self.eda.draw(self.screen)
        self.ojedja.draw(self.screen)
        self.game.draw(self.screen)


        pg.display.flip()
        

    

Game()
