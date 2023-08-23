#   Miscellaneous functionality for pixelsword :DD

#   Libraries
from time import time as _time

from pygame.time import Clock as _clock

#   Code
class Clock:
    def __init__(self, framerate=360, base_framerate=60):
        
        self._clock = _clock()

        self.framerate = framerate
        self.base_framerate = base_framerate
        self.delta_time = 0
        self._lt = 0

    def tick(self):
        self._clock.tick(360)

        self.delta_time = (_time() - self._lt) * self.base_framerate
        self._lt = _time()