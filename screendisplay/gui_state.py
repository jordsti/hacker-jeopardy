import base_state


class gui_state(base_state.base_state):
    def __init__(self):
        base_state.base_state.__init__(self)
        self.items = []

    def on_paint(self, screen):
        for i in self.items:
            i.draw(screen)
