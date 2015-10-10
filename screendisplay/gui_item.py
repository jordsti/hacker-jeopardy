
class gui_item:
    def __init__(self, item_name, width=0, height=0):
        self.item_name = item_name
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0

    def draw(self, surface):
        pass