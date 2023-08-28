
#   Libraries
import pygame as pg

import misc

#   Code
class App:

    BASEFPS = 60

    def __init__(self, testing=False):
        
        pg.init()

        self.caption = "Slippery Spaceship"
        self.display = pg.display.set_mode((960, 540), pg.RESIZABLE)
        self.running = False
        self.clock = misc.Clock()

        self._testing_font = pg.font.SysFont("Bahnschrift", 16)

        self._testing = testing

    @property
    def caption(self) -> str:
        return self._caption
    
    @caption.setter
    def caption(self, value: str):
        self._caption = value
        pg.display.set_caption(self._caption)

    def run(self):
        
        self.running = True

        while self.running:
            self.clock.tick()
            self.process_events()
            self.render()

        # just put cleanup code here :DD

        pg.quit()

    def render(self):

        self.display.fill((255, 255, 255))

        #   Rendering

        #   run if testing code
        if self._testing:
            #   Improve font rendering / make font renderer etc etc
            fps = self._testing_font.render(
                f"FPS: {round(self.clock._clock.get_fps())}", 
                True, (230, 50, 50))
            self.display.blit(fps, 
                (self.display.get_width() - fps.get_width() - 5, 
                 self.display.get_height() - fps.get_height() - 5))

        pg.display.update()

    def process_events(self):

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                break

            #   run if testing code
            if self._testing:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.running = False
                        break

if __name__ == "__main__":
    app = App(True)
    app.run()