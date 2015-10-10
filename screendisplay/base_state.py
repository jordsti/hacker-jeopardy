

class base_state:
    def __init__(self):
        self.viewport = None
        pass

    def width(self):
        return self.viewport.width

    def height(self):
        return self.viewport.height

    def on_event(self, e):
        pass

    def on_paint(self, screen):
        pass

    def tick(self):
        pass
