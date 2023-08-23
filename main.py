
#   Libraries
import pygame

import misc

#   Code
class App:

    BASEFPS = 60

    def __init__(self, testing=False):
        
        pygame.init()

        self.caption = "Pixelsword"
        self.display = pygame.display.set_mode((960, 540), pygame.RESIZABLE)
        self.running = False
        self.clock = misc.Clock()

        self.testing_font = pygame.font.SysFont("Bahnschrift", 16)

        self._testing = testing

    @property
    def caption(self):
        return self._caption
    
    @caption.setter
    def caption(self, value: str):
        self._caption = value
        pygame.display.set_caption(self._caption)

    def run(self):
        
        self.running = True

        while self.running:
            self.clock.tick()
            self.process_events()
            self.render()

        # just put cleanup code here :DD

        pygame.quit()

    def render(self):

        self.display.fill((255, 255, 255))

        #   Rendering

        #   run if testing code
        if self._testing:
            #   Improve font rendering / make font renderer etc etc
            fps = self.testing_font.render(
                f"FPS: {round(self.clock._clock.get_fps())}", 
                True, (230, 50, 50))
            self.display.blit(fps, 
                (self.display.get_width() - fps.get_width() - 5, 
                 self.display.get_height() - fps.get_height() - 5))

        pygame.display.update()

    def process_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break

            #   run if testing code
            if self._testing:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        break

if __name__ == "__main__":
    app = App(True)
    app.run()