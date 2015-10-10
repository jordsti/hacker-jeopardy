import pygame
from pygame import display

class viewport:
    # Display Mode
    (Windowed, Fullscreen) = (0, 1)


    def __init__(self, width, height, mode=Windowed):
        self.width = width
        self.height = height
        self.mode = mode
        self.__run = False
        self.__state = None
        self.__screen = None
        self.background = 0, 0, 0
        self.__init_screen()

    def __init_screen(self):
        flags = 0

        flags |= pygame.DOUBLEBUF

        if self.mode == self.Fullscreen:
            flags |= pygame.FULLSCREEN

        self.__screen = pygame.display.set_mode((self.width, self.height), flags)

    def push(self, state):
        self.__state = state
        state.viewport = self

    def run(self):
        self.__run = True

        while self.__run:
            if self.__state is not None:
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        self.__run = False
                    else:
                        self.__state.on_event(e)

                self.__screen.fill(self.background)
                self.__state.tick()
                self.__state.on_paint(self.__screen)
                pygame.display.flip()

            else:
                print "Not state found!"
                self.__run = False

